import { ref, watch } from 'vue'

const STORAGE_KEY = 'novarag:theme'
const isDark = ref(localStorage.getItem(STORAGE_KEY) === 'dark')

function apply(val) {
  document.documentElement.classList.toggle('dark-mode', val)
}
apply(isDark.value) // apply immediately on module load, before first paint

watch(isDark, (val) => {
  apply(val)
  localStorage.setItem(STORAGE_KEY, val ? 'dark' : 'light')
})

export function useTheme() {
  function toggle() {
    isDark.value = !isDark.value
  }
  return { isDark, toggle }
}