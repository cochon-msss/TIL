# Java

## 함수형 인터페이스 (Functional Interface)

- `java.lang.Runnable` | `void run()` | 매개변수도 없고, 반환값도 없음
- `Supplier<T>` | `T get()` | 매개변수는 없고, 반환값만 있음
- `Consumer<T>` | `void accept(T t)` | Supplier와 반대로 매개변수만 있고, 반환값이 없음
- `Function<T, R>` | `R apply(T t)` | 일반적인 함수, 하나의 매개변수를 받아서 결과를 반환함
- `Predicate<T>` | `boolean test(T t)` | 조건식을 표현하는 데 사용됨, 매개변수는 하나, 반환 타입은 boolean

람다식 표현:

```
반환타입 메서드이름(매개변수 선언) { 문장들 }

(매개변수 선언) -> { 문장들 }
```

## 메서드 참조

- **하나의 메서드만 호출**하는 람다식은 `클래스이름::메서드이름`
- 또는 `참조변수::메서드이름`으로 바꿀 수 있다.

```java
import java.util.function;

MyClass obj = new MyClass();
Function<String, Boolean> f = (x) -> obj.equals(x);  // 람다식
Function<String, Boolean> f2 = obj::equals;          // 메서드 참조
```

- 생성자를 호출하는 람다식도 메서드 참조로 변환할 수 있다.

```java
Supplier<MyClass> s = () -> new MyClass();   // 람다식
Supplier<MyClass> s = MyClass::new;          // 메서드 참조

// 매개변수가 있는 생성자
Function<Integer, MyClass> f = (i) -> new MyClass(i);  // 람다식
Function<Integer, MyClass> f2 = MyClass::new;          // 메서드 참조

// 배열 생성
Function<Integer, int[]> f = x -> new int[x];    // 람다식
Function<Integer, int[]> f2 = int[]::new;        // 메서드 참조

// 메서드 참조는 람다식을 마치 static 변수처럼 다룰 수 있게 해준다.
```

## 스트림 (Stream)

- 스트림을 이용하면, 배열이나 컬렉션뿐만 아니라 파일에 저장된 데이터도 모두 같은 방식으로 다룰 수 있다.

### 스트림 만들기 - 컬렉션

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class Func {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        Stream<Integer> is = list.stream();  // list를 stream으로 변환

        is.forEach(System.out::print);       // forEach 최종연산
        System.out.println();

        // Stream은 1회용, stream에 대해 최종연산 수행하면 stream이 닫힌다.
        is = list.stream();                  // list로부터 stream을 생성
        is.forEach(System.out::print);
    }
}
```

### 스트림 만들기 - 배열

```java
String[] strArr = new String[] {"a", "b", "c"};
Stream<String> strStream = Stream.of(strArr);
Stream<String> strStream = Stream.of(new String[] {"a", "b", "c"});
Stream<String> strStream = Arrays.stream(strArr);
strStream.forEach(System.out::println);

// Integer stream 에는 최종연산 count밖에 없음
Integer[] intArr = {1, 2, 3, 4, 5};
Stream<Integer> intStream = Arrays.stream(intArr);
intStream.forEach(System.out::println);
System.out.println("count=" + intStream.count());

int[] intArr = {1, 2, 3, 4, 5};
IntStream intStream = Arrays.stream(intArr);
System.out.println("count=" + intStream.count());
System.out.println("sum=" + intStream.sum());
System.out.println("avg=" + intStream.average());
```

### 람다식 iterate(), generate()

```java
// 초기화
// iterate(T seed, UnaryOperator) 단항 연산자
Stream<Integer> intStream = Stream.iterate(1, n -> n + 2);
intStream.forEach(System.out::print);

// generate(Supplier s) : 주기만 하는 것, 입력 x, 출력 o
Stream<Integer> oneStream = Stream.generate(() -> 1);
oneStream.forEach(System.out::print);
```

## 로직 정리

### 쓰레드 초 딜레이

```java
package class01;

import java.util.Date;

