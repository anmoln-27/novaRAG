import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'
import 'primeicons/primeicons.css'

import App from './App.vue'
import router from './router'
import novaRagPreset from './styles/primevue-preset'
import './styles/main.css'

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: novaRagPreset,
    options: {
      darkModeSelector: '.dark-mode',
      cssLayer: {
        name: 'primevue',
        order: 'tailwind-base, primevue, tailwind-utilities',
      },
    },
  },
})
app.use(ToastService)

app.mount('#app')