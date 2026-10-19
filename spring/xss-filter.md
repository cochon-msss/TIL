# XSS 필터 직접 만들기

원래 네이버 루시 필터(`lucy-xss-servlet`)를 썼다. 스프링 버전을 올리니까 못 쓰게 돼서 직접 만들었다. 만들고 나서 우회 결함을 두 번 지적받았다. 그 과정이 라이브러리를 왜 쓰는지에 대한 답이었다.

## 왜 못 쓰게 됐나

버전을 올리면서 의존성이 통째로 바뀌었다.

```
javax.annotation  →  jakarta.annotation
javax.inject      →  jakarta.inject
javax.servlet     →  jakarta.servlet
javax.websocket   →  jakarta.websocket
javax.servlet.jsp →  jakarta.servlet.jsp
```

처음엔 "패키지명만 바뀐 거면 import 고치면 되겠지" 했다. 내 코드는 그게 맞다. 문제는 **라이브러리**다.

루시 필터는 이렇게 생긴 라이브러리다.

```java
public class XssEscapeServletFilter implements javax.servlet.Filter { ... }
```

컴파일된 `.class` 안에 `javax/servlet/Filter` 가 박혀 있다. 톰캣 10부터는 `jakarta.servlet.Filter` 만 로딩하니까 **루시가 구현한 인터페이스가 세상에 없는 인터페이스**가 된다. 소스를 고치는 문제가 아니라 라이브러리가 새로 빌드돼야 하는 문제다.

그래서 이건 루시 하나의 문제가 아니었다. **서블릿 API에 직접 기대는 라이브러리는 전부 같이 끊긴다.** 필터, 인터셉터, 파일 업로드, 인증 라이브러리 전부.

### 왜 패키지명을 바꿨나

이 부분이 황당해서 찾아봤다. 기술적인 이유가 아니었다.

오라클이 Java EE를 이클립스 재단에 넘길 때 **`javax` 라는 상표는 안 넘겼다.** 그래서 이클립스가 이어받은 뒤로는 그 이름을 쓸 수 없고, 전부 `jakarta` 로 바꿔야 했다.

패키지명은 자바에서 타입의 신분증이다. 이름이 바뀌면 다른 타입이다. 그래서 상표권 문제 하나가 **바이너리 호환성을 통째로 깨는 변경**이 됐다. 라이브러리가 새 버전을 내주지 않으면 쓸 방법이 없다.

이름이 코드에 박히는 구조면 이름 변경이 호환성 변경이 된다. 이걸 이때 알았다.

## 루시가 해줬던 것

지우기 전에 설정 파일을 봤다. 75줄이었다.

```xml
<config xmlns="http://www.navercorp.com/lucy-xss-servlet">
    <defenders>
        <defender>
            <name>xssPreventerDefender</name>
            <class>...defender.XssPreventerDefender</class>
        </defender>
    </defenders>

    <default>
        <defender>xssPreventerDefender</defender>
    </default>

    <url-rule-set>
        <url-rule>
            <url>/login.do</url>
            <params>
                <param name="password" useDefender="false" />
            </params>
        </url-rule>
    </url-rule-set>
</config>
```

구조가 세 겹이다.

- `defender` — 어떻게 막을지 (전략)
- `default` — 기본으로 뭘 쓸지
- `url-rule-set` — URL·파라미터별 예외

제일 눈에 들어온 게 `url-rule-set` 이다. **비밀번호 필드는 필터를 끈다.** 비밀번호에 `<` 나 `&` 를 쓰는 사람이 있는데, 그걸 `&lt;` 로 바꿔서 통과시키면 저장된 해시랑 안 맞는다.

이런 예외가 필요하다는 걸 설정으로 뺄 수 있게 만들어둔 거다. 직접 만들 때 이 설계를 못 따라갔다. 나는 경로를 배열에 하드코딩했다.

```java
private static final String[] EXCLUDED_PREFIXES = {
        "/asset/create",
        "/asset/modify",
        ...
};
```

파라미터 단위가 아니라 **URL 단위 전체 제외**다. 즉 그 화면의 모든 필드가 검사에서 빠진다. 루시는 "이 URL의 이 파라미터만" 이었는데 내 건 "이 URL 전부"다. 거칠다.

## 치환이냐 차단이냐

루시의 기본 `XssPreventerDefender` 는 **값을 바꿔서 통과시킨다.**

```
입력:  <script>alert(1)</script>
통과:  &lt;script&gt;alert(1)&lt;/script&gt;
```

나는 **차단**으로 갔다.

```java
if (SUSPICIOUS_PATTERN.matcher(body).find()) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST, "XSS risk detected");
    return;
}
```