public class Test02 {
    public static void main(String[] args) {
        try {
            System.out.println("start" + new Date());
            Thread.sleep(5000);
            System.out.println("end.." + new Date());
        } catch (Exception e) {
        }
    }
}
// 지연문. 예외처리 해줘야 함. InterruptedException 발생
```

### 정렬

#### 배열 거꾸로 정렬

```java
Arrays.sort(arr, Collections.reverseOrder()); // 근데 String만 됨

// 1. 원본 배열
Integer[] arr = { 1, 2, 3, 4, 5 };

// 2. 원본 배열을 List로 변환
List<Integer> list = Arrays.asList(arr);

// 3. Collections.reverse() 메서드를 사용하여 list를 거꾸로 변환
Collections.reverse(list);

// 4. 리스트를 배열로 변환
Integer[] reverseArr = list.toArray(arr);

// 5. 결과 출력
System.out.println("arr : " + Arrays.toString(arr));
System.out.println("reverseArr : " + Arrays.toString(reverseArr));

// list로 변환해서 정렬하고 다시 배열로 가지고 옴
```

#### 버블 정렬

```java
for (int a = 0; a < data.length; a++) {
    for (int i = 0; i < data.length - 1; i++) { // 데이터 개수만큼 반복
        // 마지막 -1을 써야 자기 자신과는 비교하지 않는다.
        if (data[i] > data[i + 1]) {
            int tmp = data[i];
            data[i] = data[i + 1];
            data[i + 1] = tmp;
        }
    }
}
```

#### 삽입 정렬

```java
public static void main(String[] args) {

    int[] arr = {3, 1, 5, 2, 7};

    for (int i = 1; i < arr.length; i++) { // 삽입정렬 시작. i=1인 이유는 두 번째 배열부터 시작해야 하기 때문
        int tmp = arr[i];                  // tmp에 반복되는 배열을 먼저 저장한다.
        int index = i - 1;                 // 현재 원소 이전의 원소를 탐색하기 위한 index 변수
        System.out.println(i + "회전 정렬");
        // 현재 배열의 왼쪽에 있는 정수를 알기 위해 -1
        // 자기 위치에서 앞에 위치한 배열의 값들을 차례대로 비교

        // (index가 0보다 크거나 같고) (sort 배열의 index 순서에 들어있는 원소가 tmp보다 클 경우까지만) 반복
        while (index >= 0 && arr[index] > tmp) {
            arr[index + 1] = arr[index]; // 조건이 참일 때 앞 배열의 값을 뒤로 이동
            index--;                     // 작은 수를 앞에 저장하기 위해 index-- 진행
            System.out.println(Arrays.toString(arr));
        }
        arr[index + 1] = tmp; // while문이 false가 되면 tmp에 저장한 수를 다시 저장

        System.out.println(i + "-1회전 정렬\n" + Arrays.toString(arr));
    }
    System.out.println("정렬 끝\n" + Arrays.toString(arr));
}
```

#### 퀵 정렬

```java
public static void main(String[] args) {
    int[] data = new int[10];
    data[0] = 4;
    data[1] = 1;
    data[2] = 10;
    data[3] = 2;
    data[4] = 8;
    data[5] = 7;
    data[6] = 9;
    data[7] = 3;
    data[8] = 6;
    data[9] = 5;
    for (int v : data) {
        System.out.print(v + " ");
    }
    System.out.println();

    quickSort(data, 0, data.length - 1);
    for (int v : data) {
        System.out.print(v + " ");
    }
}

