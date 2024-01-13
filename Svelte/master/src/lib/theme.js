// src/lib/theme.js
import { writable } from 'svelte/store';

// Initial theme
export const theme = writable();

// Function to update the theme
export function setTheme(newTheme) {
  theme.set(newTheme);
}
