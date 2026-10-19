# SSE (Server-Sent Events)

대시보드 숫자가 새로고침 없이 바뀌어야 해서 썼다. 처음엔 웹소켓을 생각했는데 써보니 과했다.

## 폴링이랑 뭐가 다르냐

폴링은 클라가 계속 묻는다.

```
클라 ──새 거 있어?──▶ 서버 ──없어──▶   (3초 뒤)
클라 ──새 거 있어?──▶ 서버 ──없어──▶   (3초 뒤)
클라 ──새 거 있어?──▶ 서버 ──있다!──▶
```

대부분 "없어"다. 그 "없어"를 받으려고 요청을 계속 만든다. 3초 간격이면 늦고, 1초로 줄이면 요청이 세 배가 된다.

SSE는 한 번 묻고 연결을 안 끊는다.

```
클라 ──생기면 알려줘──▶ 서버
                        (연결 유지...)
             서버 ──생겼다!──▶ 클라
             서버 ──또 생겼다!──▶ 클라
```

웹소켓하고 헷갈렸는데 차이는 방향이다.

| | 방향 | 프로토콜 | 클라 코드 |
|---|---|---|---|
| 폴링 | 클라가 요청 | HTTP | setInterval + ajax |
| SSE | 서버 → 클라 | HTTP 그대로 | `new EventSource(url)` |
| 웹소켓 | 양방향 | ws:// 로 업그레이드 | 연결·재연결 직접 |

내가 필요한 건 "서버가 알려주기"뿐이었다. 클라가 서버로 올려보낼 건 없다. 웹소켓은 양방향이라 안 쓰는 절반을 떠안는 거고 [프로토콜](../network/http.md)이 바뀌니까 프록시 설정까지 손봐야 한다. SSE는 그냥 HTTP라 Content-Type만 바꾸면 된다.

양방향이 진짜로 필요한 쪽은 따로 썼다. → [WebSocket](websocket.md)

```java
@RequestMapping(value = "/subscribe", method = RequestMethod.GET, produces = "text/event-stream")
public SseEmitter subscribe() { ... }
```

받는 쪽은 브라우저 기본 API라 한 줄이다.

```js
const eventSource = new EventSource('/sse/subscribe');
eventSource.addEventListener('sse', e => { ... });
```

## 서버가 연결을 들고 있어야 한다

여기서 제일 먼저 막혔다.

평소 HTTP는 응답하면 끝이다. 근데 SSE는 응답이 안 끝난다. 나중에 보내려면 **그 열린 응답을 어딘가 쥐고 있어야** 한다. 컨트롤러 메서드가 return하면 지역변수는 사라지니까.

그 손잡이가 `SseEmitter`고, 보관함은 직접 만들어야 한다.

```java
private static final Map<String, EmitterWrapper> EMITTERS = new ConcurrentHashMap<>();
```

`HashMap`이 아니라 `ConcurrentHashMap`인 이유는 넣는 쪽과 꺼내는 쪽이 다른 스레드라서다. 구독은 웹 요청 스레드가 `put` 하고, 전송은 데이터 들어오는 쪽 스레드가 순회하면서 꺼낸다. 동시에 건드린다.

구독이 "접속"이 아니라 "**Map에 등록**"이라는 게 처음에 안 와닿았다. 연결은 브라우저가 맺고, 서버가 하는 일은 그 연결을 잃어버리지 않게 적어두는 거다.

## 탭을 2개 열면 한쪽이 안 온다

처음엔 Map 키를 세션 하나로 했다. 그러니까 같은 사람이 탭을 두 개 열면 두 번째 `put` 이 첫 번째를 덮는다.

```
탭A 구독 → EMITTERS["abc"] = 탭A
탭B 구독 → EMITTERS["abc"] = 탭B      ← 탭A 덮임
전송     → 탭B만 받는다
```

덮인 탭A는 연결 자체는 살아 있다. 끊긴 게 아니라서 재연결도 안 한다. 그냥 조용히 아무것도 안 온다. 이게 제일 찾기 어려웠다. 에러가 안 나니까.

키에 탭을 섞으면 공존한다.

```java
String connectionKey = hashKey + "_" + tabId;
```

탭 ID는 클라가 만들어서 보낸다. 여기서 한 번 더 틀렸다. 처음에 `localStorage` 에 저장했는데 그러면 모든 탭이 같은 ID를 공유해서 원점이다.

