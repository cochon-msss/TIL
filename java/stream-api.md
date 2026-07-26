# Stream API

## 왜 쓰는가
컬렉션을 for문으로 돌리면서 조건 걸고 값 뽑고 하던 걸,
스트림으로 바꾸면 흐름이 눈에 더 잘 들어온다.
"거른다(filter) -> 바꾼다(map) -> 모은다(collect)" 순서로 읽힌다.

## 핵심 정리
- 스트림 연산은 중간 연산과 최종 연산으로 나뉜다.
  filter, map 같은 중간 연산은 바로 실행되지 않고,
  collect, forEach 같은 최종 연산을 만나야 그때 한 번에 돈다. (lazy)
- 스트림은 한 번 쓰면 끝. 같은 스트림을 두 번 최종 연산하면 예외 난다.
- 원본 컬렉션은 바뀌지 않는다. 결과는 새로 만들어진다.

## 예제
```java
// 20살 넘는 유저 이름만 리스트로 뽑기
List<String> names = users.stream()
        .filter(u -> u.getAge() > 20)
        .map(User::getName)
        .collect(Collectors.toList());
```

기존 for문으로 쓰면 이렇게 되던 것:
```java
List<String> names = new ArrayList<>();
for (User u : users) {
    if (u.getAge() > 20) {
        names.add(u.getName());
    }
}
```

## 막혔던 점
스트림을 변수에 담아놓고 재사용하려다 IllegalStateException이 났다.
"stream has already been operated upon or closed" 메시지.
스트림은 한 번 소비하면 닫히는 거라, 다시 쓰려면 users.stream()을
새로 호출해야 했다.

peek()이랑 map()도 헷갈렸는데, peek은 값을 바꾸지 않고
들여다보기(로그 찍기 등)만 하는 용도고, 값을 바꿔서 넘기는 건 map이다.
