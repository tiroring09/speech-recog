from fastapi import FastAPI, APIRouter, File, UploadFile
from typing import List

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
router = APIRouter()


app.mount('/assets', StaticFiles(directory='frontend/dist/assets'))

@app.get('/')
def index():
  return FileResponse('frontend/dist/index.html')

@app.get('/favicon.ico')
def favicon():
  return FileResponse('frontend/dist/favicon.ico')


@app.get('/api/hello')
def hello():
  return {'Hello': 'world'}

@app.post('/api/files')
def speech_to_text(files: List[UploadFile] = File(...)):
  for file in files:
    print(file.filename)
    print(file.file)
  return { 'fileNames': [ file.filename for file in files ] }

@app.post('/api/stt')
def speech_to_text(file: UploadFile = File(...)):
  print('/api/stt called: ', file.filename)
  # print(file.filename)
  # print(file.file)

  format = file.filename.split('.')[-1].lower()

  # 2) whisper제공 api 사용한 코드
  # text = convert_whisper(file.file)

  # 1) 최초 speech-recognition패키지사용한 코드
  if format == 'mp3':
    wav = convert_mp3_to_wav(file.file)
    text = convert_audio_to_text(wav)
  else:
    text = convert_audio_to_text(file.file)
  
  # print(text)
  return { 'fileName': file.filename, 'text': text }







import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file):
  audio = AudioSegment.from_file(mp3_file, format='mp3')
  return audio.export(format='wav')
  # return audio.export('example', format='wav')
  # return audio.raw_data

def convert_mp3_to_wav1(mp3_file_path):
  audio = AudioSegment.from_mp3(mp3_file_path)
  wav_file_path = mp3_file_path.replace(".mp3", ".wav")
  audio.export(wav_file_path, format="wav")
  return wav_file_path

def convert_audio_to_text(audio_file_path):
  print('convert_audio_to_text called')
  recognizer = sr.Recognizer()
  with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)
    try:
      # Google API를 사용하는 경우, 아래 코드의 주석을 해제하세요.
      # text = recognizer.recognize_google(audio_data, language='ko-KR')

      # 오프라인에서 동작하는 Sphinx 사용
      # text = recognizer.recognize_sphinx(audio_data, language='ko-KR')
      # text = recognizer.recognize_sphinx(audio_data)

      # openai의 whispher사용(오프라인가능)
      text = recognizer.recognize_whisper(audio_data, language='ko')
    except sr.UnknownValueError as e :
      text = f"음성 인식을 할 수 없습니다. {e}"
    except sr.RequestError as e:
      text = f"요청에 실패했습니다; {e}"
  return text





import whisper

def convert_whisper(audio_file):
  print('convert_whisper called')
  model = whisper.load_model('base')
  result = model.transcribe('example.wav')
  return result['text']