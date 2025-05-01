// vite.config.js
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  base: '/',  // <--- ROOT. Because it's at mcweaponry.spinnycat.com/
  plugins: [svelte()],
});
