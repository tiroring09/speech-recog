# 사용법: docker build -t 태그이름 .
# 사용법: docker build . -t 태그이름
# docker run -d -p 8000:8000 태그이름
# docker run -p 8000:8000 태그이름 << 포어그라운드 실행

# 베이스 이미지
FROM python:3.10

# ffmpeg설치 << pydub의 의존성
RUN apt-get update && \
  apt-get install -y ffmpeg

# 루트디렉토리 설정
WORKDIR /speech-recog

# 의존성 설치 - pip를 기준으로 함. poetry사용하면 수정필요
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install poetry
# COPY pyproject.toml poetry.lock /speech-recog/
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root



# 소스코드 복붙
# COPY ./src /speech-recog/src
COPY ./src ./src
# COPY ./frontend/dist /speech-recog/frontend/dist
COPY ./frontend/dist ./frontend/dist

# 실행 명령어
CMD [ "poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0"]

# 포트 노출
EXPOSE 8000