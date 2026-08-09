# 코딩테스트 (프로그래머스)

부트캠프 기간에 풀었던 프로그래머스 문제 풀이 모음. 내 풀이와 다른 사람 풀이를 비교하며 정리했다.

## Lv.0

### 나이 구하기

```java
class Solution {
    public int solution(int age) {
        int result = 2022 - age + 1;
        return result;
    }
}
```

현재 연도에서 나이를 빼고 +1 하면 만 나이를 계산할 수 있다.

### 짝수의 합

```java
class Solution {
    public int solution(int n) {
        int result = 0;
        for (int i = 0; i <= n; i++) {
            if (i % 2 == 0) {
                result += i;
            }
        }
        return result;
    }
}
```

`%2`로 짝수를 판별하고, 반복문으로 1부터 n까지의 짝수만 합산한다.

### 양꼬치 구하기

```java
// 내가 구한 방식
class Solution {
    public int solution(int n, int k) {
        int kkochi = 12000;
        int drink = 2000;
        int sum2 = k * drink - (n / 10 * 2000);
        int sum = n * kkochi;
        return sum + sum2;
    }
}

// 다른 사람들이 구한 방식
class Solution {
    public int solution(int n, int k) {
        return n * 12000 + k * 2000 - (n / 10 * 2000);
    }
}
```

변수를 따로 두지 않고 한 줄로 계산한 방식이 더 깔끔하다.

### 배열의 평균값

```java
// 내 방식
class Solution {
    public double solution(int[] numbers) {
        double result = 0;
        for (int i = 0; i < numbers.length; i++) {
            result += numbers[i];
        }
        return result / numbers.length;
    }
}

// 향상된 for문 — number를 불러오기만 하면 되니 가독성이 올라간다
class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int number : numbers) {
            answer += number;
        }
        return answer / numbers.length;
    }
}

// 스트림 — Arrays.stream으로 배열 스트림을 생성하고 average()로 평균을 구한다
import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        return Arrays.stream(numbers).average().orElse(0);
    }
}
```

`average()`는 중간 연산이라 바로 이어 쓸 수 있고, `orElse(0)`은 값이 없을 때 기본값 0을 반환한다.

## Lv.1

### 짝수와 홀수

```java
class Solution {
    public String solution(int num) {
        return num % 2 == 0 ? "Even" : "Odd";
    }
}
```

삼항 연산자로 간단히 처리할 수 있다. 반환값이 String이므로 변수를 따로 만들 필요가 없다.

### 평균 구하기

```java
class Solution {
    public double solution(int[] arr) {
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum / arr.length;
    }
}
```

`result` 변수를 따로 선언하지 않고 return에 바로 작성하면 코드를 간략화할 수 있다.

### 약수의 합

```java
class Solution {
    public int solution(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }
        return sum;
    }
}
```

`i = 1`부터 시작해 n을 나누어떨어지게 하는 수(약수)를 더한다.

### 자릿수의 합

```java
public class Solution {
    public int solution(int n) {
        int answer = 0;
        while (n != 0) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}
```

123이 주어지면 `1 + 2 + 3 = 6`을 반환한다. `n % 10`으로 마지막 자릿수를 얻고, `n /= 10`으로 자릿수를 하나씩 줄이며 n이 0이 될 때까지 반복한다.

### 자연수 뒤집어 배열로 만들기

```java
// 길이를 먼저 구해 배열에 채우는 방식
class Solution {
    public int[] solution(long n) {
        int length = Long.toString(n).length();
        int[] answer = new int[length];
        for (int i = 0; i < length; i++) {
            answer[i] = (int) (n % 10);
            n /= 10;
        }
        return answer;
    }
}

// while문으로 채우는 방식
class Solution {
    public int[] solution(long n) {
        String a = "" + n;
        int[] answer = new int[a.length()];
        int cnt = 0;
        while (n > 0) {
            answer[cnt] = (int) (n % 10);
            n /= 10;
            cnt++;
        }
        return answer;
    }
}

// 스트림으로 한 줄 처리
import java.util.stream.IntStream;

class Solution {
    public int[] solution(long n) {
        return new StringBuilder()
                .append(n)
                .reverse()
                .chars()
                .map(Character::getNumericValue)
                .toArray();
    }
}
```