```js
let tabId = sessionStorage.getItem('sseTabId');
if (!tabId) {
    tabId = Math.random().toString(36).substring(2, 10);
    sessionStorage.setItem('sseTabId', tabId);
}
```

| | 범위 | 언제 사라지나 |
|---|---|---|
| localStorage | 브라우저 전체 | 직접 지울 때까지 |
| sessionStorage | 탭 하나 | 탭 닫으면 |

`sessionStorage` 는 탭마다 따로 생기고 탭 닫으면 없어진다. 내가 원한 "탭 단위"랑 수명이 정확히 같다. 새로고침에는 남는데 이것도 맞다. 같은 탭이니까 같은 ID를 써야 한다.

## 안 지우면 쌓인다

Map에 넣었으면 빼야 한다. 빠지는 경로가 세 개다.

```java
sseEmitter.onCompletion(() -> deleteById(key));  // 정상 종료
sseEmitter.onTimeout(()    -> deleteById(key));  // 타임아웃
sseEmitter.onError(e       -> deleteById(key));  // 에러
```

`onError` 를 처음에 빼먹었다. 그러면 깨진 연결이 Map에 영구히 남는다. 그 상태로 전체 전송을 돌리면 매번 그 시체를 붙잡고 예외가 난다. 1000개 중 900개가 시체면 전송 한 번에 900번 실패한다. 접속자는 안 늘었는데 서버만 바빠진다.

로그도 한 번 갈랐다.

```java
if (e instanceof AsyncRequestNotUsableException || e instanceof IOException) {
    logger.debug(...);   // 탭 닫음. 정상이다
} else {
    logger.error(...);   // 진짜 문제
}
```

브라우저 탭을 닫으면 `IOException` 이 난다. 이건 에러가 아니라 일상인데 `error` 로 찍으면 로그가 전부 이거다. 진짜 에러가 안 보인다.

## 연결만 하고 가만히 있으면 끊긴다

구독 직후에 빈 이벤트를 하나 보낸다.

연결만 열고 바이트를 하나도 안 보내면 중간의 프록시나 서블릿 컨테이너가 "응답 안 주는 요청"으로 보고 잘라버린다. 첫 바이트를 흘려서 스트림이 살아 있다는 걸 확정시켜야 한다.

## 누구한테 보낼 거냐

Map을 직접 순회하니까 범위를 내가 정해야 한다. 세 가지가 됐다.

| | 범위 | 쓰는 데 |
|---|---|---|
| 전체 | 접속자 전원 | 대시보드 카운트 (누가 봐도 같은 값) |
| 세션 | 그 세션의 모든 탭 | 내 알림 |
| 사용자 | 그 사람의 모든 세션·탭 | 내 작업 완료 알림 |

두 번째랑 세 번째를 처음엔 같은 걸로 봤다. 다르다. 같은 사람이 크롬하고 엣지로 각각 로그인하면 세션이 **두 개**다.

세션을 찾는 함수를 이렇게 써놨었다.

```java
for (Map.Entry<String, EmitterWrapper> entry : EMITTERS.entrySet()) {
    if (entry.getValue().getUserSeq() == userSeq) {
        return entry.getValue().getHashKey();   // 첫 번째를 만나면 바로 return
    }
}
```

세션이 둘인데 하나만 돌려준다. 그걸로 보내면 **지금 보고 있는 창이 아닌 쪽으로만** 갈 수 있다. 본인 작업인데 알림이 안 온다. 재로그인해서 옛 연결이 남아 있으면 더 꼬인다.

그래서 사용자 기준은 세션을 거치지 말고 Map 전체를 `userSeq` 로 훑어서 해당하는 연결 전부에 보내게 했다.

## 끊긴 걸 미리 알 방법이 없다

이게 SSE에서 제일 적응 안 됐다. 브라우저가 탭을 닫아도 서버는 모른다. **보내다가 터져야 안다.**

그래서 전송하는 모든 자리가 이 모양이다.

```java
try {
    sseEmitter.send(SseEmitter.event().id(key).name("sse").data(payload));
} catch (Exception e) {
    deleteById(key);   // 보내다 터졌다 = 이미 끊긴 연결
}
```

`catch` 가 에러 처리가 아니라 사실상 연결 정리 담당이다. `onError` 랑 역할이 겹치는데 겹치는 게 맞다. `deleteById` 는 `Map.remove` 라 두 번 불려도 아무 일 안 생긴다.

## 매번 보낼 필요가 없다

