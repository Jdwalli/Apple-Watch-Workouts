/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "blue-charcoal": {
          50: "#f3f6fc",
          100: "#e6eef8",
          200: "#c8dbef",
          300: "#98bbe1",
          400: "#6198cf",
          500: "#3d7bba",
          600: "#2c629d",
          700: "#254e7f",
          800: "#22436a",
          900: "#213959",
          950: "#0a111b",
        },

        shark: {
          50: "#f5f5f6",
          100: "#e5e5e8",
          200: "#cfd0d2",
          300: "#adaeb3",
          400: "#84858c",
          500: "#696a71",
          600: "#595961",
          700: "#4c4d52",
          800: "#434347",
          900: "#3b3b3e",
          925: "#262626", // Target
          950: "#1c1c1e", // Target
        },

        mirage: {
          50: "#f6f7f9",
          100: "#ebedf3",
          200: "#d3d9e4",
          300: "#acb8cd",
          400: "#7f91b1",
          500: "#5f7498",
          600: "#4b5d7e",
          700: "#3e4b66",
          800: "#364156",
          900: "#30384a",
          950: "#1b1f29", // Target
        },

        purple: {
          50: "#f4f2ff",
          100: "#ebe8ff",
          200: "#d8d4ff",
          300: "#bdb1ff",
          400: "#9c85ff",
          500: "#6e40ff", // Target
          600: "#6c30f7",
          700: "#5e1ee3",
          800: "#4e18bf",
          900: "#41169c",
          950: "#270b6a",
        },

        pink: {
          50: "#fef1fa",
          100: "#fee5f7",
          200: "#feccf0",
          300: "#ff92df", //Target
          400: "#fe68ce",
          500: "#f83cb8",
          600: "#e81a98",
          700: "#ca0c7a",
          800: "#a70d64",
          900: "#8b1055",
          950: "#550231",
        },

        red: {
          50: "#fff0f4",
          100: "#ffe3e9",
          200: "#ffcbda",
          300: "#ffa0ba",
          400: "#ff6b96",
          500: "#fb2a6c", //Target
          600: "#e91563",
          700: "#c50b53",
          800: "#a50c4c",
          900: "#8d0e47",
          950: "#4f0223",
        },

        green: {
          50: "#fdffe4",
          100: "#f8ffc5",
          200: "#efff92",
          300: "#e1ff53",
          400: "#cefb20",
          500: "#c3fa00", // Target
          600: "#88b500",
          700: "#678902",
          800: "#526c08",
          900: "#455b0c",
          950: "#233300",
        },

        blue: {
          50: "#f0f9ff",
          100: "#dff1ff",
          200: "#b1e3ff", // Target
          300: "#79d2ff",
          400: "#32bcfe",
          500: "#07a3f0",
          600: "#0083cd",
          700: "#0067a6",
          800: "#035889",
          900: "#094971",
          950: "#062e4b",
        },
      },
    },
  },
  plugins: [],
};
