<template>
  <div class="m-auto pb-14 flex flex-col justify-center">
    <LoginBox :signup="signup" @change-login="toggleSignup"/>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import LoginBox from '../components/LoginBox.vue'
let signup = ref(false)
const toggleSignup = () => {
  signup.value = !signup.value
}
</script>
