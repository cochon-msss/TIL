# 파일 업로드 검증

첨부 파일을 받는 화면이 여러 개 있어서 검증 유틸을 만들었다. 처음엔 "확장자 목록만 확인하면 되지" 싶었는데 그게 제일 약한 검사였다.

## 확장자는 그냥 파일명이다

확장자는 파일 안에 적혀 있는 게 아니다. **이름 뒤에 붙은 글자**다. 그러니까 바꾸면 된다.

```
evil.jsp  →  evil.jpg  로 이름만 바꿔서 업로드
```

확장자 검사는 통과한다. 서버가 그 파일을 웹 경로에 저장하고, 나중에 누가 `.jsp` 로 다시 접근할 길이 있으면 그게 실행된다.

그래서 검사가 두 층이어야 했다.

1. 이름에 붙은 확장자가 허용 목록에 있나
2. **파일 내용이 그 확장자랑 맞나**

2번이 본질이고 1번은 싼 1차 거름망이다. 순서는 1번이 먼저인데, 내용을 읽는 건 비싸니까 이름으로 걸러낼 수 있는 건 먼저 떨어뜨린다.

## 화이트리스트를 짰는데 블랙리스트도 남겼다

[XSS 필터](../spring/xss-filter.md) 때 "허용할 걸 다 적을 수 있으면 화이트리스트"라고 적었다. 파일 확장자는 적을 수 있다. 그래서 화이트리스트로 갔다.

```java
private static final Set<String> ALLOWED_EXTENSIONS = Set.of(
        "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "hwp", "hwpx",
        "jpg", "jpeg", "png",
        "zip", "tar", "gz"
);
```

그런데 위험한 확장자 목록도 같이 뒀다.

```java
private static final Set<String> DANGEROUS_EXTENSIONS = Set.of(
        "exe", "bat", "cmd", "sh", "ps1", "vbs", "js", "jar", "war",
        "jsp", "jspx", "php", "asp", "aspx", "cgi", "pl", "py", "rb",
        "msi", "dll", "com", "scr", "pif", "hta", "wsf", "wsh"
);
```

검사 순서는 블랙리스트가 먼저다.

```java
// 3. 위험한 확장자 (블랙리스트)
if (DANGEROUS_EXTENSIONS.contains(extension)) {
    LOGGER.warn("Dangerous file extension upload attempt: {}", extension);
    return fail(...);
}

// 4. 화이트리스트
if (!allowedExtensions.contains(extension)) {
    LOGGER.warn("Disallowed extension upload attempt: {}", extension);
    return fail(...);
}
```

처음엔 이게 중복이라고 생각했다. 화이트리스트에 `jsp` 가 없으니 4번에서 어차피 걸린다. 3번은 왜 있나.

**로그가 다르다.** 그리고 그게 의도였다.

| | 뜻 | 로그 |
|---|---|---|
| 블랙리스트에 걸림 | `jsp`, `exe` 를 올렸다 | 공격 시도일 가능성 |
| 화이트리스트에만 걸림 | `gif`, `svg` 를 올렸다 | 그냥 안 되는 걸 몰랐다 |

둘 다 "거부"지만 성격이 다르다. 한 줄로 합치면 **로그에서 구분이 안 된다.** `gif` 올리려는 사람 수백 명 사이에 `jsp` 한 건이 섞여 있으면 못 찾는다.

거부 사유를 같은 수준으로 묶지 않는 게 포인트였다. 거부는 결과가 같아도 **왜 거부됐는지가 운영에서는 다른 정보**다.

그리고 화이트리스트를 쓸 수 없는 자리도 있었다. 아무 파일이나 첨부할 수 있어야 하는 게시판 같은 데는 블랙리스트만 쓰는 별도 메서드를 뒀다. 좋은 선택은 아닌데 요구사항이 그랬다.

## 내용을 보려면 Tika

내용 검증은 Apache Tika로 했다. 바이트를 보고 MIME 타입을 추정해준다.

