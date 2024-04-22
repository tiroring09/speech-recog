speech-recognition

google
구글 > 데이터 수집하는지 검증 못함

sphinx

cmu sphinx > pocketsphinx

한국어모델 구해야 함
missing PocketSphinx language data directory


한국어 음성인식을 사용해볼 수 있는 개발자 사이트의 API로 AI-Hub에서 공개한 다양한 테스트셋의 에러율(Character Error Rate) 을 음성인식 API별로 측정한 리포지토리
https://github.com/rtzr/Awesome-Korean-Speech-Recognition?tab=readme-ov-file


한국전자통신연구원 ETRI의 공공 인공지능오픈 API
https://aiopen.etri.re.kr/

20초짜리 하루 1000건 요청 가능(약 55시간분량)
데이터 수집하는지 검증 못함

직접 한국어모델 개발하는 경우에 쓸만한 교육데이터를 제공하고 있음


speech-recognition 안전한가? => 쓰레기
https://voicepower.co.uk/is-speech-recognition-secure/


파이썬 speech-recognition패키지에서 확인된 오프라인 api목록
https://pypi.org/project/SpeechRecognition/

- CMU Sphinx (works offline) << 한국어모델 공식지원 없음, 커뮤니티모델 못찾음
- Snowboy Hotword Detection (works offline) << 사용목적에 맞지 않음
- Vosk API (works offline)
- OpenAI whisper (works offline)

블로그 vosk & openai whisper 예제
https://devskim.tistory.com/60

openai whisper 시도
https://github.com/openai/whisper

whisper의 의존성인 triton이 윈도우에서 실행불가능하다는 의견
https://stackoverflow.com/questions/76327878/python-poetry-fails-to-add-openai-whisper-due-to-triton-installation-error

wsl설치해서 프로젝트 진행

pyenv 설치
curl https://pyenv.run | bash

sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

ffmpeg 설치필요
sudo apt update && sudo apt install ffmpeg    # on Ubuntu or Debian



---

```
poetry shell
poetry add fastapi uvicorn[standard]
poetry run uvicorn src.app:app --reload

poetry run uvicorn src.app:app  # 프로덕션 실행 시(실제로는 gunicorn에 올려야 함)

poetry run uvicorn src.app:app --host 0.0.0.0   # 도커사용시

docker run -d -p 8000:8000 sample
docker run -p 8000:8000 태그이름 << 포어그라운드 실행
```


```
npm create vite@latest frontend
cd frontend
npm install
npm run dev
npm run build

server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true
    }
  }
}
```

tailwind 설치
daisyui 설치

---

[TODOS] 할일

(프론트)
+확장자 mp3, wav 제한
+로딩UI, 폼 프리징
+설명문
+스타일적용
+클릭하여 클립보드 복사
+문장 분리
500에러 처리

(백)
+확장자에 따른 포멧변환
+파일구조 모듈화
+성능(속도, 정확도) 및 용량 최적화 전략 확인
500에러 처리

(배포)
도커파일로 이미지 생성
배포전략 고민
엔드유저쪽에서 도커설치 및 실행 스크립트
