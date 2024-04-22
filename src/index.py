import whisper

def main():
  # print(whisper.available_models())
  model = whisper.load_model('base')
  result = model.transcribe('example.wav')
  print(result['text'])
  return

if __name__ == '__main__':
  main()