```java
try (InputStream is = file.getInputStream()) {
    String detectedMimeType = TIKA.detect(is);
    return expectedMimeTypes.contains(detectedMimeType);
}
```

확장자별로 기대하는 MIME 집합을 매핑해뒀다.

```java
EXTENSION_MIME_MAP.put("pdf",  Set.of("application/pdf"));
EXTENSION_MIME_MAP.put("png",  Set.of("image/png"));
EXTENSION_MIME_MAP.put("docx", Set.of("application/vnd.openxmlformats-officedocument.wordprocessingml.document"));
```

`Set` 인 게 중요하다. 하나로 끝나는 확장자가 생각보다 적었다.

## zip 기반 포맷은 서로 구분이 안 된다

여기서 제일 오래 막혔다. `.xlsx` 를 올렸는데 검증이 실패했다.

**xlsx 는 zip 이다.** OOXML 이라는 포맷인데 실체는 XML 파일 여러 개를 zip으로 묶은 거다. 확장자만 바꿔서 압축 해제 프로그램으로 열어보면 안에 파일들이 보인다. docx, pptx도 같다.

그래서 Tika가 **내용만 보고는 xlsx인지 그냥 zip인지 확신을 못 한다.** 상황에 따라 `x-tika-ooxml` 이나 `application/zip` 으로 떨어진다.

```java
EXTENSION_MIME_MAP.put("xlsx", Set.of(
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/x-tika-ooxml",
        "application/zip"          // ← 이걸 넣어야 동작한다
));
```

hwpx도 같은 구조다. ODF처럼 OCF(zip) 컨테이너다. 이건 직접 올려보면서 확인했다.

```
mimetype 항목이 있으면   → application/hwp+zip
mimetype 항목이 없으면   → application/zip
```

같은 hwpx인데 안에 `mimetype` 이라는 항목이 들어 있냐 없냐로 결과가 갈린다. 저장한 프로그램에 따라 다르다. 그래서 둘 다 받아야 했다.

### 이게 뜻하는 것

허용 목록에 `application/zip` 을 넣는 순간 **xlsx 자리에 아무 zip이나 올려도 통과한다.** 내용 검증이 그 확장자에서는 사실상 꺼진다.

주석에 "zip 은 이미 화이트리스트에 있어 느슨해지는 것도 없다"고 적어뒀다. `zip` 자체를 허용하고 있으니 공격자가 굳이 xlsx로 위장할 이유가 없다는 뜻이다. 맞는 얘기지만, **그 타협이 성립하는 이유가 "zip을 이미 허용했기 때문"**이라는 게 중요하다. zip을 허용 목록에서 빼면 이 매핑이 구멍이 된다.

구형 Office도 같은 문제다. doc·xls·ppt는 **OLE 컴파운드 문서**라는 공통 컨테이너를 쓴다.

```java
EXTENSION_MIME_MAP.put("doc", Set.of("application/msword",        "application/x-tika-msoffice"));
EXTENSION_MIME_MAP.put("xls", Set.of("application/vnd.ms-excel",  "application/x-tika-msoffice"));
EXTENSION_MIME_MAP.put("ppt", Set.of("application/vnd.ms-powerpoint", "application/x-tika-msoffice"));
```

`x-tika-msoffice` 가 셋에 다 들어 있다. 즉 **doc 자리에 xls를 올려도 통과한다.** 셋 다 허용 목록에 있으니 실질 위험은 없지만, "확장자와 내용이 일치한다"는 검사가 여기서는 "같은 컨테이너 계열이다" 수준으로 약해진다.

컨테이너 포맷은 겉이 같다. 내용 검증은 **겉까지만** 본다. 더 확실히 하려면 zip을 열어서 안에 뭐가 있는지 봐야 하는데 거기까지는 안 갔다.

## 매핑이 없는 확장자는 검증을 건너뛴다

이걸 쓰고 나서 발견했다.

```java
private static boolean validateMimeType(MultipartFile file, String extension) throws IOException {
    Set<String> expectedMimeTypes = EXTENSION_MIME_MAP.get(extension);
    if (expectedMimeTypes == null) {
        // 매핑이 없는 확장자는 추가 검증 없이 통과 (화이트리스트에 있으므로)
        return true;
    }
    ...
}
```

