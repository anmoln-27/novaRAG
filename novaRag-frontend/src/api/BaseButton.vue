<script setup>
// Wraps PrimeVue's Button with novaRAG's variant system, so every CTA in the
// app (hero "Run Analysis", table row actions, form submits) looks consistent
// without re-specifying Tailwind classes each time.
import Button from 'primevue/button'

const props = defineProps({
  label: { type: String, default: '' },
  icon: { type: String, default: '' },
  variant: { type: String, default: 'primary' }, // primary | secondary | ghost
  size: { type: String, default: 'default' }, // default | large
  loading: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
})

defineEmits(['click'])

const variantClasses = {
  primary: '!bg-accent !border-accent hover:!bg-accent-soft hover:!border-accent-soft !text-white',
  secondary: '!bg-transparent !border-border !text-ink hover:!bg-bg-secondary',
  ghost: '!bg-transparent !border-transparent !text-accent hover:!bg-pink/30',
}
</script>

<template>
  <Button
    :label="label"
    :icon="icon"
    :loading="loading"
    :disabled="disabled"
    :class="[variantClasses[variant], size === 'large' ? '!px-7 !py-3.5 !text-base' : '!px-5 !py-2.5 !text-sm']"
    class="!font-semibold !rounded-[10px] !transition-all !duration-200 hover:!-translate-y-px active:!translate-y-0"
    @click="$emit('click', $event)"
  >
    <slot />
  </Button>
</template>
