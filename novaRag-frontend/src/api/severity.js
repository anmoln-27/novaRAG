// Central mapping from backend severity/status strings to design tokens.
// Every page that renders a severity badge or status dot imports from here
// instead of re-deciding colors locally.

export const SEVERITY_TOKENS = {
  Critical: { color: '#C53030', bg: '#FBEAEA', icon: 'pi-exclamation-triangle', label: 'Critical' },
  High: { color: '#C53030', bg: '#FBEAEA', icon: 'pi-exclamation-triangle', label: 'High' },
  Medium: { color: '#D69E2E', bg: '#FCF3E3', icon: 'pi-exclamation-circle', label: 'Medium' },
  Low: { color: '#6F6F6F', bg: '#F3E7E1', icon: 'pi-info-circle', label: 'Low' },
  None: { color: '#2F855A', bg: '#EAF6EF', icon: 'pi-check-circle', label: 'No finding' },
}

export function getSeverityToken(severity) {
  return SEVERITY_TOKENS[severity] || SEVERITY_TOKENS.None
}

export const STATUS_TOKENS = {
  online: { color: '#2F855A', bg: '#EAF6EF', label: 'Online' },
  offline: { color: '#C53030', bg: '#FBEAEA', label: 'Offline' },
  degraded: { color: '#D69E2E', bg: '#FCF3E3', label: 'Degraded' },
  ok: { color: '#2F855A', bg: '#EAF6EF', label: 'Operational' },
  quota_exceeded: { color: '#D69E2E', bg: '#FCF3E3', label: 'Quota exceeded' },
  unknown: { color: '#6F6F6F', bg: '#F3E7E1', label: 'Unknown' },
}

export function getStatusToken(status) {
  return STATUS_TOKENS[status] || STATUS_TOKENS.unknown
}

export function httpStatusTone(statusCode) {
  if (!statusCode) return STATUS_TOKENS.unknown
  if (statusCode < 300) return STATUS_TOKENS.online
  if (statusCode < 500) return STATUS_TOKENS.degraded
  return STATUS_TOKENS.offline
}