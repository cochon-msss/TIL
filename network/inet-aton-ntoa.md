# INET_ATON / INET_NTOA

INET 함수는 IP를 정수로, 정수를 IP로 변환하는 함수이다.

## INET_ATON

IP 주소를 숫자로 변환한다.

> IPv4 네트워크 주소가 점으로 구분된 쿼드 문자열로 표현될 때, 네트워크 바이트 순서로 주소의 숫자 값을 나타내는 정수를 반환한다. 인수를 이해하지 못하거나 인자가 NULL인 경우 NULL을 반환한다.

```sql
SELECT INET_ATON('10.0.5.9');
-- 167773449
```

반환 값은 `(10 x 256^3) + (0 x 256^2) + (5 x 256) + 9`로 계산된다.

자바 코드로는:

```java
public static Long inetATON(String ip) {
    try {
        String[] segments = ip.split("\\.");
        return Long.parseLong(segments[0]) * 16777216L
             + Long.parseLong(segments[1]) * 65536L
             + Long.parseLong(segments[2]) * 256L
             + Long.parseLong(segments[3]);
    } catch (Exception exception) {
        return null;
    }
}
```

## INET_NTOA

숫자 값에서 IP 주소를 반환한다.

> 네트워크 바이트 순서로 숫자 IPv4 네트워크 주소가 주어지면, 주소의 점으로 구분된 쿼드 문자열 표현을 반환한다. 인수를 이해하지 못하면 NULL을 반환한다.

```sql
SELECT INET_NTOA(167773449);
-- '10.0.5.9'
```

자바 코드로는:

```java
public static String inetNTOA(long n) {
    try {
        return (n >> 24 & 0xFF) + "." + (n >> 16 & 0xFF) + "."
             + (n >> 8 & 0xFF) + "." + (n & 0xFF);
    } catch (Exception exception) {
        return null;
    }
}
```
