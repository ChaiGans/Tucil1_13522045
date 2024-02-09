/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        basic: "#D0ED57",
        bgblack: "#0e1111",
      },
      fontFamily: {
        rajdhaniBold: ["Rajdhani-Bold", "sans-serif"],
        rajdhaniLight: ["Rajdhani-Light", "sans-serif"],
        rajdhaniMedium: ["Rajdhani-Medium", "sans-serif"],
        rajdhaniRegular: ["Rajdhani-Regular", "sans-serif"],
        rajdhaniSemiBold: ["Rajdhani-Semibold", "sans-serif"],
      },
    },
  },
  plugins: [],
};

