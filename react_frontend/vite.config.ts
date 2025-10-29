import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

// PUBLIC_INTERFACE
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    plugins: [react()],
    server: {
      port: 3000,
      strictPort: true
    },
    preview: {
      port: 3000,
      strictPort: true
    },
    define: {
      __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
      __API_BASE_URL__: JSON.stringify(env.VITE_API_BASE_URL || ''),
      __WS_BASE_URL__: JSON.stringify(env.VITE_WS_BASE_URL || '')
    }
  };
});
