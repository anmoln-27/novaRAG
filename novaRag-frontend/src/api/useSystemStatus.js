import { ref, onMounted, onUnmounted } from 'vue'
import { checkTargetAppHealth, getSystemHealth } from '@/api/health'

/**
 * Polls target-app + orchestrator health for the Navbar status dots.
 * Both underlying calls already respect VITE_USE_MOCK_DATA â€” this composable
 * doesn't know or care whether it's looking at fixtures or a live backend.
 */
export function useSystemStatus({ pollIntervalMs = 30000 } = {}) {
  const targetAppOnline = ref(null) // null = checking
  const geminiStatus = ref('unknown')
  const attackCount = ref(0)
  const targetUrl = ref(import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8080')
  const loading = ref(true)

  async function refresh() {
    try {
      const [targetHealth, systemHealth] = await Promise.all([
        checkTargetAppHealth(),
        getSystemHealth().catch(() => null),
      ])
      targetAppOnline.value = targetHealth.online
      if (systemHealth) {
        geminiStatus.value = systemHealth.gemini_status
        attackCount.value = systemHealth.attack_count ?? 0
        targetUrl.value = systemHealth.target_url ?? targetUrl.value
      }
    } finally {
      loading.value = false
    }
  }

  let interval = null
  onMounted(() => {
    refresh()
    interval = setInterval(refresh, pollIntervalMs)
  })
  onUnmounted(() => {
    if (interval) clearInterval(interval)
  })

  return { targetAppOnline, geminiStatus, attackCount, targetUrl, loading, refresh }
}