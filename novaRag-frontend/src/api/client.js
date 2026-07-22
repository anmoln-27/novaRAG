import axios from 'axios'

// Single source of truth for the FastAPI target application's base URL.
// Configurable via .env (VITE_API_BASE_URL) and, later, the Settings page.
const DEFAULT_BASE_URL = 'http://127.0.0.1:8080'

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || DEFAULT_BASE_URL,
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Allows Settings > Backend URL to repoint every service at runtime
// without reloading the app or touching individual service files.
export function setApiBaseUrl(url) {
  apiClient.defaults.baseURL = url
}

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const normalized = {
      message: error.response?.data?.detail || error.message || 'Unknown error contacting backend',
      status: error.response?.status ?? null,
      isNetworkError: !error.response,
      raw: error,
    }
    return Promise.reject(normalized)
  }
)

export default apiClient