`tar`, `gz` 는 매핑을 안 만들었다. 그러니까 **내용 검증을 안 탄다.** 확장자만 맞으면 통과다.

근거는 "화이트리스트에 있으므로"다. 이상한 논리는 아니다 — 허용한 확장자니까. 그런데 그러면 내용 검증을 하는 이유 자체가 흔들린다. 내용 검증은 "**허용된 확장자로 위장한 다른 파일**"을 잡는 거였다. 매핑을 빼먹으면 그 확장자가 위장 통로가 된다.

허용 목록에 확장자를 추가할 때 매핑도 같이 추가해야 하는데, 코드가 그걸 강제하지 않는다. 지금은 `null` 이면 조용히 통과다. **검증을 생략하는 분기는 소리를 내야 한다**는 걸 [XSS 필터](../spring/xss-filter.md)에서도 똑같이 느꼈는데 여기서 또 했다.

## Path Traversal 은 패턴 열거보다 불변식이 강했다

파일명에 경로가 들어오면 엉뚱한 데 저장된다.

```
../../../../etc/passwd
..\..\windows\system32\evil.jsp
```

처음엔 이런 패턴을 적어서 막았다.

```java
String normalized = filename.replace("\\", "/");
if (normalized.contains("../") || normalized.contains("..\\") ||
        normalized.startsWith("/") || normalized.startsWith("\\") ||
        normalized.contains(":")) {
    return false;
}
```

`:` 를 막는 건 윈도 때문이다. `C:` 같은 드라이브 지정이랑 `file.txt:hidden` 같은 대체 데이터 스트림(ADS)이 둘 다 `:` 를 쓴다.

널 바이트도 막았다.

```java
if (filename.contains("\0")) {
    return false;
}
```

`evil.jsp\0.jpg` 같은 걸 넣으면, 자바는 끝까지 읽어서 `.jpg` 로 보는데 밑단의 C 계열 라이브러리는 `\0` 에서 문자열이 끝났다고 보고 `evil.jsp` 로 처리할 수 있다. 같은 문자열을 두 층이 다르게 읽는 거다.

그런데 이것도 블랙리스트다. 인코딩을 섞으면(`%2e%2e%2f`, 유니코드 변형) 빠져나갈 수 있다. 그래서 마지막에 조건을 하나 더 뒀는데 이게 제일 강했다.

```java
// 파일명만 추출하여 원본과 비교
String baseName = FilenameUtils.getName(filename);
if (!baseName.equals(filename)) {
    return false;
}
```

**"파일명에서 경로를 떼어낸 결과가 원본과 같아야 한다."**

경로 요소가 조금이라도 있으면 떼어낸 결과가 달라지니까 거부된다. 어떤 모양으로 들어왔는지 알 필요가 없다. 위험한 패턴을 열거하는 게 아니라 **"이건 순수한 파일명이다"라는 불변식을 확인**하는 거다.

XSS 필터에서는 블랙리스트밖에 답이 없었는데, 여기서는 불변식을 쓸 수 있었다. 차이는 **원하는 값의 조건을 한 문장으로 적을 수 있느냐**였다. "파일명은 경로를 포함하지 않는다"는 적을 수 있다. "사용자 설명문은 ..."은 적을 수 없다.

막을 걸 세는 대신 지켜야 할 조건을 쓸 수 있으면 그게 훨씬 짧고 강하다. 위의 패턴 열거는 지금 보면 거의 필요 없다. 진단 로그를 더 자세히 남기는 값 정도다.

저장할 때 쓸 파일명은 따로 정규화했다.

```java
String sanitized = baseName.replaceAll("[^가-힣a-zA-Z0-9_\\-]", "_");
sanitized = sanitized.replaceAll("_{2,}", "_");      // 연속 언더스코어 정리
sanitized = sanitized.replaceAll("^_+|_+$", "");     // 앞뒤 제거
if (sanitized.isEmpty()) sanitized = "file";         // 다 날아간 경우
```

