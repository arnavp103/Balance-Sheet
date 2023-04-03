import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import './assets/index.css'

import './assets/index.css'

const app = createApp(App)
			.use(createPinia())
			.use(router)
			.mount('#app')
