# Git 명령어

## 기본 흐름
- `mkdir git` : git이라는 폴더 생성
- `ls -al` : 파일 확인
- `git init` : 깃 초기화. 초기화하면 기본적으로 master 브랜치가 생성됨
- `rm -rf .git` : 깃 제거
- `git status` : 상태 확인
- `echo "hello world!" > a.txt` : 문자열을 a.txt에 저장(생성)
- `open .` : 현재 위치한 폴더 열기

## add / commit
- `git add <file>` : 커밋할 준비가 된 변경사항을 스테이징(tracked 상태로)
- 파일을 변경하면 다시 `add` 해야 함
- `git rm --cached *` : 트랙에 올라간 파일들을 다시 언트랙으로 내림
- (참고) tracked에 올린 파일을 삭제(`rm a.txt`)하면 다시 `git add .` 해줘야 함
- `git diff` : 변경사항이 있는지 확인
- `git difftool` : 수정 내용 확인
- `git commit` : 저장소에 현재 변화(스테이지의 변화)를 커밋
- `git commit -m "second commit"` : 커밋 메시지도 같이 저장

메모: 브랜치 색이 초록색에서 주황색으로 변하면 브랜치가 변경됐다는 뜻(아직 커밋 안 됨).

## 설정
- `git --version` : 깃 버전 확인
- `git config --global user.name "이름"` : 유저 이름 설정
- `git config --global user.email "이메일"` : 유저 이메일 설정
- `git config --list` : 설정 리스트 출력

## 로그 / 되돌리기
- `git log --oneline` : 커밋 관련 간략한 로그 출력
- `git checkout <commit> <file>` : 이전 버전의 커밋된 상태로 체크아웃(일종의 되돌리기)
- `git checkout master` : 원래 버전으로 되돌아오기
- `git reset` : 저장소를 이전 커밋된 상태로 되돌리기

## 원격 저장소
- `git remote add origin <repository URL>` : 원격 저장소 등록
- `git push -u origin master` : 로컬 저장소의 정보를 origin의 master 브랜치에 push (push = 로컬 → 원격 반영)
- `git clone <repository URL>` : 원격 저장소의 복제본을 로컬에 저장