| | 치환 | 차단 |
|---|---|---|
| 위험한 입력 | 바꿔서 저장 | 400으로 거부 |
| 정상 입력이 걸리면 | 값이 깨진 채 저장됨 | 저장 자체가 안 됨 |
| 사용자가 아는가 | 모른다 | 바로 안다 |
| DB에 들어가는 값 | 인코딩된 문자열 | 원본 |

차단으로 간 이유는 치환이 **조용히 값을 바꾼다**는 게 싫어서였다. 사용자는 저장됐다고 생각하는데 내용이 달라져 있다. 나중에 왜 이렇게 저장됐냐는 문의가 오면 추적이 어렵다.

대신 차단은 **정상 입력을 막는다**. 이 대가를 나중에 치렀다.

## 본문을 읽으면 컨트롤러가 못 읽는다

필터를 만들자마자 터진 문제다. 본문을 검사하려고 읽었더니 컨트롤러에서 요청 본문이 빈 값으로 왔다.

`request.getInputStream()` 은 **한 번만 읽을 수 있는 스트림**이다. 파일이 아니라 네트워크에서 흘러오는 바이트라 되감기가 없다. 필터가 다 읽어버리면 뒤에서는 읽을 게 없다.

```
[필터] getInputStream() → 끝까지 읽음
[컨트롤러] getInputStream() → 빈 값
```

해결은 읽은 걸 들고 있다가 다시 내주는 거다. 서블릿에 그걸 위한 상속 지점이 있다.

```java
public class CachedBodyHttpServletRequest extends HttpServletRequestWrapper {

    private final byte[] cachedBody;

    public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
        super(request);
        this.cachedBody = request.getInputStream().readAllBytes();   // 한 번 다 읽어서 보관
    }

    @Override
    public ServletInputStream getInputStream() {
        ByteArrayInputStream bais = new ByteArrayInputStream(this.cachedBody);
        return new ServletInputStream() {
            @Override public int read() throws IOException { return bais.read(); }
            @Override public boolean isFinished() { return bais.available() == 0; }
            @Override public boolean isReady() { return true; }
            @Override public void setReadListener(ReadListener l) { }
        };
    }
}
```

`getReader()` 도 같이 재정의해야 한다. 컨트롤러가 둘 중 뭘 쓸지 모른다.

그리고 **래퍼를 체인에 넘겨야** 의미가 있다.

```java
chain.doFilter(wrappedRequest, res);   // req 가 아니라 wrappedRequest
```

여기서 원래 `req` 를 넘기면 래퍼를 만든 게 아무 의미가 없다. 한 글자 차이다.

바이트를 그대로 들고 있으니까 본문이 크면 그만큼 메모리를 쓴다. 처음엔 100KB 상한을 두고 넘으면 검사를 생략했는데, 생략은 곧 우회라서 지금은 상한 없이 다 읽는다. 대신 업로드 경로를 제외 목록에 넣었다.

## 정화한 결과로 검사하고 원본을 넘기면 검사가 무의미하다

이게 제일 큰 배움이었다.

처음 구현은 2단계였다. 정규식으로 1차 탐지하고, Jsoup으로 HTML을 정화해서 2차로 확인했다.

```java
String cleaned = Jsoup.clean(body, Safelist.none());
if (SUSPICIOUS_PATTERN.matcher(cleaned).find()) {    // 정화된 걸 검사
    // 거부
}
chain.doFilter(wrappedRequest, res);                  // 원본을 넘김
```

"이중으로 검사하니까 더 안전하겠지" 했다. 반대였다.

`Jsoup.clean(..., Safelist.none())` 은 **모든 태그를 지운다.** 그러니까 정화된 결과에는 당연히 위험한 패턴이 없다. 검사를 항상 통과한다.

```
원본:      <script>alert(1)</script>
Jsoup:     (태그 제거)  →  ""
2차 검사:  ""  →  깨끗하다  →  통과
컨트롤러:  <script>alert(1)</script>      ← 원본이 그대로 간다
```

**정화한 사본으로 검사하고 원본을 흘려보낸 거다.** 2단계를 추가해서 더 안전해진 게 아니라, 통과 판정을 받기 쉬운 경로를 하나 만든 거였다.

고치는 방법은 둘이었다.

1. 정화한 결과를 **컨트롤러에 넘긴다** (치환 방식)
2. 정화를 **아예 안 하고** 원본이 패턴에 걸리면 거부한다 (차단 방식)

차단으로 가기로 했으니 2번이다. Jsoup을 걷어냈다.

```java
// 정규식 매치만으로 즉시 400 반환
if (SUSPICIOUS_PATTERN.matcher(body).find()) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST, "XSS risk detected");
    return;
}
```

