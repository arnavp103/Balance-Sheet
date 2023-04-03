<template>
    <main class="flex flex-col min-h-screen font-Outfit dark:bg-dprimary bg-primary">
      <SiteNavigation v-if="loggedIn"/>
      <RouterView />
    </main>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import { ref } from 'vue'
import SiteNavigation from './components/SiteNavigation.vue'

const loggedIn = ref(true)
</script>

<style>
* {
  color: #32292F;
}

@media (prefers-color-scheme: dark) {
  * {
    color: #CDFDF0
  }
}
</style>