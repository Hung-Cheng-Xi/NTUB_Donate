import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

// https://vitejs.dev/config/
export default defineConfig({
  base: '/admin/',
  root: 'app/admin',
  plugins: [react()],
  server: {
    proxy: {
      '/api/admin': {
        target: 'http://120.97.28.11:8081/',
        changeOrigin: true,
      },
    },
  },
});