데이터가 초 단위로 들어온다. 들어올 때마다 전원에게 보내면 대부분 낭비다. 숫자가 안 바뀌었는데도 보내니까.

직전에 보낸 값을 기억해두고 같으면 생략했다.

```java
public void broadcastIfChanged(String cacheKey, String snapshot, EventPayload payload) {
    if (snapshot != null && snapshot.equals(lastSnapshot.get(cacheKey))) {
        return;                          // 직전과 같다. 안 보낸다
    }
    lastSnapshot.put(cacheKey, snapshot);
    broadcast(payload);
}
```

`snapshot` 은 보낼 데이터를 문자열 하나로 눌러놓은 거다.

```java
counts.stream()
      .map(c -> c.getAreaCode() + "=" + c.getCount())
      .sorted()
      .collect(Collectors.joining(","));
// "A001=3,A002=0,A003=12"
```

`.sorted()` 를 안 넣었다가 한참 헤맸다. 정렬을 안 하면 DB가 돌려주는 순서가 그때그때 달라서 내용이 똑같은데 문자열이 달라진다. 그러면 매번 "바뀌었다"가 되고 게이팅이 통째로 무력화된다. 켜놨는데 안 켜진 상태였다. 로그상으로는 잘 도는 것처럼 보인다.

## 근데 그 최적화가 실시간성을 깨먹었다

제일 오래 붙잡은 버그다.

자산을 등록했는데 화면 숫자가 안 바뀌었다. 코드를 보면 분명히 전송을 호출하고 있다.

```
수집기(초 단위) ──broadcastIfChanged("unknownIp", "A001=3")──▶ 스냅샷 = "A001=3"
                                  ↓
자산 등록 → 미확인 IP가 3 → 2 로 줄어야 한다
                                  ↓
DB를 다시 세서 broadcastIfChanged 호출
                                  ↓
근데 수집기가 방금 "A001=3" 을 넣어놨다 → "같다" → 생략
                                  ↓
화면 그대로
```

게이팅은 "고빈도 트리거에서 값이 안 바뀌면 생략"하려고 만든 건데, 같은 키를 쓰는 저빈도 변경까지 같이 틀어막은 거다.

구분이 필요했다. 수집기는 "**바뀌었을지도 모른다**"라서 확인이 필요하고, 자산 등록은 "**바뀐 게 확실하다**"라서 확인할 이유가 없다. 후자는 게이트를 타면 안 된다.

```java
public void broadcastAndUpdateSnapshot(String cacheKey, String snapshot, EventPayload payload) {
    if (snapshot != null) {
        lastSnapshot.put(cacheKey, snapshot);   // 스냅샷은 갱신하고
    }
    broadcast(payload);                         // 보내는 건 무조건
}
```

스냅샷을 왜 갱신하냐면, 안 하면 다음 수집기 호출이 또 "바뀌었다"고 판단해서 같은 걸 한 번 더 보낸다. 게이팅 정합성을 맞춰놔야 한다.

| | 값이 같을 때 | 스냅샷 | 쓰는 데 |
|---|---|---|---|
| broadcastIfChanged | 생략 | 갱신 | 수집기 (고빈도·불확실) |
| broadcastAndUpdateSnapshot | 그래도 보냄 | 갱신 | 자산 등록/삭제 (저빈도·확정) |

키를 나눠야 하는 것도 같은 함정이다. 집계값이랑 개별값을 한 키로 묶으면 개별 항목 하나가 바뀌어도 집계는 그대로일 수 있어서 개별 변화가 억눌린다. 그래서 `"areaStatus:" + areaCode` 랑 `"unitStatus:" + areaCode` 로 따로 뒀다.

게이팅은 캐시랑 같은 종류의 문제였다. 안 보내도 되는 걸 안 보내는 건 맞는데, **안 보내도 되는지를 판단하는 기준**이 한 군데에만 맞춰져 있으면 다른 경로가 조용히 죽는다.

## 끊긴 동안 놓친 건 안 온다

SSE는 복구되면 그 다음 것부터 온다. 끊겨 있던 사이에 발생한 건 그냥 없어진다.

화면 숫자를 "+1" 식으로 올리고 있었으면 놓친 만큼 영구히 틀어진다.

```
화면 10  ──[끊김]──  서버에서 3건 발생  ──[복구]──  화면 10 / 서버 13
          그 뒤로 1건 더                            화면 11 / 서버 14
                                                     계속 3 차이
```

