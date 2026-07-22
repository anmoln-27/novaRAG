import mockAttacks from '@/mock/attack.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Attack pipeline service (Hacker Agent -> Executor -> Critic Agent)
 *
 * No HTTP endpoint exists yet for triggering a single attack run — main.py
 * runs this chain in-process. In mock mode these functions return fixture
 * data shaped exactly like the documented agent outputs, merged. Once the
 * backend exposes a real endpoint, replace the `throw` with the real POST
 * call; no component using this service needs to change.
 */

export async function getRecentAttacks() {
  if (USE_MOCK_DATA) {
    await simulateLatency()
    return mockAttacks
  }
  // TODO: Connect to Executor/Critic history endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}

export async function runAttack({ path, method, fields }) {
  if (USE_MOCK_DATA) {
    await simulateLatency(900) // real run = Gemini call + HTTP request, simulate the wait
    const template = mockAttacks[0]
    return {
      ...template,
      id: `atk_mock_${Date.now()}`,
      timestamp: new Date().toISOString(),
      hacker: { ...template.hacker, endpoint: path, method },
    }
  }
  // TODO: Connect to Hacker Agent -> Executor -> Critic Agent pipeline endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}

export async function runFullPipeline() {
  if (USE_MOCK_DATA) {
    await simulateLatency(1200)
    return mockAttacks
  }
  // TODO: Connect to full-pipeline run endpoint once exposed.
  throw new Error('Backend endpoint not implemented yet.')
}