import apiClient from './client'
import mockEndpoints from '@/mock/discovery.json'
import { USE_MOCK_DATA, simulateLatency } from '@/mock'

/**
 * Discovery Engine service
 * Backend contract: GET /openapi.json (standard FastAPI-generated schema).
 * This is a REAL, documented endpoint — no placeholder needed once
 * VITE_USE_MOCK_DATA=false and the target app is reachable.
 */

function extractFields(schema, operation) {
  const fields = {}
  const bodyRef =
    operation.requestBody?.content?.['application/json']?.schema?.$ref ||
    operation.requestBody?.content?.['application/json']?.schema?.properties

  if (typeof bodyRef === 'string') {
    const schemaName = bodyRef.split('/').pop()
    const resolved = schema.components?.schemas?.[schemaName]
    if (resolved?.properties) {
      for (const [key, value] of Object.entries(resolved.properties)) {
        fields[key] = value.type || 'string'
      }
    }
  } else if (bodyRef && typeof bodyRef === 'object') {
    for (const [key, value] of Object.entries(bodyRef)) {
      fields[key] = value.type || 'string'
    }
  }

  return fields
}

export async function getDiscoveredEndpoints() {
  if (USE_MOCK_DATA) {
    await simulateLatency()
    return mockEndpoints
  }

  const { data: schema } = await apiClient.get('/openapi.json')
  const endpoints = []

  for (const [path, methods] of Object.entries(schema.paths || {})) {
    for (const [method, operation] of Object.entries(methods)) {
      if (!['get', 'post', 'put', 'patch', 'delete'].includes(method)) continue
      endpoints.push({
        path,
        method: method.toUpperCase(),
        summary: operation.summary || operation.operationId || path,
        fields: extractFields(schema, operation),
      })
    }
  }

  return endpoints
}