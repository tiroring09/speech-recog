<template>
  <div class="container m-auto text-center">
    <div class="py-8">

      <h2 class="text-lg font-bold">
        음성변환
      </h2>

      <p class="mt-4 text-gray-500 text-sm">
        <a href="https://openai.com/research/whisper" target="_blank" class="link">Openai Whisper</a>를 사용자 로컬에 직접 설치하여 안전한 음성변환
      </p>

      <div class="my-4">
        <input type="file"
          class="file-input file-input-bordered"
          @change="uploadFile"
          :accept="allowedExtensions.map(x => `.${x}`).join(' ')"
          :disabled="isLoading">
        <p class="text-sm text-gray-500">
          가능한 파일 확장자: {{ allowedExtensions.join(', ') }}<br/>
          ※최초 <a href="https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages" target="_blank" class="link">학습모델</a> 다운로드를 위해 인터넷 연결이 필요합니다.
        </p>
      </div>

      <div>
        <button class="btn"
          @click="submitFile"
          :disabled="isLoading">
          {{ isLoading ? '텍스트 변환중': '텍스트 변환하기' }}
          <span v-if="isLoading" class="loading"></span>
        </button>
      </div>

    </div>
    <hr>
    <div class="py-8">

      <textarea class="textarea textarea-bordered w-2/3 min-h-52"
        placeholder="음성변환한 텍스트"
        :value="translatedText">
      </textarea>

      <div>
        <button class="btn"
          @click="copyToClipboard">
          클립보드에 복사
        </button>
      </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
const toast = useToast()

const selectedFile = ref()
const translatedText = ref('')

const allowedExtensions: string[] = ['mp3', 'wav']
const isLoading = ref(false)

function uploadFile(event: any) {
  selectedFile.value = event.target.files[0]
}

async function submitFile() {
  if (!selectedFile.value) {
    toast.error('파일을 선택해주세요')
    return
  }

  const extension = selectedFile.value?.name.split('.').pop().toLowerCase()

  if (!allowedExtensions.includes(extension)) {
    toast.error(`파일확장자에러(${extension}), 허용된것: ${allowedExtensions}`)
    return
  }

  const formData = new FormData()
  formData.append('file', selectedFile.value)

  isLoading.value = true
  try {
    const { data } = await axios.post('/api/stt', formData)
    translatedText.value = data.text.replaceAll('.', '.\n')
  } catch (error) {
    console.log(error)
    toast.error(`요청 처리 중 에러 발생. (개발자도구 콘솔확인)`)
  }
  isLoading.value = false
  // const { data } = await new Promise(res => 
  //   setTimeout(() => {
  //     res({data: {text: 'asdf'} })
  //   }, 1000)
  // )
}

function copyToClipboard() {
  navigator.clipboard.writeText(translatedText.value)
  toast.success('클립보드에 복사되었습니다')
}
</script>

<style scoped>
</style>
