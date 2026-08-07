# MVC 디자인 패턴

애플리케이션을 Model, View, Controller 세 가지 역할로 분리하는 디자인 패턴이다.

## Model

- DB(DBMS: MySQL, Oracle 등)와 연동되는 부분
- JAVA 코드 외적으로 저장된 데이터(DBMS에 저장된 데이터)를 JAVA 코드 내부로 연동해 가져오는 역할
- **데이터 파트**

## View

- 사용자 공간(Console, 브라우저, 클라이언트 등)
- 사용자의 편의성을 고려하고, 서비스를 제공하는 "대상"을 고려해야 하는 파트 (예: 폰, PC → 프론트엔드)
- 화면 구성(UI/UX)
- 사용자 입력값에 대한 유효성 검사

## Controller

- Model과 View를 연결하는 로직
- Model과 View는 다이렉트로 연결할 수 없으며 반드시 Controller를 통해 연결한다.

사용자가 서비스를 사용하기 위해 프로그램을 실행하면 다음 흐름으로 동작한다.

```
View → Controller → Model(DB)
Model(DB) → Controller → View
```

## MVC 설계 규칙

1. **Model은 Controller와 View에 의존하지 않아야 한다.** (Model 내부에 Controller와 View에 관련된 코드가 있으면 안 된다.)
2. **View는 Model에만 의존해야 하고, Controller에는 의존하면 안 된다.** (View 내부에 Model의 코드만 있을 수 있고, Controller의 코드가 있으면 안 된다.)
3. **View가 Model로부터 데이터를 받을 때는, 사용자마다 다르게 보여주어야 하는 데이터에 대해서만 받아야 한다.**
4. **Controller는 Model과 View에 의존해도 된다.** (Controller 내부에는 Model과 View의 코드가 있을 수 있다.)
5. **View가 Model로부터 데이터를 받을 때, 반드시 Controller에서 받아야 한다.**
