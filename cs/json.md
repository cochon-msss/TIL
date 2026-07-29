# JSON

**JSON(JavaScript Object Notation)** 은 사람이 읽을 수 있고 시스템에서 구문 분석할 수 있는 방식으로 데이터를 저장하고 교환하기 위한 **텍스트 기반 형식**이다. 일반적으로 웹 개발자가 서버와 웹 애플리케이션 간에 데이터를 전송하는 데 사용한다. 다양한 기술 간의 데이터 교환을 단순화하기 때문에 개발자들이 자주 선호한다.

예를 들어 사용자가 웹 애플리케이션에서 구매를 하는 경우, 애플리케이션은 사용자의 입력을 JSON 형식으로 서버에 전송한다. 서버는 데이터를 처리하고 응답을 JSON 형식으로 다시 전송하며, 이를 웹 애플리케이션이 렌더링한다. JSON은 JavaScript에 기반하지만 다양한 플랫폼 및 프로그래밍 언어에서 데이터 교환을 단순화하는 강력한 데이터 형식으로 성장했다.

## 특징

- 웹 개발자가 서버와 웹 애플리케이션 간에 데이터를 전송하는 데 자주 사용하는 데이터 형식이다.
- 텍스트 기반이므로 사람이 쉽게 읽고 컴퓨터가 쉽게 이해한다.
- 언어 독립적 특성 덕분에 다양한 프로그래밍 언어와 플랫폼에서 데이터를 교환하기에 이상적이다.
- 많은 데이터베이스가 JSON으로 데이터를 저장하고 교환하기 위해 등장했다.

## JSON, XML, HTML

웹에 데이터를 저장하고 전송할 수 있는 형식은 다양하다. 가장 인기 있는 세 가지는 JSON, XML, HTML이다. JSON과 XML은 데이터를 저장하고 전송하는 데 사용되는 형식이며 각각 다른 강점을 가진다. HTML은 웹 페이지의 구조를 생성하는 데 사용되는 언어이다.

- **JSON**(JavaScript Object Notation): 일반적으로 데이터 저장 및 전송에 사용된다. 간단하고 사용하기 쉬워 널리 채택된다.
- **XML**(Extensible Markup Language): 복잡한 데이터 구조를 허용하는, JSON과 유사한 범용 마크업 언어이다.
- **HTML**(Hypertext Markup Language): 웹 페이지의 구조 및 콘텐츠를 생성하는 데 사용된다.

## JSON 구조

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    }
  ]
}
```

## 단점

- 주석을 지원하지 않아 설정 파일을 JSON으로 작성할 때 어려움이 있다.
- 데이터 타입을 강제하려면 JSON 스키마로 보완해야 한다.
- 날짜/시간 타입을 지원하지 않는다.
