<script setup>
// Reusable premium card surface. Every KPI card, table wrapper, and panel
// in the app should compose this rather than repeating border/radius/shadow
// classes locally.
defineProps({
  padded: { type: Boolean, default: true },
  hoverLift: { type: Boolean, default: false },
})
</script>

<template>
  <div
    class="surface-card transition-all duration-300 ease-elegant"
    :class="[padded ? 'p-6' : '', hoverLift ? 'hover:-translate-y-0.5 hover:shadow-elevated' : 'shadow-soft']"
  >
    <slot />
  </div>
</template>
