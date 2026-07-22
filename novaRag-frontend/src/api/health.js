import apiClient from './client'
import mockHealth from '@/mock/health.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Health service
 *
 * `checkTargetAppHealth` uses the one real, documented endpoint (GET /) as a
 * lightweight reachability check for the FastAPI target application.
 *
 * `getSystemHealth` (Gemini quota, orchestrator status, attack count) has no
 * backend endpoint yet. In mock mode it returns fixture data; once a real
 * endpoint exists, replace the `throw` below with the real GET call — no
 * caller needs to change.
 */
export async function checkTargetAppHealth() {
  if (USE_MOCK_DATA) {
    await simulateLatency(150)
    return { online: mockHealth.target_app_status === 'online', latencyMs: 12 }
  }
  try {
    const start = performance.now()
    await apiClient.get('/')
    return { online: true, latencyMs: Math.round(performance.now() - start) }
  } catch (err) {
    return { online: false, latencyMs: null, error: err.message }
  }
}

export async function getSystemHealth() {
  if (USE_MOCK_DATA) {
    await simulateLatency(150)
    return mockHealth
  }
  // TODO: Connect to orchestrator health endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}