public static void quickSort(int[] data, int start, int end) {
    if (start >= end) { // 더 이상 분할되지 않을 때
        return;
    }
    int pivod = data[start]; // 맨 왼쪽에 있는 데이터
    int L = start + 1;
    int H = end;

    while (L < H) {

        while (data[L] < pivod) {
            L++;
        }

        while (data[H] > pivod) {
            H--;
        }

        if (L > H) { // 크로스
            break;
        }

        int tmp = data[L];
        data[L] = data[H];
        data[H] = tmp;
    }
    int tmp = data[start];
    data[start] = data[H];
    data[H] = tmp;

    quickSort(data, start, H - 1);
    quickSort(data, H + 1, end);
}
```

#### 선택 정렬

```java
public static void main(String[] args) {
    int[] nums = {2, 5, 4, 8, 3, 6, 1, 7, 9};

    System.out.println("정렬 전");
    System.out.println(Arrays.toString(nums));
    System.out.println("----------------------------------");

    for (int i = 0; i < nums.length - 1; i++) {
        int MinIndex = i; // 현재 탐색에서 가장 앞의 값을 초기 값으로 설정해둔다.
        for (int j = i + 1; j < nums.length; j++) { // 탐색을 진행하며 가장 작은 값을 찾는다.
            if (nums[MinIndex] > nums[j])
                MinIndex = j; // for문 이용, 가장 작은 값을 초기화
        }
        // 탐색이 완료되면 가장 앞의 원소와 가장 작은 원소의 위치를 바꾸어준다.
        // 교체
        int temp = nums[MinIndex];
        nums[MinIndex] = nums[i];
        nums[i] = temp;
        System.out.println(i + "회전 정렬" + Arrays.toString(nums));
        System.out.println("----------------------------------");
        // 다시 for문 반복
    }

    System.out.println("정렬 후");
    System.out.println(Arrays.toString(nums));
}
```

#### 이진 탐색

```java
int L = 0;
int H = 100;
while (true) {
    int M = (L + H) / 2;
    System.out.println("L: " + L);
    System.out.println("H: " + H);
    System.out.println("M: " + M);
    System.out.println();
    if (num == data[M]) { // 찾으면
        System.out.println("index: " + M);
        break;
    } else if (data[M] < num) {
        L = M + 1;
    } else {
        H = M - 1;
    }

    if (L > H) { // cross(교차), 없는 값을 찾을 때
        System.out.println(num + "은 없습니다...");
        break;
    }
}
```

#### 중복 없이 저장 - flag 변수

```java
while (true) {
    int rdrange = rand.nextInt(range) + 1;
    System.out.println("g" + Arrays.toString(rdNum));
    boolean flag = false;
    for (int i = 0; i < checkIndex; i++) {
        if (rdrange == rdNum[i]) {
            flag = true;
            break;
        }
    }
    System.out.println("1" + Arrays.toString(rdNum));

    if (!flag) { // 조건식이 false인데 !으로 true로 바꿔 if문 안의 문장을 실행
        rdNum[checkIndex] = rdrange;
        checkIndex++;
    } else {
        continue;
    }
    System.out.println("2" + Arrays.toString(rdNum));

    if (checkIndex == rdNum.length) {
        break;
    }
}
System.out.println("중복 없는 랜덤값: " + Arrays.toString(rdNum));
```

#### 교환

```java
if (a > b) { // a가 b보다 크다면 a와 b를 교환해준다.
    int tmp = a;
    a = b;
    b = tmp;
}
```

#### 배열 삭제

```java
public static int[] removeElement(int[] arr, int item) {
    return Arrays.stream(arr)
            .filter(i -> i != item)
            .toArray();
}
// 메서드 따로 정의
```

### Math 클래스

수학적 계산 기능을 구현한 Math 클래스가 있습니다. Math 클래스에는 여러 편리한 함수를 제공합니다.

- `abs`: 인수의 절대값을 반환
- `ceil`: 인수의 올림 값을 반환
- `cos`: 인수의 코사인 값을 반환
- `floor`: 인수의 내림값을 반환
- `max`: 2개의 인수 중 큰 값을 반환
- `min`: 2개의 인수 중 작은 값을 반환
- `pow`: 첫 번째 인수를 두 번째 인수만큼 거듭제곱한 값을 반환
- `random`: 랜덤값 반환
- `rint`: 인수에 가장 가까운 값을 반환
- `sin`: 인수의 사인 값을 반환
- `sqrt`: 인수의 제곱근을 반환
- `tan`: 인수의 탄젠트 값을 반환
- `log`: 인수의 로그 값을 반환

```java
double d1 = Math.abs(3.4);
int i1 = Math.abs(3);
double d2 = Math.ceil(3.4);
double d3 = Math.cos(3.4);
double d4 = Math.floor(3.4);
double d5 = Math.max(3.4, 3.5);
double d6 = Math.min(3.4, 3.5);
double d7 = Math.pow(3.4, 2);
double d8 = Math.random();
double d9 = Math.rint(3.4);
double d10 = Math.sin(3.4);
double d11 = Math.sqrt(2);
double d12 = Math.tan(3.4);
double d13 = Math.log(3.4);
```

### 수학

#### 약수

```java
int num = 6;
int i = 1;
while (i <= num) {
    if (num % i == 0) {
        System.out.println("i= " + i);
    }
    i++;
}
```

#### 소수

```java
int num = 3;

