import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 5173,
    watch: {
      ignored: ['**/_reference_kigo/**', '**/extracted_kigo/**', '**/imges/**', '**/.git/**']
    }
  }
});
