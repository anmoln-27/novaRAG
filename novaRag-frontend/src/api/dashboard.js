import mockDashboard from '@/mock/dashboard.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Dashboard summary service
 *
 * No endpoint yet returns precomputed KPIs/timeline for the Dashboard.
 * Once the backend exposes one, replace the `throw` with the real GET call.
 */
export async function getDashboardSummary() {
  if (USE_MOCK_DATA) {
    await simulateLatency()
    return mockDashboard
  }
  // TODO: Connect to a dashboard-summary endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}