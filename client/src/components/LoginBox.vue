<template>
  <section class="border-2 rounded border-secondary dark:border-dsecondary transition-all duration-150 ease-in-out max-w-fit p-4">
	<h2 class="text-2xl font-bold text-center pb-2">Login</h2>
	<form class="flex flex-col items-center min-w-full space-y-4" @submit.prevent="onSubmit">
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
import axios from 'axios';

defineEmits<{
	"change-login": () => void
}>()

const props = defineProps<{
	signup: boolean
}>()

const email = ref("");
const password = ref("");
const confirmPassword = ref("");
let users;

let passwordHint = ref(false);

function getUsers() {
	const path = 'http://localhost:5000/api/login';
	axios.get(path)
	.then ((res) => {
		users = res.data;
	})
	.catch ((err) => {
		console.error(err);
	});
}

function logUser(username: string) {
	const path = 'http://localhost:5000/success/' + username;
	axios.get(path)
	.then ((res) => {
		users = res.data;
		sessionStorage.clear();
		sessionStorage.setItem("currUser", JSON.stringify(users));
	})
	.catch ((err) => {
		console.error(err);
	});
}

function addUser(payload: any) {
	const path = 'http://localhost:5000/api/register';
	axios.post(path, payload)
	.then ((res) => {
		getUsers();
	})
	.catch ((err) => {
		console.error(err);
		console.log(err.message)
		getUsers();
	});
}

function submitLogin(payload: any) {
	const path = 'http://localhost:5000/api/login';
	axios.post(path, payload)
	.then ((res) => {
		logUser(payload['name'])
	})
	.catch ((err) => {
		console.error(err);
		getUsers();
	});
}

function onSubmit(e: any) {
	e.preventDefault();
	if (!matchingPasswords() && props.signup) {
		passwordHint.value = true;
		return;
	}
	passwordHint.value = false;
	const payload = {
		name: email.value.split('@')[0],
		email : email.value,
		password : password.value,
		signup: props.signup
		};
	if (props.signup) {
		addUser(payload)
	}
	else {
		submitLogin(payload)
	}

	console.log("Here is the current user:")
	email.value = "";
	password.value = "";
	confirmPassword.value = "";
}

function matchingPasswords():boolean {
	return password.value === confirmPassword.value
}
</script>