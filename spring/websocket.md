# WebSocket

[SSE](sse.md) 를 쓰고 나서 웹소켓도 쓸 일이 생겼다. 처음엔 "둘 중 하나만 쓰면 되는데 왜 둘 다 쓰나" 싶었는데 써보니 자리가 다르다.

```
수집기 ──[WebSocket]──▶ 관리 서버 ──[SSE]──▶ 브라우저
       ◀──설정 변경───┘
```

브라우저는 받기만 하면 되니까 SSE다. 수집기는 데이터를 올려보내고 설정 변경을 받아야 해서 양쪽이 필요하다. 그래서 웹소켓이다. **양방향이 필요해서 웹소켓인 거지, 실시간이라서 웹소켓인 게 아니다.** 이걸 구분하는 데 한참 걸렸다.

## 받는 쪽은 SSE랑 똑같이 생겼다

서버가 `TextWebSocketHandler` 를 상속하고 콜백 네 개를 채운다.

```java
public class CollectorWebSocket extends TextWebSocketHandler {

    public static final Map<String, CollectorSession> channelMgmt = new ConcurrentHashMap<>();

    @Override public void afterConnectionEstablished(WebSocketSession session) { ... }
    @Override protected void handleTextMessage(WebSocketSession session, TextMessage message) { ... }
    @Override public void afterConnectionClosed(WebSocketSession session, CloseStatus status) { ... }
    @Override public void handleTransportError(WebSocketSession session, Throwable e) { ... }
}
```

`ConcurrentHashMap` 에 세션을 들고 있는 게 [SSE](sse.md) 의 `EMITTERS` 랑 같다. 처음엔 "웹소켓은 프레임워크가 세션 관리해주겠지" 했는데 아니다. **열린 연결에 나중에 보내려면 직접 들고 있어야 한다.** 이건 SSE든 웹소켓이든 같은 문제다.

```java
channelMgmt.put(session.getId(), collectorSession);   // 접속하면 등록
...
channelMgmt.remove(session.getId());                   // 끊기면 제거
```

차이는 `onTimeout` 같은 게 없는 거다. 웹소켓은 수명 제한이 없다. 붙어 있으면 계속 붙어 있다.

## 인증을 핸드셰이크가 아니라 첫 메시지로 했다

여기서 좀 헤맸다. 웹소켓 핸드셰이크는 HTTP GET이다. **바디가 없다.**

```
GET /ws/collector HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: ...
```

그러니까 로그인 폼처럼 아이디·비번을 실어 보낼 자리가 없다. 쿼리 파라미터나 헤더에 넣는 방법이 있는데, 쿼리는 URL이라 로그에 다 찍히고 헤더는 브라우저 `WebSocket` API에서 못 넣는다.

그래서 연결은 일단 받고 **첫 메시지의 키로 인증**한다.

```java
if (!collectorSession.isAuthStatus()) {
    CollectorVo vo = authHandler(apiKey);
    if (vo != null) {
        collectorSession.setAuthStatus(true);
    } else {
        closeSessionList.add(sessionId);      // 인증 실패 → 끊는다
    }
}
```

인증 안 된 세션도 Map에는 들어가 있다. 그래서 세션을 훑을 때마다 `isAuthStatus()` 를 봐야 한다. 이걸 빼먹어서 인증 안 된 세션을 정상 연결로 센 적이 있다.

## 보낼 데이터가 없으면 끊긴 것처럼 보였다

소켓은 붙어 있는데 화면에 계속 "연결 끊김"으로 떴다. 한참 봤는데 원인이 이거였다.

서버가 **첫 메시지를 받았을 때** 연결 상태를 기록한다. 소켓이 붙은 시점이 아니다. 그러니까 수집기가 연결만 하고 보낼 데이터가 없으면 서버 입장에서는 "인증도 안 된 정체불명 세션"이라 끊김으로 남아 있다.

그래서 연결 직후에 인증 전용 메시지를 한 번 보낸다.

```java
@Override
public void onOpen(ServerHandshake handshake) {
    sendAuthMessage();        // apiKey + messageType=AUTH 만 담긴 메시지
}
```

서버는 이 타입이면 인증만 하고 나머지 처리를 건너뛴다.

```java
if ("AUTH".equals(preMessageType)) {
    sendApiHeader = null;     // 응답·이력·로그가 무의미하다
    return;
}
```

SSE에서 "연결 직후 빈 이벤트 보내기"랑 모양이 같아서 같은 문제인 줄 알았는데 이유가 다르다.

| | 왜 첫 메시지를 보내나 |
|---|---|
| SSE | 바이트를 안 보내면 **프록시·컨테이너가 끊는다** |
| WebSocket | 연결은 유지되는데 **서버가 상태를 갱신할 계기가 없다** |

