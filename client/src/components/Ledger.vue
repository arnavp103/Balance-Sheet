<template>
	<div class="min-h-full min-w-full flex flex-row flex-nowrap">

		<div name="" id="" 
		class="min-h-full bg-debit d-flex flex-1 text-neutral-900 font-mono
		resize-none px-2 focus:outline-none" height="300">
			<form class="bg-primary rounded d-flex flex-grow-1 mt-5 p-5">
				<h2 class="text-2xl font-bold text-center pb-2">Debit</h2>
				<br>
					<label :for="deb_amount">Amount: $ </label>
					<input v-model="deb_amount" placeholder="0.00" id="deb_amount" type="number">
					<br><br>
					<label :for="deb_date">Date: </label>
					<input v-model="deb_date" placeholder="" id="deb_date" type="date">
					<br><br>
					<label :for="deb_reason">Reason: </label>
					<input v-model="deb_reason" placeholder="(optional)" id="deb_reason" type="text">
					<br><br>
					<button @click="clearDeb()"
					class="rounded p-1 bg-red-500 text-white">
						Clear
					</button>
					<button variant="outline-debit" @click="onDebSubmit"
					class="rounded p-1 bg-green-500 text-white float-right">
						Submit
					</button>
			</form>
			<div id="deb-space" class="scrollable d-flex flex-grow-1 overflow-auto display">
				<div v-for="deb in deb_list" :key="deb.id" class="bg-white m-3 rounded p-1">
					Date: {{ deb.date }}<br>
					Amount: ${{ deb.amount_dollars + deb.amount_cents / 100.00 }}<br>
					Reason: {{ deb.reason }}<br>
				</div>
			</div>
		</div>

		<!-- Separator -->
		<div class="h-full min-h-full bg-primary dark:bg-dprimary flex flex-col px-2">
		</div>

		<div name="" id=""
		class="min-h-full  bg-credit flex-1 text-neutral-900 font-mono
		resize-none px-2 focus:outline-none">
			<form class="bg-primary rounded d-flex flex-grow-1 mt-5 p-5">
				<h2 class="text-2xl font-bold text-center pb-2">Credit</h2>
				<br>
					<label :for="cred_amount">Amount: $ </label>
					<input v-model="cred_amount" placeholder="0.00" id="cred_amount" type="number">
					<br><br>
					<label :for="cred_date">Date: </label>
					<input v-model="cred_date" placeholder="" id="cred_date" type="date">
					<br><br>
					<label :for="cred_reason">Reason: </label>
					<input v-model="cred_reason" placeholder="(optional)" id="cred_reason" type="text">
					<br><br>
					<button @click="clearCred()"
					class="rounded p-1 bg-red-500 text-white">
						Clear
					</button>
					<button variant="outline-debit" @click="onCredSubmit"
					class="rounded p-1 bg-green-500 text-white float-right">
						Submit
					</button>
			</form>
			<div id="cred-space" class="scrollable d-flex flex-grow-1 overflow-auto display">
				<div v-for="cred in cred_list" :key="cred.id" class="bg-white m-3 rounded p-1">
					Date: {{ cred.date }}<br>
					Amount: ${{ cred.amount_dollars + cred.amount_cents / 100.00 }}<br>
					Reason: {{ cred.reason }}<br>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { onBeforeUpdate, onMounted, ref } from 'vue';
// import router from '../router/index'
import axios from 'axios';

const deb_amount = ref("");
const deb_date = ref("");
const deb_reason = ref("");
const cred_amount = ref("");
const cred_date = ref("");
const cred_reason = ref("");

var deb_list: any;
var cred_list: any;

type Transaction = {
	date: string;
	amount_dollars: number;
	amount_cents: number;
	reason: string;
	user_id: number;
	debcred: number;
};

type TransactionsList = {
  data: Transaction[];
};


function getTransactions() {
	const newJSON: any = sessionStorage.getItem("currUser");
	const currUser: any = JSON.parse(newJSON);
	const path = 'http://localhost:5000/api/debcred/' + currUser.id;
	axios.get(path)
	.then ((result) => {
		let trans_obj = JSON.stringify(result.data);
		let trans_list = JSON.parse(trans_obj);
		deb_list = trans_list[0];
		cred_list = trans_list[1];
		console.log(deb_list);
		console.log(cred_list);
	})
	.catch ((err) => {
		console.error(err);
	});
}

onMounted(async () => {
	getTransactions(); // Fetch data from server
})

onBeforeUpdate(async () => {
	getTransactions(); // Fetch data from server
})

// Adds a v-card to cred-space
// function addCredCard(amount_val: number, date: string, reason: string) {
// 	document.getElementById("cred-space");

// }

function clearDeb() {
	deb_amount.value = "";
	deb_date.value = "";
	deb_reason.value = "";
}


function onDebSubmit(e: any) {
	e.preventDefault();
	const newJSON: any = sessionStorage.getItem("currUser");
	const currUser: any = JSON.parse(newJSON);
	var amount_val = parseFloat(deb_amount.value);
	var dollars = Math.floor(amount_val);
	var cents = Math.round((amount_val - dollars) * 100);
	console.log(cred_date.value);
	console.log(cred_reason.value);
	const payload: Transaction = {
		amount_dollars: dollars,
		amount_cents : cents,
		date: deb_date.value,
		reason : deb_reason.value,
		user_id: currUser.id,
		debcred: 0
	};
	console.log(payload);
	clearDeb();
	submitTransaction(payload);
}


function clearCred() {
	cred_amount.value = "";
	cred_date.value = "";
	cred_reason.value = "";
}


function onCredSubmit(e: any) {
	e.preventDefault();
	const newJSON: any = sessionStorage.getItem("currUser");
	const currUser: any = JSON.parse(newJSON);
	var amount_val = parseFloat(cred_amount.value);
	var dollars = Math.floor(amount_val);
	var cents = Math.round((amount_val - dollars) * 100);
	const payload: Transaction = {
		amount_dollars: dollars,
		amount_cents : cents,
		date: cred_date.value,
		reason : cred_reason.value,
		user_id: 1,
		debcred: 1
	};
	console.log(payload);	
	clearCred();
	// addCred();
	submitTransaction(payload);
}


function submitTransaction(payload: any) {
	const newJSON: any = sessionStorage.getItem("currUser");
	const currUser: any = JSON.parse(newJSON);
	const path = 'http://localhost:5000/api/debcred';
	axios.post(path, payload)
	.then ((res) => {
		console.log(res.data)
	})	
	.catch ((err) => {
		console.error(err);
	});
}


</script>

<style>
.display {
	height: 49%;
}
.card {
	height: 25%;
}
</style>