검사한 값과 통과시킬 값이 다르면 검사가 아니다. 당연한 말인데 코드로는 자연스럽게 틀릴 수 있었다. 정화 함수가 있으면 그걸 검사에 쓰고 싶어진다.

## Content-Type이 없으면 통째로 빠져나갔다

보안 점검에서 지적받은 결함이다.

본문 검사를 할 수 있는 요청인지 Content-Type으로 판단했다.

```java
if (contentType == null ||
    !(contentType.contains("application/json")
        || contentType.contains("application/x-www-form-urlencoded")
        || ...)) {
    chain.doFilter(req, res);    // 검사 없이 통과
    return;
}
```

본문 검사만 생각하고 쓴 코드다. 그런데 **GET 요청은 Content-Type이 없다.** 그러니까 GET은 전부 이 `return` 으로 빠져나갔다.

```
GET /search?keyword=<script>alert(1)</script>
    → Content-Type 없음 → 검사 없이 통과
```

아래에 쿼리 파라미터 검사 로직이 있었는데도 거기까지 도달하지 못했다. **검사 코드가 있는데 안 실행되는 상태**였다.

고친 건 검사를 조건 양쪽에 두는 거다.

```java
boolean bodyCheckable = contentType != null && (...);

if (!bodyCheckable) {
    // 본문 검사 대상이 아니어도 쿼리 파라미터는 검사한다
    if (hasSuspiciousParameter(request)) {
        response.sendError(SC_BAD_REQUEST, "XSS risk detected");
        return;
    }
    chain.doFilter(req, res);
    return;
}
```

`if (조건 아님) { 통과; return; }` 이 패턴이 위험하다. "이 경우는 내 관심사가 아니다"로 썼는데 실제 의미는 "이 경우는 **아무 검사도 안 한다**"였다. 필터에서 early return 은 곧 우회 경로다.

## 블랙리스트는 계속 늘어난다

처음 패턴은 네 개였다.

```java
Pattern.compile("<script|<img|on\\w+\\s*=|javascript:", CASE_INSENSITIVE);
```

지금은 이렇다.

```java
Pattern.compile("<script|<img|<iframe|<frame|<object|<embed|<svg|<base|<meta|<link|<form"
        + "|on\\w+\\s*=|javascript:|vbscript:|data:text/html", CASE_INSENSITIVE);
```

점검에서 프레임 인젝션이 걸려서 늘렸다. `<iframe>` 으로 외부 페이지를 끼워넣는 건 `<script>` 가 없어도 된다. `<svg onload=...>`, `<object data=...>`, `<base href=...>` 도 각자 다른 방법으로 같은 걸 한다.

늘릴 때마다 느낀 건 **이 목록이 끝나지 않는다**는 거다. 내가 아는 태그까지만 막을 수 있다.

[SSE 노트](sse.md)에서 `tabId` 는 화이트리스트로 막았다. 거기선 되는데 여기선 안 된다. 차이가 뭔지 생각해봤다.

| | tabId | 사용자 입력 전체 |
|---|---|---|
| 들어올 값을 아는가 | 안다 (내가 만든 base36 8자리) | 모른다 (한글·특수문자·설명문) |
| 허용 집합을 쓸 수 있나 | `^[a-z0-9]{1,16}$` | 못 쓴다 |
| 그래서 | 화이트리스트 | 블랙리스트밖에 없다 |

**허용할 걸 다 적을 수 있으면 화이트리스트, 못 적으면 블랙리스트가 된다.** 블랙리스트가 나쁜 선택이라서 쓰는 게 아니라 다른 방법이 없어서 쓴다. 그리고 블랙리스트를 쓴다면 그게 최후 방어선이면 안 된다.

[파일 업로드 검증](../security/file-upload.md)에서 같은 갈림길을 또 만났다. 거기선 화이트리스트를 쓸 수 있었는데도 느슨해지는 자리가 나왔다.

## 전부 막으면 못 쓰는 화면이 생긴다

차단 방식의 대가가 왔다. 자산 등록 화면에서 저장이 안 된다는 얘기가 나왔다.

자산 이름이나 설명에 `<` 가 들어갈 수 있다. 등록 양식 규격이 **길이만 제한하고 문자는 다 허용**이다. 그런데 필터가 400을 뱉는다.

그래서 그 경로를 제외했다.

```java
private static final String[] EXCLUDED_PREFIXES = {
        "/asset/create",
        "/asset/modify",
        ...
};
```

제외했으면 그 입력은 다른 데서 막아야 한다. 두 군데로 나눴다.

**저장할 때 인코딩**