한 번 틀어지면 스스로 안 맞춰진다. 새로고침해야 맞는다. 사용자는 틀렸다는 것도 모른다.

그래서 재연결이었을 때만 지금 보고 있는 화면의 숫자를 **절대값으로 다시 조회**한다.

```js
eventSource.onopen = function() {
    var wasReconnect = reconnectAttempts > 0;
    reconnectAttempts = 0;
    if (wasReconnect) {
        resyncCounts();     // 증분 말고 현재값을 직접 받아온다
    }
};
```

처음엔 이것도 서버가 전체 전송으로 밀어주려고 했는데 안 된다. 게이트에 걸린다. 서버 입장에서는 값이 안 바뀌었으니까 "보낼 필요 없음"인데, 정작 보정이 필요한 건 방금 재연결한 그 클라다. 전송을 안 타고 그 클라가 직접 조회해야 한다.

증분으로 갱신하는 실시간 화면은 전부 이 문제가 있다. SSE 쓸 거면 "끊김 복구 시 절대값 재조회"를 처음부터 같이 설계해야 한다. 나중에 붙이려면 어디가 증분인지 다 찾아야 한다.

## 재연결이 한꺼번에 몰린다

`EventSource` 는 끊기면 브라우저가 알아서 재연결한다. 근데 간격을 못 고른다. 직접 했다.

```js
const delay = Math.min(1000 * Math.pow(2, reconnectAttempts), 30000);
return delay + Math.random() * 1000;    // 지터
```

1초 → 2 → 4 → 8 ... 30초 상한. 최대 10회까지.

뒤에 붙인 랜덤 1초가 지터다. 이게 없으면 서버 재시작 때 접속자 전원이 동시에 끊기고, 정확히 1초 뒤 **같이** 몰려온다. 막 올라온 서버를 다 같이 때려서 또 죽는다. 흩뿌려야 한다.

상한을 둔 건 무한 재시도로 브라우저가 계속 요청을 만드는 걸 막으려고다.

## tabId가 응답에 그대로 박힌다

`tabId` 는 쿼리 파라미터다. 사용자가 아무거나 넣을 수 있다. 그게 `connectionKey` 가 되고 `connectionKey` 를 이벤트 `id` 로 내보낸다.

```
id: abc123_<여기 들어간다>
event: sse
data: {...}
```

SSE 응답은 줄 단위 프로토콜이다. 빈 줄이 이벤트 경계다. 그러니까 개행을 끼워넣으면 이벤트를 위조할 수 있다. 내가 안 보낸 이벤트를 클라가 받는다.

```java
private static final Pattern TAB_ID_PATTERN = Pattern.compile("^[a-z0-9]{1,16}$");
```

클라가 base36 8자리를 만드니까 영소문자·숫자 16자 이내면 충분하다. 처음엔 개행만 막으려고 했는데 그건 블랙리스트다. 막을 문자를 내가 다 아는 게 아니라서 화이트리스트가 맞다.

연결 수 상한도 뒀다. emitter 하나가 소켓을 붙잡고 있으니까 무제한이면 메모리로 서버가 죽는다.

응답에 반영되는 값은 전부 검증해야 한다는 걸 여기서 체감했다. `id` 는 내부용이라고 생각했는데 **내부용이 아니다**. 클라가 받는 본문이다.

## 이벤트 이름은 하나만 썼다

`name("sse")` 하나로 두고, 보낼 데이터 VO에 필드를 늘리는 식으로 갔다. 클라는 필드가 있는지로 분기한다.

```js
if (data.reportInfo)        { ... }
if (data.dashboardEvent)    { ... }
if (data.clearedAlarmIds)   { ... }
```

이벤트 이름을 종류별로 나누고 `addEventListener` 를 따로 붙이는 방법도 있다. 이름 하나로 간 쪽은 기능 추가가 쉽다. VO에 필드 하나, 클라에 `if` 하나. 대신 VO가 계속 커지고 `if` 가 쌓인다. 클라 파일이 600줄 넘은 게 그 값이다. 다시 하면 이름으로 나눌 것 같다.

---

SSE 자체는 "연결을 끊지 않는 HTTP 응답"이 전부다. 어려운 건 프로토콜이 아니라 그걸 들고 있는 뒤처리였다. 들고 있으니까 지워야 하고, 끊긴 걸 모르니까 보내다가 알게 되고, 놓친 건 안 오니까 따로 맞춰야 한다.
