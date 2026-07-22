import { ref, watch } from 'vue'

const STORAGE_KEY = 'novarag:sidebar-collapsed'

// Module-level state so every component sharing this composable reads the
// same collapsed/expanded value (Sidebar toggles it, MainLayout reads it for
// content offset) without prop-drilling or a full Pinia store.
const collapsed = ref(localStorage.getItem(STORAGE_KEY) === 'true')

watch(collapsed, (val) => {
  localStorage.setItem(STORAGE_KEY, String(val))
})

export function useSidebar() {
  function toggle() {
    collapsed.value = !collapsed.value
  }
  return { collapsed, toggle }
}