```java
public static <T> T encodeObject(T obj, Set<String> skipFields) {
    Class<?> clazz = obj.getClass();
    while (clazz != null) {
        for (Field field : clazz.getDeclaredFields()) {
            if (field.getType() != String.class) continue;
            if (skipFields != null && skipFields.contains(field.getName())) continue;
            field.setAccessible(true);
            String value = (String) field.get(obj);
            if (value != null && !value.isEmpty()) {
                field.set(obj, HtmlUtils.htmlEscape(value));
            }
        }
        clazz = clazz.getSuperclass();   // 부모 클래스 필드까지
    }
    return obj;
}
```

리플렉션으로 VO의 모든 `String` 필드를 훑어서 인코딩한다. 필드를 하나하나 적으면 새 필드가 추가될 때 빼먹으니까 전부 돌린다.

`skipFields` 가 필요한 이유는 **인코딩하면 깨지는 필드**가 있어서다. JSON 문자열이나 파일 경로를 인코딩하면 `"` 가 `&quot;` 가 돼서 파싱이 깨진다. 루시의 `useDefender="false"` 랑 같은 역할인데, 설정이 아니라 호출할 때 넘기는 집합이다.

**조회할 때 디코딩**

저장할 때 인코딩했으니 읽을 때 원복해야 한다. `decodeObject` / `decodeList` 가 그걸 한다.

이 방식은 솔직히 마음에 안 든다. 문제가 몇 개 있다.

- **이중 인코딩**. 디코딩을 빼먹고 다시 저장하면 `&amp;lt;` 가 된다. 한 번 꼬이면 몇 번 인코딩됐는지 알 수 없다.
- **길이가 늘어난다**. `<` 한 글자가 `&lt;` 네 글자다. DB 컬럼 길이를 넘길 수 있다.
- **검색이 안 된다**. DB에 `&lt;` 로 들어가 있으니 `<` 로 LIKE 검색하면 안 걸린다.
- **저장소가 표현 형식에 오염된다**. DB는 HTML이 아닌데 HTML 엔티티가 들어있다.

제대로 하려면 **DB에는 원본을 넣고 출력할 때 이스케이프**하는 게 맞다. 화면에서 `c:out` 이나 `escapeHtml` 로 처리하는 거다. 실제로 출력 쪽에도 이걸 걸어뒀는데, 그러면 저장 인코딩은 사실 중복이다.

지금 구조가 이렇게 된 건 특수문자 저장 오류를 급하게 막다가 저장 쪽에 붙였기 때문이다. 다시 하면 저장은 원본으로 두고 출력에만 걸 것 같다.

## 결국 XSS는 출력 문제다

필터를 만들면서 계속 입력을 막으려고 했는데, 방향이 반쯤 틀렸다.

XSS가 터지는 건 값이 **HTML로 해석될 때**다. 입력일 때는 그냥 문자열이다. `<script>` 라는 글자가 DB에 들어있는 것 자체는 아무 일도 안 한다. 그걸 페이지에 그대로 박아서 브라우저가 태그로 읽을 때 터진다.

```
입력 ──▶ 저장 ──▶ 출력 ──▶ 브라우저가 HTML로 해석   ← 여기서 터진다
```

그러니까 근본 대책은 **출력할 때 이스케이프**다. 입력 필터는 보조다.

입력 필터만으로 안 되는 이유도 분명하다.

- 필터를 안 타는 경로가 생긴다 (배치, 외부 연동, 다른 시스템이 쓴 데이터)
- 이미 DB에 들어있는 과거 데이터는 필터를 거치지 않았다
- 블랙리스트는 내가 아는 것까지만 막는다

출력 이스케이프는 반대다. **값이 뭐든 태그로 해석되지 않게** 만든다. 막을 패턴을 알 필요가 없다.

그래도 입력 필터를 둔 이유는 있다. 출력 지점은 수백 군데고 그중 하나를 빼먹으면 터진다. 입력은 한 군데다. 겹쳐 두면 한쪽이 뚫려도 다른 쪽이 남는다.

---

라이브러리를 직접 만들어 보니 라이브러리가 왜 그렇게 생겼는지 알게 됐다. 루시의 `url-rule-set` 은 과한 설정이 아니라 "예외는 반드시 생긴다"를 알고 만든 구조였고, 내가 하드코딩 배열로 시작해서 똑같은 자리에 도달했다. 그리고 내가 두 번 지적받은 우회(정화한 사본으로 검사, Content-Type 없을 때 early return)는 **막는 로직을 잘못 쓴 게 아니라 안 타는 길을 만든 것**이었다. 검사기는 뭘 잡느냐보다 **어디로 빠져나갈 수 있느냐**가 먼저다.
