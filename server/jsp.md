# JSP (Java Server Page)

HTML을 중심으로 자바와 연동하여 사용하는 웹 언어이다. HTML 코드 안에 자바 코드를 작성할 수 있다.

## 웹 동작 구조

- **서버(server)**: 사용자의 요청에 맞는 서비스를 제공해 주는 것
- **요청(request)**: 클라이언트 → 서버
- **응답(response)**: 서버 → 클라이언트
- **웹(Web)**: 페이지 요청과 응답이 일어나는 장소. 인터넷에 연결된 컴퓨터들을 통해 사람들이 정보를 공유하는 공간

### 웹 서버 (아파치)

사용자의 요청이 정적 데이터인지 동적 데이터인지 판단한다.

- 정적 데이터일 경우: 이미 준비된 HTML 문서를 그대로 응답한다.
- 동적 데이터일 경우: 웹 컨테이너에 요청을 보낸다.

### 웹 컨테이너 (서블릿 컨테이너)

동적 데이터일 경우 JSP·서블릿으로 연산 및 제어, DB에 접근해서 정제된 데이터(정적 데이터)가 완성되면 이를 응답한다.

### WAS (Web Application Server) - 톰캣

동적 데이터를 처리할 서블릿을 메모리에 할당하며, `web.xml`을 참조하여 해당 서블릿에 대한 Thread를 생성한다. 서블릿 요청과 서블릿 응답 객체 생성 후 서블릿에 전달하면, 연산 종료 후 메모리에서 해제시킨다.

### 서블릿

자바 코드 안에 HTML 코드를 작성할 수 있는 자바 프로그램이다.

- 쓰레드에 의해 서블릿의 `service()` 메서드가 호출된다.
- 전송 방식 요청에 맞게 `doGet()` 또는 `doPost()` 메서드를 호출한다.
- WAS는 Response 객체를 HttpResponse 형태(정적 데이터)로 바꾸어 웹 서버에 전달하고 생성된 Thread를 종료시킨다. 그리고 HttpServletRequest와 HttpServletResponse 객체를 제거한다.

정리하면 요청이 오면:

1. WAS는 Request, Response 객체를 새로 만들어 서블릿 객체를 **호출**
2. 개발자는 Request 객체에서 HTTP 요청 정보를 편리하게 꺼내서 **사용**
3. 개발자는 Response 객체에 HTTP 응답 정보를 편리하게 **입력**
4. WAS는 Response 객체에 담긴 내용으로 HTTP 응답 정보를 생성

## 디렉티브(지시어) 태그

JSP 컨테이너에게 해당 페이지를 어떻게 처리해야 하는지 전달하기 위한 태그. 기본 형식은 `<%@ directive attribute="value" %>`이다.

### page

현재 페이지에 대한 정보를 설정하는 태그로, 되도록 페이지 최상단에 선언한다.

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" import="java.util.*" errorPage="error.jsp" %>
```

- **language**: 현재 JSP 페이지가 사용할 프로그래밍 언어 (기본 java)
- **contentType**: 현재 JSP 페이지가 생성할 문서의 콘텐츠 유형. 클라이언트 응답 시 전달하는 HTTP 헤더 정보가 된다.
- **pageEncoding**: JSP 파일을 컨테이너가 처리할 때 사용하는 문자 인코딩. 올바른 한글 처리를 위해 UTF-8로 지정
- **import**: JSP 파일 내에서 자바 코드를 직접 사용하는 경우 필요한 패키지/클래스 import
- **session**: 세션 사용 여부 설정
- **info**: 현재 JSP 페이지에 대한 설명 설정
- **errorPage**: 오류 발생 시 보여줄 오류 페이지 설정. 매 페이지에 넣기보다 서버 설정을 사용하는 것이 권장된다.
- **isErrorPage**: 현재 페이지가 오류 페이지인지 여부 설정

### include

```jsp
<%@ include file="header.jsp" %>
<%@ include file="body.jsp" %>
<%@ include file="footer.html" %>
```

다른 파일(html, jsp)을 포함하기 위한 지시어로, include 지시어가 사용된 위치에 해당 파일을 불러온다. 컨테이너는 포함된 파일들을 하나로 처리하며 자바 소스를 생성한 뒤 서블릿으로 컴파일한다. 따라서 포함되는 파일이 단독 실행되지 않는다면 개별 구성요소(page 지시어, html 기본 태그 등)를 갖출 필요가 없다.

보통 header와 footer는 대부분의 페이지에서 동일하게 작성되기 때문에, 유지보수 및 편의를 위해 외부 파일로 만든 후 include해서 사용한다. 이러한 것을 **모듈화**라고 한다.

### taglib

커스텀 태그 라이브러리를 선언하는 지시어.

## 스크립트 태그

HTML 코드에 자바 코드를 넣어 프로그램 기능을 구현할 수 있다.

1. **선언문(declaration)** `<%! %>`: 자바 변수나 메서드를 정의하는 데 사용
2. **스크립틀릿(scriptlet)** `<% %>`: 자바 변수 및 자바 로직 코드를 작성하는 데 사용
3. **표현문(expression)** `<%= %>`: 변수, 계산식, 리턴이 있는 메서드 호출 결과를 문자열 형태로 출력

## 액션 태그

서버나 클라이언트에게 어떤 행동을 하도록 명령하는 태그. 페이지 사이를 제어하거나 다른 페이지의 실행 결과를 현재 페이지에 포함시킬 때 사용한다. 자바빈즈와 같은 다양한 기능을 제공하며, XML 형식의 `<jsp:.../>`를 사용한다.

1. **forward** `<jsp:forward />`: 다른 페이지로 이동, 페이지 흐름 제어
2. **include** `<jsp:include page="" />`: 외부 페이지 내용 포함 또는 페이지 모듈화
3. **param** `<jsp:param />`: 현재 페이지에서 다른 페이지로 정보 전달

## 자바빈즈 (액션 태그)

JSP가 표준 태그를 통해 접근할 수 있는 자바 클래스로, 멤버 변수와 setter/getter 메서드로 이루어져 있다.

```jsp
<%-- 객체 생성 --%>
<jsp:useBean class="com.koreait.beans.MemberVO" id="member" />

