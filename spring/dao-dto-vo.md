# DAO, DTO, VO

## DAO
`DAO(Data Access Object)`는 데이터베이스의 data에 접근하기 위한 객체.
DB에 접근하기 위한 로직과 비즈니스 로직을 분리하기 위해 사용한다.

## DTO
`DTO(Data Transfer Object)`는 계층 간 데이터 교환을 위해 사용하는 객체.
로직을 가지지 않는 순수한 데이터 객체(getter & setter만 가진 클래스)다.

유저가 입력한 데이터를 DB에 넣는 과정:
1. 유저가 브라우저에서 데이터를 입력하여 form에 있는 데이터를 DTO에 넣어서 전송한다
2. DTO를 받은 서버가 DAO를 이용하여 데이터베이스에 데이터를 넣는다

## VO
`VO(Value Object)`는 값을 위해 쓰인다. read-only 특징(사용 도중 변경 불가, 읽기만 가능)을 가진다.
DTO와 유사하지만, DTO는 setter를 가지고 있어 값이 변할 수 있다는 점이 다르다.
