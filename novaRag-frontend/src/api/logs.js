import mockLogs from '@/mock/logs.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Logs service
 *
 * logs/attack_log.jsonl is written directly to disk by executor.py. A
 * browser can't read local files, so no endpoint exists yet to serve it.
 * Once the backend exposes one, replace the `throw` with the real GET call.
 */
export async function getAttackLogs() {
  if (USE_MOCK_DATA) {
    await simulateLatency()
    return mockLogs
  }
  // TODO: Connect to attack_log.jsonl endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}