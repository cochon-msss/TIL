# Java volatile

멀티스레드에서 변수에 붙이는 `volatile`이 뭔지 정리해봤다. 한 줄로 하면 "이 변수는 캐시하지 말고 항상 메인 메모리에서 읽고 써라" 라는 표시다.

## 왜 필요하냐

스레드는 성능 때문에 변수 값을 자기 CPU 캐시에 복사해두고 쓸 수 있다. 문제는 한 스레드가 값을 바꿔도 다른 스레드는 자기 캐시의 옛날 값을 계속 보는 상황이 생긴다는 거.

```java
class Worker {
    boolean running = true;   // volatile 없음

    void run() {
        while (running) {
            // 열심히 일함
        }
        System.out.println("멈춤");
    }
}
```

다른 스레드에서 `running = false`로 바꿔도, 이 while 도는 스레드는 캐시에 있는 `true`만 계속 봐서 영원히 안 멈출 수 있다. 실제로 이런 무한루프 버그가 난다.

여기에 `volatile`을 붙이면:

```java
volatile boolean running = true;
```

이제 `running`은 캐시 안 하고 항상 메인 메모리에서 읽는다. 그래서 다른 스레드가 바꾼 `false`를 바로 보고 멈춘다. 이걸 가시성(visibility) 보장이라고 한다.

덤으로 컴파일러나 CPU가 성능 위해 하는 명령어 재배치(reordering)도 막아준다. 메모리 배리어 역할.

## 근데 원자성은 보장 안 됨

`volatile`은 "보이게" 는 해주는데 "동시에 안전하게" 는 아니다.

```java
volatile int count = 0;
count++;   // 위험
```

`count++`는 사실 읽고 -> 1 더하고 -> 쓰기 이렇게 세 단계라, 두 스레드가 동시에 하면 값이 꼬인다(race condition). 이런 복합 연산은 volatile로 못 막는다.

- 그냥 플래그 하나 켜고 끄기(위의 running 예시) -> volatile로 충분
- count++ 같은 계산 -> `synchronized` 나 `AtomicInteger` 써야 함

## static이랑 다른 거야?

완전히 다른 거다. 자주 헷갈리는데 축이 다르다.

- `static` = 이 변수가 몇 개 있냐 / 누구 소유냐 문제. 인스턴스마다 따로 안 갖고 클래스에 하나만 있어서 모두가 공유.
- `volatile` = 이 변수를 읽을 때 최신값을 보장하냐 문제. 캐시 하지 말고 메인 메모리에서 읽어라.

비유하면 `static`은 반 전체가 같이 쓰는 칠판 하나(각자 공책에 따로 안 갖고 공유), `volatile`은 그 칠판 볼 때 눈으로 직접 보고 읽어라(머릿속에 베껴둔 옛날 메모 보지 말고).

### 헷갈렸던 포인트

"static이면 어차피 하나를 공유하니까 스레드끼리도 공유되잖아? 그럼 volatile 필요 없는 거 아냐?" 이게 함정이었다.

공유한다 != 최신값이 보인다. static으로 변수 하나를 공유해도, 각 스레드는 여전히 그 값을 자기 캐시에 베껴놓고 본다. 그래서 아까 그 무한루프 버그, `static boolean running`으로 해도 똑같이 남는다.

```java
static boolean running = true;   // 공유는 되는데, 최신값 보장은 안 됨 -> 무한루프 여전히 가능
```

`static`은 어느 변수를 보냐를 정하고, `volatile`은 그 변수를 볼 때 최신으로 보냐를 정한다. 목적이 달라서 둘이 같이 쓰기도 한다.

```java
static volatile boolean running = true;
// 클래스에 하나 공유(static) + 캐시 안 하고 최신으로 읽기(volatile)
```

정리하면 이렇게 갈린다.

| | 뭘 정하나 | 관심사 |
|---|---|---|
| `static` | 인스턴스마다? vs 클래스에 하나? | 공유 / 스코프 |
| `volatile` | 캐시된 값? vs 메인 메모리 최신값? | 스레드 가시성 |

그래서 `static`은 싱글스레드에서도 의미 있고, `volatile`은 멀티스레드일 때만 의미가 있다.

## 한 줄 정리

- 가시성만 필요하면 `volatile`
- 원자성까지 필요하면 `synchronized` / `Atomic`
- `static`이랑은 아예 다른 축의 얘기 (공유 vs 가시성)
