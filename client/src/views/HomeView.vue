

<template>
  <div class="flex flex-col min-h-full min-w-full">
    <div class="editors flex flex-row flex-nowrap min-h-full min-w-full flex-1">
      <Ledger />
    </div>
    <Report />
  </div>
</template>


<script setup lang="ts">
import Report from '../components/Report.vue';
import Ledger from '../components/Ledger.vue';
import { ref } from 'vue';
</script>
