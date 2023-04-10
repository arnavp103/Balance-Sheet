
<template>
  <main class="m-auto pt-12 min-h-full min-w-full flex flex-col items-center justify-start">
    <div class="flex flex-col w-3/5 min-h-full h-full gap-12 py-2">
      <div class="container">
        <h2 class="font-semibold text-2xl">You've been with us for {{ days }}</h2>
        <h2 class="font-semibold text-2xl">You've logged {{ amount }} transactions</h2>
      </div>

      <section class="flex flex-col container">
        <p v-if="goal"> Your current spending goal is {goal}.<br/>Would you like to change it? </p>
        <p v-else> You don't have a spending goal set yet!<br/>Would you like to set one up?</p>
        <form @submit.prevent="setGoal" class="flex flex-col items-center min-w-full space-y-4">

        </form>
      </section>

      <section class="flex flex-row gap-8 container justify-evenly flex-grow align-baseline">
        <button @click="Logout" type="submit" class="bg-secondary dark:bg-dsecondary text-white rounded-md p-2 mt-4 w-2/6">Logout</button>
        <button @click="DeleteAccount" type="submit" class="bg-red-600 text-white rounded-md p-2 mt-4 w-2/6">Delete Account</button>
      </section>
    </div>
  </main>
</template>

<script setup lang="ts">
import router from '../router/index'
import { ref } from 'vue';
import axios from 'axios';


const days = ref(0);
const amount = ref(0);

const goal = ref(null);

function getUserInfo() {
    const newJSON: any = sessionStorage.getItem("currUser");
    const currUser: any = JSON.parse(newJSON)
    if (currUser != null) {
        const path = 'http://localhost:5000/settings/' + currUser.email;
        axios.get(path)
        .then ((res) => {
            days.value = res.data.num_days;
            amount.value = res.data.num_transactions;
        })
        .catch ((err) => {
            console.error(err);
        });
    }
    else {
        router.push({ path: 'login' });
    }
}

getUserInfo()

function Logout() {
    sessionStorage.clear();
    router.push({ path: 'login' });
}

function DeleteAccount() {
    const newJSON: any = sessionStorage.getItem("currUser");
    const currUser: any = JSON.parse(newJSON)
    if (currUser != null) {
        const path = 'http://localhost:5000/deleteAccount/' + currUser.email;
        axios.get(path)
        .then ((res) => {
            sessionStorage.clear();
            router.push({ path: 'login' });
        })
        .catch ((err) => {
            console.error(err);
        });
    }
}
function setGoal() {

}
</script>