여긴 허용할 문자를 적었으니 화이트리스트다. 한글은 남겨야 해서 넣었다. `sanitized.isEmpty()` 처리가 필요한 이유는 파일명이 전부 특수문자면 결과가 빈 문자열이 되기 때문이다. 확장자만 남은 `.pdf` 같은 게 저장된다.

## SVG 는 이미지가 아니라 실행 가능한 문서다

이미지 허용 목록을 보면 세 개뿐이다.

```java
private static final Set<String> ALLOWED_IMAGE_EXTENSIONS = Set.of("jpg", "jpeg", "png");
// gif, bmp, svg, webp, ico 제외
```

`svg` 를 뺀 이유는 **SVG가 XML이고, 그 안에 스크립트가 들어간다**는 거다. png는 픽셀 데이터지만 svg는 마크업이다. 브라우저가 열면 그냥 그려지는 게 아니라 **해석한다.**

```svg
<svg xmlns="http://www.w3.org/2000/svg">
  <script>alert(document.cookie)</script>
</svg>
```

이걸 업로드해서 누가 그 URL로 직접 열면 스크립트가 그 도메인에서 돈다. 이미지 파일이 XSS 벡터가 된다. 확장자도 맞고 내용도 진짜 SVG니까 지금까지의 검사는 다 통과한다.

그런데 아이콘 업로드처럼 SVG가 꼭 필요한 자리가 있었다. 거기는 전용 검증을 따로 만들었다.

```java
// 크기 상한 100KB
if (file.getSize() > 100 * 1024) { ... }

String[] dangerousTags = {
        "<script", "<iframe", "<object", "<embed",
        "<foreignobject",    // SVG 안에 HTML 을 넣는 통로
        "<handler"
};

String[] dangerousAttributes = {
        "onload=", "onerror=", "onclick=", ... ,
        "javascript:", "data:text/html", "vbscript:"
};

// SVG 고유 — xlink:href 로도 스크립트를 걸 수 있다
if (lowerContent.matches(".*xlink:href\\s*=\\s*[\"']\\s*javascript:.*")) { ... }
```

`<foreignObject>` 와 `xlink:href` 가 SVG에서만 나오는 벡터다. 일반 HTML XSS 목록만 가져다 쓰면 이 둘이 빠진다.

이건 블랙리스트라 XSS 필터와 같은 한계가 있다. 내가 아는 태그까지만 막는다. SVG 스펙이 넓어서 목록이 충분하다고 자신할 수 없다.

### 그리고 여기 약점이 하나 있다

```java
String contentType = file.getContentType();
if (contentType == null || !contentType.equals("image/svg+xml")) {
    return fail("Only SVG files are allowed.");
}
```

`file.getContentType()` 은 **브라우저가 보낸 값**이다. 멀티파트 요청의 `Content-Type` 헤더를 그대로 읽는다. 공격자는 요청을 직접 만들 수 있으니 아무 값이나 넣을 수 있다.

다른 메서드들은 Tika로 내용을 읽는데 SVG 검증만 신고값을 믿는다. 뒤에서 내용을 파싱해서 태그를 검사하니까 결과적으로는 막히지만, **검증 순서상 첫 관문이 위조 가능한 값**이다. 일관성이 깨진 자리다. 다시 하면 여기도 내용 기준으로 바꿀 것 같다.

## 크기 제한은 내 코드보다 먼저 터진다

크기 상한을 상수로 뒀다.

```java
// web.xml multipart-config 의 max-file-size 와 같은 값으로 유지한다
private static final long DEFAULT_MAX_FILE_SIZE = 20L * 1024 * 1024;
```

주석을 달아둔 이유가 있다. 같은 값이 **두 군데**에 있다. 그리고 순서가 중요하다.

```
요청 도착
  ↓
컨테이너가 멀티파트를 파싱        ← web.xml max-file-size 가 여기서 걸린다
  ↓
컨트롤러 진입
  ↓
내 검증 코드                      ← DEFAULT_MAX_FILE_SIZE
```

