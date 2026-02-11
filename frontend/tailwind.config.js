/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'pastel-purple': '#F3E5F5',
        'pastel-blue': '#E1F5FE',
        'pastel-pink': '#FCE4EC',
        'pastel-green': '#E8F5E9',
        'pastel-yellow': '#FFF9C4',
      },
    },
  },
  plugins: [],
}
