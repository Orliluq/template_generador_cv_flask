/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './src/**/*.{html,js}',
  ],
  theme: {
    extend: {
      colors: {
                'primary': '#031b43',
                'primary-dark': '#02122f',
              },
    },
  },
  plugins: [],
};