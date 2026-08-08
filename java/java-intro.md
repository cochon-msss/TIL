# Java란

Java는 1995년 Sun Microsystems에서 개발한 객체지향 프로그래밍 언어이다. **"한 번 작성하면, 어디서나 실행된다(Write Once, Run Anywhere)"** 라는 철학을 바탕으로 플랫폼 독립적인 언어로 설계되었다. 이는 Java로 작성된 프로그램이 운영 체제에 관계없이 JVM(Java Virtual Machine)이 설치된 어떤 환경에서도 실행될 수 있음을 의미한다.

## 주요 특징

- 객체 지향
- 플랫폼 독립성
- 강력한 메모리 관리
- 풍부한 표준 라이브러리
- 높은 보안성

## 버전

Java는 지속적으로 발전하고 있으며 여러 버전이 존재한다. 가장 최신 버전을 사용하는 것이 좋지만, 프로젝트의 요구사항이나 호환성을 고려해야 한다.

- **Java 8 (LTS)**: 2014년 출시, 여전히 널리 사용됨
- **Java 11 (LTS)**: 2018년 출시, 장기 지원 버전
- **Java 17 (LTS)**: 2021년 출시, 장기 지원 버전
- **Java 21 (LTS)**: 2023년 출시

> LTS(Long-Term Support): 장기간 지원과 업데이트가 제공되므로 안정성을 중시하는 프로젝트에 적합하다.

## Java SE vs Java EE vs Java ME

1. **Java SE (Standard Edition)**
   - 가장 기본적인 플랫폼
   - 핵심 프로그래밍 도구와 API 제공
   - 데스크톱 및 간단한 서버 애플리케이션 개발에 사용

2. **Java EE (Enterprise Edition)**
   - Java SE를 기반으로 구축
   - 대규모, 다계층, 확장 가능하고 안정적이며 안전한 네트워크 애플리케이션 개발을 위한 API와 런타임 환경 제공
   - 웹 애플리케이션 서버에서 실행됨

3. **Java ME (Micro Edition)**
   - 제한된 리소스를 가진 임베디드 및 모바일 장치를 위한 플랫폼
   - 경량화된 Java API 제공

대부분의 개발자는 Java SE로 시작하며, 필요에 따라 EE나 ME로 확장한다.

## JDK vs JRE

Java를 다운로드할 때 JDK와 JRE 중 어떤 것을 선택해야 할지 고민될 수 있다.

1. **JRE (Java Runtime Environment)**
   - Java 프로그램을 실행하기 위한 최소한의 환경
   - JVM과 Java 클래스 라이브러리를 포함
   - Java 애플리케이션을 실행만 하려는 경우

2. **JDK (Java Development Kit)**
   - JRE를 포함하며, 추가로 개발 도구 제공
   - 컴파일러(javac), 디버거, 문서 생성기(javadoc) 등 포함
   - Java 애플리케이션을 개발하려는 경우 필요

개발자라면 JDK, 단순히 Java 프로그램을 실행만 하려는 경우 JRE를 선택한다.
