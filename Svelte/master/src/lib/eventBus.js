// src/lib/eventBus.js
import { writable } from 'svelte/store';

// Create an event store
export const themeChangeEvent = writable(null);

// Function to trigger the theme change event
export function triggerThemeChange(newTheme) {
  themeChangeEvent.set(newTheme);
}
