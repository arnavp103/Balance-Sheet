<template>
  <section class="border-2 rounded border-secondary dark:border-dsecondary transition-all duration-150 ease-in-out max-w-fit p-4">
	<h2 class="text-2xl font-bold text-center pb-2">Login</h2>
	<form class="flex flex-col items-center min-w-full space-y-4" @submit.prevent="submit">
		<div class="flex flex-row justify-between flex-wrap md:flex-nowrap items-center mx-2 min-w-full ">
			<label for="email" class="text-sm">Email</label>
			<input
				type="email"
				id="email"
				name="email"
				v-model="email"
				class="border border-gray-300 rounded-md p-2 text-dprimary grow-0 justify-end"
			/>
		</div>

		<div class="flex flex-row justify-between flex-wrap md:flex-nowrap items-center mx-2 min-w-full">
			<label for="password" class="text-sm">Password</label>
			<input
				type="password"
				id="password"
				name="password"
				v-model="password"
				class="border border-gray-300 rounded-md p-2 text-dprimary grow-0 justify-end"
			/>
		</div>

		<div v-show="signup" class="flex flex-row justify-between flex-wrap md:flex-nowrap items-center mx-2 transition-all duration-150 ease-in-out min-w-full">
			<label for="password" v-bind:class="{'text-red-500': !matchingPasswords()}" class="text-sm">Confirm Password</label>
			<input
				type="password"
				id="confirmPassword"
				name="confirmPassword"
				v-model="confirmPassword"
				v-bind:class="{'border-red-500': !matchingPasswords()}"
				class="border border-gray-300 rounded-md p-2 text-dprimary grow-0 justify-end"
			/>
		</div>
		<p v-show="passwordHint" class="text-center text-sm md-2 text-red-500">
		Your passwords don't match</p>
	  	<button type="submit" class="bg-secondary dark:bg-dsecondary text-white rounded-md p-2 mt-4">Submit</button>
	</form>
  </section>
  <p class="text-center text-sm mt-4 text-secondary underline ">
	<span v-if="!signup" @click="$emit('change-login')" class="cursor-pointer">Don't have an account?</span>
	<span v-else @click="$emit('change-login')" class="cursor-pointer">Already have an account?</span>
  </p>
</template>

<script setup lang="ts">
import { ref } from 'vue';

defineEmits<{
	"change-login": () => void
}>()

defineProps<{
	signup: boolean
}>()

let email = ref("");
let password = ref("");
let confirmPassword = ref("");

let passwordHint = ref(false);

function submit() {
	email.value = "";
	if (!matchingPasswords()) {
		passwordHint.value = true;
		return;
	}
	passwordHint.value = false;

}

function matchingPasswords():boolean {
	return password.value === confirmPassword.value
}
</script>