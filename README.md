# WECODE git 중간시험>

## [ 오늘 시험에서 사용했던 명령어 최소 3개 이상 정리 ]


### `1.  git init` 

- 현재 디렉토리를 git local repository[Working Directory]로 지정(생성)

### `2. git add .` 

- staging area 로 모든 파일 한번에 추가(프로젝트 폴더 내의 모든파일과 폴더를 staging area 에 추가하고 커밋을 남길 수 있게해줌

### `3. git commit -m "Commit message"` 

- 식별을 위한 커밋 메세지 작성(레포지토리에커밋남기기)

### `4. git remote add <name> <url>` 

- 원격 저장소 추가, 생성한 디렉토리와 repository 주소 연동 (# git remote add origin <url>)

### `5. git remote -v`

- 원격 저장소 목록 확인 및 상세정보 표시 

### `5. git push origin main` 

-  origin이라는 원격저장소의 main 브랜치에 푸쉬

### `6. git branch` 

- 프로젝트에 존재하는 모든 브랜치 확인(현재 속한 브랜치는 앞에 *가 붙음)

### `7. git branch -M  main` 

- main으로 브랜치 명 변경

### `8.git checkout -b <브랜치명>`

- 브랜치를 새로 생성하고 바로 그곳으로 이동(checkout)

### `9. git status`

- git 상태확인 , git add 명령어와 주로 함께사용, 작업 디렉토리(working directory)와 스테이징 영역(staging area)의 상태를 확인하기 위해서 사용

### `10. git log`

- commit 이력 보기 