SSE는 연결이 실제로 끊기는 문제고, 웹소켓은 연결은 멀쩡한데 표시가 틀리는 문제다.

## 같은 클라가 두 번 붙으면 좀비가 남는다

클라가 재연결하면 서버에는 세션이 두 개가 된다. 옛 세션이 아직 안 닫혀 있을 수 있다. 끊긴 걸 서버가 바로 아는 게 아니니까.

그러면 "연결된 수집기 수"가 뻥튀기되고, 옛 세션으로 보낸 메시지는 허공으로 간다.

그래서 인증 성공 시점에 같은 클라의 다른 세션을 찾아서 끊는다.

```java
// 같은 IP + 같은 식별자를 가진 다른 세션이 있으면 옛 세션을 종료
if (searchSession.getSocketAddress().equals(current.getSocketAddress())
        && searchConnectId.equals(newConnectId)) {
    closeSessionList.add(searchKey);
}
```

비교 기준을 뭘로 할지에서 한 번 틀렸다. 처음엔 시스템 ID로 비교했는데, 인증 쿼리에 `GROUP BY` 가 있어서 **행이 합쳐질 때 ID를 임의로 하나 고른다.** 같은 클라가 붙을 때마다 다른 ID로 인증되니까 "같은 클라"로 안 묶인다. 중복을 못 걸러서 좀비가 쌓였다.

연결 단위로 고유한 값을 따로 쓰는 걸로 바꿨다. **비교 키는 "같다"의 정의가 안 흔들리는 값이어야 한다.**

## 끊김 콜백이 늦게 와서 "연결됨"을 덮어썼다

제일 재밌었던 버그다. 데이터는 잘 들어오는데 상태가 "끊김"으로 고정됐다.

`handleTextMessage` 가 오래 걸리면 (대량 insert + 트랜잭션) `afterConnectionClosed` 가 그만큼 늦게 불린다. 그 사이에 클라가 재접속해서 **새 세션이 이미 "연결됨"을 기록**해놨다. 그런데 뒤늦게 깨어난 옛 세션의 종료 콜백이 "끊김"을 덮어쓴다.

```
옛 세션 끊김 발생
   ↓ (수신 처리가 길어서 콜백이 밀림)
클라 재접속 → 새 세션 → "연결됨" 기록
   ↓
드디어 옛 세션 afterConnectionClosed 실행 → "끊김" 기록   ← 덮어씀
   ↓
데이터는 새 세션으로 계속 들어오는데 화면은 끊김
```

한 번 덮어쓰면 다음 상태 변경이 있을 때까지 안 풀린다. 데이터가 들어온다고 상태를 다시 쓰는 게 아니니까.

고친 방법은 쓰기 전에 확인하는 거다.

```java
// 같은 대상을 담당하는 다른 세션이 살아있으면 끊김을 기록하지 않는다
if (hasLiveSessionForUnits(session.getId(), vo.getUnitIds())) {
    LOGGER.info("같은 대상을 담당하는 세션이 살아있어 끊김 상태 기록을 건너뜀");
} else {
    vo.setConnectStatus(false);
    statusHandler(vo);
}
```

그 확인 함수에서도 세 가지를 걸러야 했다.

```java
if (entry.getKey().equals(excludeSessionId)) continue;        // 자기 자신
if (!searchSession.isAuthStatus()) continue;                  // 인증 안 된 세션
if (!searchSession.getSession().isOpen()) continue;           // Map에 남은 죽은 세션
```

자기 자신을 "살아있는 다른 세션"으로 세면 **아무도 끊김을 못 기록한다.** 죽은 세션을 살아있다고 보면 영원히 연결됨으로 남는다.

콜백이 **순서대로 온다는 보장이 없다**는 게 핵심이다. 콜백에서 공유 상태를 쓸 거면 "지금 쓰는 게 최신인가"를 봐야 한다.

## 재연결을 콜백 안에서 하면 안 된다

이 프로젝트에 웹소켓 클라이언트가 두 개 있는데, 하나는 먼저 만든 거고 하나는 겪고 나서 고친 거다. 차이가 그대로 교재였다.

### 먼저 만든 쪽

```java
@Override
public void onClose(int code, String reason, boolean remote) {
    // 5초 대기
    long setTime = System.currentTimeMillis() + 5000;
    while (System.currentTimeMillis() < setTime) {
        Thread.sleep(1000);
    }
    connectManager(URL);        // 여기서 다시 연결
}
```

문제가 세 개다.

- **콜백 스레드를 붙잡는다.** `onClose` 는 웹소켓 라이브러리 스레드에서 불린다. 거기서 5초를 자면 그 스레드가 그동안 아무것도 못 한다.
- **재귀로 쌓인다.** 재연결이 실패하면 또 `onClose` 가 불리고 거기서 또 `connectManager` 를 부른다. 서버가 오래 죽어 있으면 스택이 계속 깊어진다.
- **`onClose` 가 안 오면 영원히 안 붙는다.** 재연결 경로가 `onClose` 하나뿐이라 그게 유실되면 끝이다.

