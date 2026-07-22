import mockReport from '@/mock/report.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Reports service
 *
 * No endpoint yet aggregates Critic Agent findings across attack runs.
 * Once the backend exposes one, replace the `throw` with the real GET call.
 */
export async function getVulnerabilityReport() {
  if (USE_MOCK_DATA) {
    await simulateLatency()
    return mockReport
  }
  // TODO: Connect to Critic Agent endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}