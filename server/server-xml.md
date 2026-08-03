# server.xml

톰캣의 `server.xml` 파일은 보통 `conf` 폴더 내에 위치한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Server port="8005" shutdown="SHUTDOWN">
  <Service name="Catalina">
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000" redirectPort="8443" />
    <Engine name="Catalina" defaultHost="localhost">
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
               resourceName="UserDatabase"/>
      </Realm>
      <Host name="localhost" appBase="webapps"
            unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve"
               directory="logs" prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />
      </Host>
    </Engine>
  </Service>
</Server>
```

- **Server**: 톰캣 인스턴스 최상위 요소. `port="8005"`는 셧다운 명령을 받는 포트다.
- **Service**: 하나 이상의 Connector와 하나의 Engine을 묶는다.
- **Connector**: 클라이언트 요청을 받는 포트를 정의한다. HTTP는 8080, SSL 리다이렉트는 8443.
- **Engine**: 요청을 처리하는 Catalina 엔진. `defaultHost`로 기본 호스트를 지정한다.
- **Host**: 가상 호스트. `appBase="webapps"`에 배포된 애플리케이션을 자동 배포한다.
- **Valve**: 요청/응답을 가로채는 컴포넌트. 위 예시는 접근 로그(AccessLogValve)를 남긴다.
