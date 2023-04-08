<template>
	<div class="min-h-full min-w-full flex flex-row flex-nowrap">

		<textarea name="" id="" v-model.trim="debits"
		class="min-h-full bg-debit flex-1 text-neutral-900 font-mono
		resize-none px-2 focus:outline-none"
		>
		</textarea>

		<div class="h-full min-h-full bg-primary dark:bg-dprimary flex flex-col px-2">
			<button class="rounded full bg-blue-950 text-yellow-400">
				17/02/2021
			</button>
		</div>

		<textarea name="" id="" v-model.trim="credits"
		class="min-h-full  bg-credit flex-1 text-neutral-900 font-mono
		resize-none px-2 focus:outline-none"
		>
		</textarea>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const debits = ref('debits...');
const credits = ref('credits...');

</script>
