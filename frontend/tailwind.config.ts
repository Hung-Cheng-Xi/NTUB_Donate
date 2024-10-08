import type { Config } from 'tailwindcss';

export default {
  content: [
    './app/admin/src/**/*.{js,jsx,ts,tsx}',
    './app/client/src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        button: {
          darkblue: '#0C2D65',
          gray: '#F5F5F5',
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
