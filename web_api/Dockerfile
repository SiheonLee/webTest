
FROM python:3

# 컨테이너 내에서 코드가 실행될 경로 설정
WORKDIR /usr/src/app

# 배포 서버 업데이트
RUN apt -y -qq update & apt -y -qq dist-upgrade && apt -y -qq autoremove

# pip 업그레이드
RUN pip install --upgrade pip

# requirements.txt 파일 복사
COPY config/requirements.txt ./

# requirements.txt에 있는 라이브러리 설치
RUN pip install -r requirements.txt

# 현재 프로젝트를 /srv/velog 폴더에 복사
COPY . .

# Docker 컨테이너 생성시 default로 실행하는 명령어
CMD /bin/bash