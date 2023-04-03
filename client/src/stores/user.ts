import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
	state: () => ({
		user: null,
	}),
	actions: {
		async fetchUser() {
			const res = await fetch("https://jsonplaceholder.typicode.com/users/1");
			const user = await res.json();
			this.user = user;
		},

		async signup(email: string, password: string) {
			const res = await fetch("https://jsonplaceholder.typicode.com/users", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					email,
					password,
				}),
			});
			const user = await res.json();
			this.user = user;
		},

		async signIn(email: string, password: string) {
			const res = await fetch("https://jsonplaceholder.typicode.com/users", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					email,
					password,
				}),
			});
			const user = await res.json();
			this.user = user;
		}
	}
});



