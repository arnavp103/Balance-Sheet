<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header class="min-w-full pb-2">
    <nav class="flex flex-col md:flex-row justify-around items-center">
      <RouterLink to="/" class="text-2xl font-bold text-center">Home</RouterLink>
      <RouterLink to="/about" class="text-2xl font-bold text-center">About</RouterLink>
      <RouterLink to="/login" class="text-2xl font-bold text-center">Login</RouterLink>
      <RouterLink to="/register" class="text-2xl font-bold text-center">Register</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

