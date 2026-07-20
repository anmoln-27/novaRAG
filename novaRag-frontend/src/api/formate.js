export function formatRelativeTime(isoString) {
  if (!isoString) return '—'
  const date = new Date(isoString)
  const diffSeconds = Math.round((date - new Date()) / 1000)
  const divisions = [
    { amount: 60, unit: 'seconds' },
    { amount: 60, unit: 'minutes' },
    { amount: 24, unit: 'hours' },
    { amount: 7, unit: 'days' },
    { amount: 4.34524, unit: 'weeks' },
    { amount: 12, unit: 'months' },
    { amount: Infinity, unit: 'years' },
  ]
  const rtf = new Intl.RelativeTimeFormat('en', { numeric: 'auto' })
  let duration = diffSeconds
  for (const division of divisions) {
    if (Math.abs(duration) < division.amount) {
      return rtf.format(Math.round(duration), division.unit)
    }
    duration /= division.amount
  }
}

export function formatResponseTime(seconds) {
  if (seconds == null) return '—'
  if (seconds < 1) return `${Math.round(seconds * 1000)}ms`
  return `${seconds.toFixed(2)}s`
}

export function formatClockTime(date = new Date()) {
  return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
}

export function prettyJson(value) {
  return JSON.stringify(value, null, 2)
}