### 고친 쪽

재연결을 **콜백에서 떼어내서 주기적으로 도는 감시 스레드 하나**에 몰았다.

```java
public static synchronized void startWatchdog() {
    if (watchdogStarted) return;
    watchdogStarted = true;
    scheduler().scheduleWithFixedDelay(() -> {
        if (isConnected()) return;
        connect(URL);                  // 끊겨 있으면 붙인다
    }, 5, 5, TimeUnit.SECONDS);
}
```

그리고 `onClose` 에서는 재연결을 **안 한다**.

```java
@Override
public void onClose(int code, String reason, boolean remote) {
    LOGGER.error("연결 끊김 code=" + code + " remote=" + remote);
    IS_CONNECTING = false;
    // 재연결은 워치독이 전담한다. 여기서 예약하면 두 경로가 중복으로 시도한다
}
```

이게 제일 큰 배움이었다. **재연결 경로는 하나여야 한다.** 둘이면 동시에 두드려서 세션이 두 개 생기고, 그중 하나는 아무도 안 쓰는 유령이 된다.

워치독으로 몰면 덤도 있다. `onClose` 가 유실되든 `onError` 만 오든 부팅 시 서버가 아직 안 떠 있든, **5초 뒤에 또 확인하니까** 다 복구된다. 상태를 추적하는 게 아니라 주기적으로 사실을 확인하는 방식이다.

`remote` 플래그는 알아두면 편하다. `true` 면 서버가 끊은 거고 `false` 면 내가 끊은 거다. 로그에 찍어두면 원인 찾을 때 반은 줄어든다.

## isOpen() 이 거짓말을 한다

```java
public static boolean isConnected() {
    return webSocketClient != null && webSocketClient.isOpen();
}
```

이게 `true` 인데 데이터가 안 가는 상황이 있었다. 랜선을 빼거나 중간 NAT이 세션을 버리면 **양쪽 다 끊긴 걸 모른다.** TCP는 보내려고 시도해봐야 안다. 하프오픈이다.

먼저 만든 쪽은 이랬다.

```java
setConnectionLostTimeout(0);     // 하트비트 끔
```

`0` 은 비활성이다. 그러니까 연결이 죽어도 라이브러리가 모르고, `isOpen()` 은 계속 `true` 를 돌려주고, 워치독도 "연결돼 있네" 하고 지나간다. **감시가 있어도 안 잡힌다.**

```java
setConnectionLostTimeout(30);    // 30초마다 ping, 응답 없으면 끊김 처리
```

웹소켓 프로토콜에 ping/pong 프레임이 있다. 주기적으로 찔러보고 응답이 없으면 끊긴 걸로 본다. 이걸 켜야 `isOpen()` 이 사실을 말한다.

하프오픈 감지는 공짜가 아니다. 켜야 한다.

## 포기한 연결이 나중에 혼자 성공한다

이건 예상 못 했다.

```java
boolean result = newClient.connectBlocking(10, TimeUnit.SECONDS);
```

제한시간을 둔 이유는 방화벽이 SYN을 버리면 응답이 영원히 안 와서다. 인자 없는 `connectBlocking()` 은 무한 대기고, 이 메서드가 `synchronized` 안에 있으면 **락을 쥔 채로 매달려서** 다른 재연결도 다 막힌다.

그런데 제한시간이 지나도 `false` 만 돌려줄 뿐 **연결 시도를 멈추지는 않는다.** 그래서 15초 뒤에 혼자 연결이 되고, 서버에는 아무 데이터도 안 보내는 세션이 남는다. 유령 세션이다. 서버는 그걸 정상 연결로 센다.

그래서 포기할 때 폐기 표시를 하고 닫는다.

```java
if (!result) {
    IS_CONNECTING = false;
    newClient.retired = true;      // 폐기 표시
    newClient.close();
}
```

표시를 하는 이유는 뒤늦게 `onOpen` 이 왔을 때 **스스로 닫게** 하려는 거다.

```java
@Override
public void onOpen(ServerHandshake handshake) {
    if (retired || this != WebSocketSession.webSocketClient) {
        close();                   // 나는 이미 버려진 인스턴스다
        return;
    }
    IS_CONNECTING = false;
    sendAuthMessage();
}
```

`this != 현재 클라이언트` 비교도 같은 목적이다. 새 인스턴스로 교체됐으면 옛 인스턴스의 콜백은 전부 무효다. 이걸 안 걸면 옛 인스턴스의 `onClose` 가 공유 플래그를 내려서 **진행 중인 새 연결의 판단을 깨뜨린다.**

