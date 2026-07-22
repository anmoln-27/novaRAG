import { ref, onMounted, onUnmounted } from 'vue'

/** Live-updating clock for the Navbar. Ticks once per second, cleans up on unmount. */
export function useClock() {
  const now = ref(new Date())
  let interval = null

  onMounted(() => {
    interval = setInterval(() => {
      now.value = new Date()
    }, 1000)
  })

  onUnmounted(() => {
    if (interval) clearInterval(interval)
  })

  return { now }
}
