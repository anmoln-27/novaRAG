<script setup>
// Single badge component for both severity (Critical/High/Medium/Low) and
// connection status (online/offline/degraded) — Dashboard, Reports, Logs,
// and Navbar all use this instead of ad-hoc colored spans.
import { computed } from 'vue'
import { getSeverityToken, getStatusToken } from '@/utils/severity'

const props = defineProps({
  kind: { type: String, default: 'severity' }, // severity | status
  value: { type: String, required: true },
  dotOnly: { type: Boolean, default: false },
})

const token = computed(() =>
  props.kind === 'status' ? getStatusToken(props.value) : getSeverityToken(props.value)
)
</script>

<template>
  <span
    v-if="dotOnly"
    class="inline-block h-2 w-2 rounded-full shrink-0"
    :style="{ backgroundColor: token.color }"
    :title="token.label"
  />
  <span
    v-else
    class="inline-flex items-center gap-1.5 rounded-pill px-2.5 py-1 text-xs font-semibold"
    :style="{ color: token.color, backgroundColor: token.bg }"
  >
    <i v-if="token.icon" :class="['pi', token.icon, 'text-[11px]']" />
    {{ token.label }}
  </span>
</template>
