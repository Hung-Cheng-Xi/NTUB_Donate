import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
    base: '/client/',
    root: "app/client",
    plugins: [react()],
    server: {
        proxy: {
            '/api/client/': {
                target: 'http://120.97.28.11:8081/',
                changeOrigin: true,
            },
        },
    },
})
