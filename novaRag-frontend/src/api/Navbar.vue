<script setup>
// Minimal top bar: current target, connection status dots, live clock, theme
// toggle. Deliberately no search bar, no notification bell — nothing that
// competes with the sidebar for navigation duties.
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useClock } from '@/composables/useClock'
import { useSystemStatus } from '@/composables/useSystemStatus'
import { useTheme } from '@/composables/useTheme'
import { formatClockTime } from '@/utils/format'
import StatusBadge from '@/components/common/StatusBadge.vue'

const route = useRoute()
const { now } = useClock()
const { targetAppOnline, geminiStatus, targetUrl } = useSystemStatus()
const { isDark, toggle: toggleTheme } = useTheme()

const pageTitle = computed(() => route.meta.title || 'novaRAG')

const targetStatusValue = computed(() => {
  if (targetAppOnline.value === null) return 'unknown'
  return targetAppOnline.value ? 'online' : 'offline'
})
</script>

<template>
  <header class="h-16 border-b border-border bg-surface/80 backdrop-blur-sm sticky top-0 z-40 flex items-center px-6 gap-6">
    <h1 class="font-display text-[15px] font-semibold text-ink shrink-0">{{ pageTitle }}</h1>

    <div class="h-5 w-px bg-border shrink-0" />

    <!-- Current target -->
    <div class="flex items-center gap-2 text-sm text-ink-soft min-w-0">
      <i class="pi pi-server text-[13px] shrink-0" />
      <span class="font-mono text-xs truncate">{{ targetUrl }}</span>
    </div>

    <div class="flex-1" />

    <!-- Status cluster -->
    <div class="flex items-center gap-4 shrink-0">
      <div class="flex items-center gap-1.5" title="FastAPI target application">
        <StatusBadge kind="status" :value="targetStatusValue" dot-only />
        <span class="text-xs text-ink-soft hidden sm:inline">FastAPI</span>
      </div>
      <div class="flex items-center gap-1.5" title="Gemini API quota status">
        <StatusBadge kind="status" :value="geminiStatus" dot-only />
        <span class="text-xs text-ink-soft hidden sm:inline">Gemini</span>
      </div>

      <div class="h-5 w-px bg-border" />

      <!-- Clock -->
      <div class="flex items-center gap-1.5 text-xs text-ink-soft font-mono tabular-nums">
        <i class="pi pi-clock text-[12px]" />
        {{ formatClockTime(now) }}
      </div>

      <!-- Theme toggle -->
      <button
        type="button"
        class="h-8 w-8 rounded-[9px] flex items-center justify-center text-ink-soft hover:bg-bg-secondary hover:text-ink transition-colors duration-150"
        :title="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
        @click="toggleTheme"
      >
        <i :class="['pi', isDark ? 'pi-sun' : 'pi-moon', 'text-[14px]']" />
      </button>
    </div>
  </header>
</template>
