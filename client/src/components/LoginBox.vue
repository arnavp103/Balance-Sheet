<template>
  <section class="border rounded border-slate-600 max-w-fit p-8 bg-slate-800">
	<h2 class="text-2xl font-bold text-center pb-2">Login</h2>
	<form class="flex flex-col items-center">
	  <label for="email" class="text-sm">Email</label>
	  <input
		type="email"
		id="email"
		name="email"
		class="border border-gray-300 rounded-md p-2"
	  />
	  <label for="password" class="text-sm">Password</label>
	  <input
		type="password"
		id="password"
		name="password"
		class="border border-gray-300 rounded-md p-2"
	  />
	  <button class="bg-blue-500 text-white rounded-md p-2 mt-4">Login</button>
	</form>
  </section>
</template>
