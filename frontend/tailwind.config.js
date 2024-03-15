/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#131517',
        shade: '#1E1F25',
        grayshade: '#292732',
        secondary: ''
      }
    },
  },
  plugins: [],
}