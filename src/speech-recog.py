import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    wav_file_path = mp3_file_path.replace(".mp3", ".wav")
    audio.export(wav_file_path, format="wav")
    return wav_file_path


def convert_audio_to_text(audio_file_path):
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
        except sr.UnknownValueError:
            text = "음성 인식을 할 수 없습니다."
        except sr.RequestError as e:
            text = f"요청에 실패했습니다; {e}"
    return text


# import os
# print(f'현재경로: {os.getcwd()}')

# wav = convert_mp3_to_wav('example.mp3')
if __name__ == '__main__':
    text = convert_audio_to_text('example.wav')
    print(text)

# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(text)