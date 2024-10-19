import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

// https://vitejs.dev/config/
export default defineConfig({
  base: '/admin/',
  root: 'app/admin',
  plugins: [react()],
  server: {
    proxy: {
      '/admin/api/': {
        // target: 'http://120.97.28.11:8081/',
        target: process.env.VITE_API_BASE_URL, // 使用 .env 中設置的 API 基本 URL,
        changeOrigin: true,
      },
    },
  },
});