<%-- setter --%>
<jsp:setProperty property="name" name="member" value="한동석" />

<%-- getter --%>
<jsp:getProperty property="name" name="member" />
```

**자바빈즈 규칙**

1. 패키지화
2. 필드 접근자를 private으로 설정
3. getter, setter 메서드는 public으로 설정
4. 기본 생성자 선언

## JSP 개요 (보충)

JSP는 서블릿의 화면 처리 어려움을 해결하기 위해 나왔으며, HTML과 데이터를 조합하기 위해 다음과 같은 기능적 특징을 가진다.

- HTML 페이지에 자바 코드를 직접 사용
- 서블릿 컨테이너에 의해 관리되는 내장 객체들의 라이프사이클을 이용한 페이지 간 상태 관리
- 커스텀 태그 기술을 사용한 코드의 태그화 (action, JSTL 등)
- EL(Expression Language)을 통한 데이터 표현

### 장점

- HTML 파일에 자바 기술을 거의 무한대로 사용할 수 있다.
- 비교적 쉽게 개발이 가능하다.
- 커스텀 태그 라이브러리 등 확장 태그 구조를 사용할 수 있다.
- 서블릿으로 변환되어 실행되므로 서블릿 기술의 장점을 모두 가진다.
- MVC 패턴, 스프링 프레임워크 등 잘 설계된 구조를 적용할 수 있어 체계가 잡히면 생산성과 성능이 향상된다.
- 모든 개발이 서버에서 이루어지므로 개발의 집중화를 통한 효율이 있다.

### 단점

- 화면 구성요소의 변경은 JSP → java → class → 서블릿 실행의 과정을 거치므로, 사소한 UI 변경도 매번 확인하는 데 시간이 소요된다.
- 개발자와 디자이너 간의 역할 분담에 제약이 있다.
- JSP 파일의 화면 디자인 확인을 위해서도 반드시 서블릿 컨테이너의 실행이 필요하다.

전반적으로 JSP 자체의 단점이라기보다는 SSR(Server Side Rendering) 방식 백엔드 웹 개발의 문제라 볼 수 있다.

## 자주 쓰는 처리

### 글자 깨짐

```java
response.setCharacterEncoding("UTF-8");             // 내가 이 인코딩으로 보낸다
response.setContentType("text/html; charset=UTF-8"); // 이 인코딩으로 읽어라, html 문서다
```

### QueryString

```
http://localhost/hello?cnt=3
```

`?` 뒤에 조건(파라미터)을 붙여 전달한다.

## JSP 내장 객체

### request

| 메서드 | 설명 |
|---|---|
| getParameterNames() | 사용자가 전달한 키들을 Enumeration 객체로 반환 |
| getParameter(name) | 사용자가 전달한 name과 일치하는 값을 반환 |
| getParameterValues(name) | 전달한 name과 일치하는 값을 배열 형식으로 반환 |
| getCookies() | 전달한 쿠키를 배열 형식으로 반환 |
| getMethod() | 요청 방식이 GET인지 POST인지 문자열로 반환 |
| getSession() | 세션 객체를 반환 |
| getRemoteAddr() | IP 주소를 반환 |
| getProtocol() | 서버의 프로토콜을 문자열로 반환 |
| setCharacterEncoding() | JSP로 전달되는 내용을 지정한 문자셋으로 변환 |
| getHeaderNames() | 현재 요청이 가지는 헤더의 이름들을 반환 |
| getHeaders(name) | 요청한 헤더에서 지정한 이름의 모든 값을 반환 |
| getQueryString() | 요청에 포함된 쿼리 문자열을 반환 |

### response

| 메서드 | 설명 |
|---|---|
| setContentType(type) | 콘텐트 형식을 설정 |
| setHeader(name, value) | 클라이언트에게 헤더로 전달할 값을 설정 |
| setDateHeader(name, date) | 클라이언트에게 헤더로 전달할 날짜를 설정 |
| sendError(status, msg) | 클라이언트에게 에러 코드와 메시지를 전달 |
| sendRedirect(url) | 클라이언트 요청을 다른 페이지로 전달 |
| addCookie(cookie) | 클라이언트에게 전달할 쿠키를 설정 |
| encodeURL(url) | URL로 유효하지 않은 문자를 인코딩 |
| setStatus(sc) | 상태 코드를 설정 |

### out

`out`은 되도록 쓰지 않는 것이 바람직하나 참고용으로 정리한다.

| 메서드 | 설명 |
|---|---|
| getBufferSize() | output buffer의 크기를 byte로 반환 |
| getRemaining() | 버퍼 크기 중 사용 가능한 비율을 반환 |
| clearBuffer() | 버퍼에 있는 콘텐츠를 모두 비운다 |
| flush() | 버퍼를 비우고 output stream도 비운다 |
| close() | output stream을 닫고 버퍼를 비운다 |
| println(content) | content를 newline과 함께 출력 |
| print(content) | content를 출력 |
