<template>
  <header class="sticky top-0 shadow-lg border-b-2 border-secondary dark:border-dsecondary">
	<nav class="container flex flex-row sm:flex-row items-center justify-evenly py-4 min-w-full min-h-full">
		<RouterLink to="/" class="cursor-pointer">
			<span class="text-debit text-2xl font-serif">Balance Sheet</span>
			<i class="text-2xl text-center not-italic px-2 rounded-full cursor-pointer hover:text-white hover:animate-pulse ease-in-out">⚖</i>
		</RouterLink>

		<RouterLink :to="{name: 'settings'}" class="flex gap-3 flex-1 justify-end">
			<i class="text-2xl text-center not-italic px-2 rounded-full cursor-pointer hover:text-white hover:animate-pulse ease-in-out">⚙</i>
		</RouterLink>
	</nav>
  </header>
</template>


<script setup lang="ts">

import { RouterLink } from "vue-router";
</script>