web.xml 값이 더 작으면 **내 코드는 아예 실행되지 않는다.** 컨테이너가 파싱 단계에서 예외를 던지니까 내가 준비한 안내 메시지("20MB 이하만 됩니다")를 줄 기회가 없다. 컨테이너 기본 오류 페이지가 나간다.

그래서 두 값을 같게 맞춰야 한다. 어느 쪽이 먼저 걸리든 같은 결과가 나오게. 동기화를 코드로 강제할 수 없어서 주석에 적어뒀는데, 주석은 지켜지지 않는다. web.xml에서 읽어오는 게 맞았을 것 같다.

크기 검증을 생략하는 길도 뒀다.

```java
// maxSize <= 0 이면 검증 생략 (multipart 설정에 위임)
if (maxSize > 0 && file.getSize() > maxSize) { ... }
```

## 거부 메시지에 개행을 넣을 수 없었다

거부할 때 **무엇을 올릴 수 있는지 같이** 알려준다.

```java
return fail(String.format("첨부할 수 없는 파일 형식입니다. (%s) 첨부 가능: %s",
        extension, joinExtensions(allowedExtensions)));
```

"안 됩니다"만 주면 사용자가 다시 시도할 근거가 없다. 뭐가 되는지 알려줘야 한다.

목록을 만들 때 정렬한다.

```java
// Set 은 순서가 없어 정렬해서 내보낸다
return extensions.stream().sorted().collect(Collectors.joining(", "));
```

`HashSet` 은 순서가 보장되지 않는다. 정렬 안 하면 같은 화면에서 안내 문구 순서가 그때그때 달라진다. [ES 노트](../elasticsearch/transform-rollup.md)에서 스냅샷 문자열에 `.sorted()` 를 빼먹어서 게이팅이 무력화됐던 것과 같은 종류다. **`Set` 을 문자열로 만들 때는 정렬해야 한다.**

그리고 보기 좋게 하려고 목록 앞에 줄바꿈을 넣었다가 화면이 깨졌다.

응답을 만드는 코드가 값을 **이스케이프 없이 JSON 문자열에 끼워넣고** 있었다. 개행이 들어가면 JSON 문법이 깨져서 브라우저의 `JSON.parse` 가 실패한다. 화면에 아무 안내도 안 뜬다.

```
{"errorMessage":"첨부할 수 없는 파일 형식입니다.
첨부 가능: csv, xls, xlsx"}     ← JSON 문자열 안에 생 개행 → parse 실패
```

[SSE 노트](../spring/sse.md)에서 `tabId` 가 응답 `id` 에 그대로 박혀서 개행으로 이벤트를 위조할 수 있었던 것과 똑같은 모양이다. 거기는 공격이고 여기는 내가 넣은 개행이지만 원인은 하나다. **직렬화를 손으로 하면서 이스케이프를 안 하면 데이터가 구조를 깨뜨린다.**

제대로 고치려면 응답 생성을 Jackson 같은 걸로 바꿔야 한다. 일단은 메시지에 개행을 안 넣는 쪽으로 피했다. 피한 거지 고친 게 아니다.

---

파일 업로드는 검사할 게 많아 보였는데, 결국 질문 두 개였다. **이 파일이 자기가 주장하는 그 파일인가**, 그리고 **이 이름이 내가 정한 자리에만 저장되는 이름인가.**

첫 번째는 컨테이너 포맷 때문에 끝까지 확실해지지 않았다. zip 안을 안 열면 xlsx와 zip을 구분할 방법이 없고, 그래서 느슨한 매핑을 허용하는 타협을 했다. 두 번째는 반대로 깔끔했다 — "경로를 떼어낸 게 원본과 같다"는 한 줄이 패턴 열거 전체보다 강했다.

같은 코드 안에서 한쪽은 불변식으로 풀리고 한쪽은 안 풀렸다. 차이는 **원하는 조건을 한 문장으로 적을 수 있느냐**였다.
