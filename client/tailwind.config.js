/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
		colors: {
			primary: "#EDEDF4",
			secondary: "#779FA1",
			dprimary: "#32292F",
			dsecondary: "#2B3A67",
			debit: "#50B2B3",
			credit: "#E54B4B",
		}
	},
    fontFamily: {
      Outfit: ['Outfit, sans-serif'],
	  mono: ['Roboto Mono, monospace']
    },
    container: {
      padding: '2rem',
      center: true
    }
  },
  plugins: []
}