```java
@Override
public void onClose(...) {
    if (retired || this != WebSocketSession.webSocketClient) {
        return;      // 폐기된 인스턴스의 종료는 우리가 닫은 거다
    }
    ...
}
```

인스턴스를 갈아끼우는 구조에서는 **콜백이 "나 아직 현역인가"를 물어봐야 한다.** 비동기 콜백은 늦게 오고, 늦게 온 시점의 세상은 이미 달라져 있다.

## 플래그 하나가 재연결을 영구히 막았다

동시에 두 번 연결하는 걸 막으려고 플래그를 뒀다.

```java
private static volatile boolean IS_CONNECTING = false;
```

`volatile` 인 이유는 워치독 스레드가 쓰고 송신 스레드가 읽어서다. 없으면 각 스레드가 자기 캐시의 옛 값을 본다.

문제는 이 플래그가 **내려가지 않는 경로**가 생길 수 있다는 거다. 연결 시도 중에 예상 못 한 예외가 나거나 스레드가 죽으면 `true` 로 남는다. 그러면 워치독이 5초마다 와서 "연결 중이네" 하고 그냥 돌아간다. **영구히 안 붙는다.**

```java
if (IS_CONNECTING) {
    long stuckMs = System.currentTimeMillis() - connectStartedAt;
    if (stuckMs > CONNECT_TIMEOUT_SEC * 3000L) {
        LOGGER.warn("연결 시도 플래그가 {}ms 째 남아 있어 강제 해제합니다", stuckMs);
        IS_CONNECTING = false;
    } else {
        return;
    }
}
```

시작 시각을 같이 기록해두고, 제한시간의 3배가 지났으면 강제로 푼다.

"중복 방지 플래그"를 둘 때는 **못 내려가는 경우**를 같이 생각해야 한다. 플래그는 상태인데 상태는 꼬인다. 꼬였을 때 스스로 풀 방법이 없으면 그 기능은 영구히 죽는다. 워치독을 둬도 소용없다 — 워치독이 그 플래그를 보고 돌아가니까.

## 브라우저에서 웹소켓은 재연결이 공짜가 아니다

브라우저쪽 코드는 이게 다였다.

```js
webSocket = new WebSocket(wsProtocol + location.host + url);
webSocket.onopen  = function(e) { webSocket.send("connect Client"); };
webSocket.onclose = function(e) { webSocket = null; };
```

끊기면 `null` 로 만들고 끝이다. **재연결이 없다.** 그래서 네트워크가 한 번 끊기면 새로고침해야 한다.

SSE 쪽은 `EventSource` 가 알아서 재연결한다. 간격을 못 고르는 게 불만이라 직접 백오프를 짰지만, **안 짰어도 붙기는 붙는다.**

| | 재연결 | 끊김 감지 |
|---|---|---|
| EventSource (SSE) | 브라우저가 자동 | 자동 |
| WebSocket | **직접 만들어야 함** | ping/pong 직접 |

웹소켓은 날것이다. 양방향을 주는 대신 연결 관리를 다 떠넘긴다. 서버쪽에서 워치독·폐기 플래그·하트비트를 다 만든 것도 결국 같은 이유다. **SSE에서 공짜로 받던 걸 웹소켓에서는 직접 만들어야 한다.**

## 그래서 뭘 쓸까

| | SSE | WebSocket |
|---|---|---|
| 방향 | 서버 → 클라 | 양방향 |
| 프로토콜 | HTTP 그대로 | 핸드셰이크 후 업그레이드 |
| 재연결 | 브라우저 자동 | 직접 |
| 끊김 감지 | 자동 | ping/pong 설정 |
| 인증 | 쿠키·세션 그대로 | 첫 메시지로 직접 |
| 프록시 | 신경 안 씀 | 업그레이드 통과 설정 필요 |

클라가 서버로 보낼 게 없으면 SSE가 거의 항상 낫다. 할 일이 적다.

양방향이 필요하면 웹소켓인데, 그때 늘어나는 일은 메시지를 양쪽으로 보내는 게 아니라 **연결을 살려두는 쪽**이다. 처음엔 "양방향이니까 핸들러 하나 더 쓰면 되겠지" 했는데, 실제로 늘어난 코드는 거의 다 재연결·중복 세션·유령 세션·하프오픈 처리였다.

---

웹소켓에서 어려운 건 메시지를 주고받는 게 아니었다. 연결이 **살아있는지 아닌지를 아는 것**이었다. `isOpen()` 은 거짓말을 하고, 끊김 콜백은 늦게 오거나 안 오고, 포기한 연결은 혼자 되살아난다. 그래서 상태를 믿는 대신 주기적으로 확인하는 쪽으로 갔다.