int i = 1;
int cnt = 0; // 약수의 개수
while (i <= num) {
    if (num % i == 0) { // i가 num의 약수라면
        cnt++;          // 약수를 찾은 것
    }
    i++;
}

if (cnt == 2) { // num이 소수라면
    System.out.println(num + "은 소수입니다.");
} else {
    System.out.println(num + "은 소수가 아닙니다.");
}
```

#### 완전수

```java
Scanner sc = new Scanner(System.in);
System.out.print("정수를 입력: ");
int num = sc.nextInt();

int sum = 0;
int i = 1;
while (i < num) { // 자기 자신을 제외한 약수들의 합
    if (num % i == 0) {
        sum += i;
        System.out.println("sum= " + sum);
    }
    i++;
}

if (sum == num) { // 합이 자기 자신과 같으면 완전수
    System.out.println("완전수입니다.");
} else {
    System.out.println("완전수가 아닙니다.");
}
```

#### 최대공약수, 최소공배수

```java
Scanner sc = new Scanner(System.in);

System.out.print("a: ");
int num1 = sc.nextInt();
System.out.print("b: ");
int num2 = sc.nextInt();

int i = 1;
int max = 0;
while (i <= num1 && i <= num2) {
    if (num1 % i == 0 && num2 % i == 0) {
        max = i;
    }
    i++;
}
int min = (num1 * num2) / max;
System.out.println(num1 + "와 " + num2 + "의 최대공약수는 " + max + "이고, 최소공배수는 " + min + "입니다.");
```

### equals() 오버라이딩

```java
@Override
public boolean equals(Object obj) { // obj에는 x와 y가 없다
    if (obj instanceof Point) {     // 캐스팅이 가능한지 먼저 물어봄 (instanceof)
        Point p = (Point) obj;      // 다운 캐스팅. 이런 경우에만 사용. Point에는 x, y가 존재
        if (p.x == this.x && p.y == this.y) {
            return true;
        }
    }
    return false;
}
```

### char 타입 String에 저장 후 int로 변환

```java
String tmp = "";
for (char v : datas) {
    tmp += v; // 문자열 더하기
}
int ans = Integer.parseInt(tmp);
System.out.println("ans=" + ans);
```

## 까먹지 말아야 할 것

- `nextInt()`는 정수만 가져가고 enter(개행)를 버퍼에 남겨둬서 무한 반복이 될 수도 있다. 그래서 enter 값을 빼줘야 하는데, 그때 `nextLine();`을 작성한다.
- 좋은 코드는 디폴트값을 지정해놓고 거기에 조건을 다는 것이다.
- 게터 메서드는 초기 저장 값을 반환하고, 세터 메서드는 게터가 반환할 값을 다른 값으로 초기화할 때 사용한다.
- `toString` 안에 if문을 작성해서 조건에 따라 다르게 toString을 호출할 수 있다.
- ArrayList에 배열 객체를 저장할 수도 있다.
- 기본형 타입 비교는 `==`

## 애너테이션(어노테이션)

실수를 줄이기 위해 붙이는 것이 좋다.
