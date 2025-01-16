import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
    build: {
        manifest: true,
        outDir: '../app/static/react', // Output directory for compiled assets
        emptyOutDir: true,
        rollupOptions: {
            input: './react/studio.jsx', // Use React entry point
        },
    },
    resolve: {
        dedupe: ['react', 'react-dom'],
    },
    optimizeDeps: {
        include: [
            '@fullcalendar/react',
            '@fullcalendar/timegrid',
            '@fullcalendar/google-calendar'
        ]
    }
});
