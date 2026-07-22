<script setup>
// Linear-style icon-first sidebar. Logo at top, nav items in the middle,
// Settings pinned to the bottom on its own — deliberately separated so it
// never scrolls out of reach as more nav items are added.
import { useRoute, RouterLink } from 'vue-router'
import { useSidebar } from '@/composables/useSidebar'

const route = useRoute()
const { collapsed, toggle } = useSidebar()

const navItems = [
  { to: '/dashboard', label: 'Dashboard', icon: 'pi-home' },
  { to: '/explorer', label: 'API Explorer', icon: 'pi-globe' },
  { to: '/console', label: 'Attack Console', icon: 'pi-bolt' },
  { to: '/reports', label: 'Reports', icon: 'pi-shield' },
  { to: '/logs', label: 'Logs', icon: 'pi-history' },
]

const isActive = (to) => route.path.startsWith(to)
</script>

<template>
  <aside
    class="h-screen sticky top-0 flex flex-col border-r border-border bg-surface transition-[width] duration-300 ease-elegant shrink-0"
    :class="collapsed ? 'w-[76px]' : 'w-[248px]'"
  >
    <!-- Logo -->
    <div class="flex items-center h-16 px-4 border-b border-border" :class="collapsed ? 'justify-center' : 'justify-between'">
      <div class="flex items-center gap-2.5 overflow-hidden">
        <div class="h-8 w-8 rounded-[9px] bg-accent flex items-center justify-center shrink-0">
          <i class="pi pi-shield text-white text-sm" />
        </div>
        <span
          v-if="!collapsed"
          class="font-display font-semibold text-[17px] tracking-tight text-ink whitespace-nowrap"
        >
          novaRAG
        </span>
      </div>
    </div>

    <!-- Nav -->
    <nav class="flex-1 py-4 px-3 flex flex-col gap-1">
      <RouterLink
        v-for="item in navItems"
        :key="item.to"
        :to="item.to"
        class="group relative flex items-center gap-3 rounded-[10px] px-3 py-2.5 text-sm font-medium transition-colors duration-150"
        :class="[
          isActive(item.to)
            ? 'bg-pink/40 text-accent'
            : 'text-ink-soft hover:bg-bg-secondary hover:text-ink',
          collapsed ? 'justify-center' : '',
        ]"
      >
        <span
          v-if="isActive(item.to)"
          class="absolute left-0 top-1/2 -translate-y-1/2 h-5 w-[3px] rounded-full bg-accent"
        />
        <i :class="['pi', item.icon, 'text-[15px] shrink-0']" />
        <span v-if="!collapsed" class="whitespace-nowrap">{{ item.label }}</span>

        <!-- Tooltip on hover when collapsed -->
        <span
          v-if="collapsed"
          class="pointer-events-none absolute left-full ml-3 whitespace-nowrap rounded-md bg-ink px-2.5 py-1.5 text-xs font-medium text-bg opacity-0 shadow-elevated transition-opacity duration-150 group-hover:opacity-100 z-50"
        >
          {{ item.label }}
        </span>
      </RouterLink>
    </nav>

    <!-- Settings, pinned bottom -->
    <div class="border-t border-border px-3 py-3 flex flex-col gap-1">
      <RouterLink
        to="/settings"
        class="group relative flex items-center gap-3 rounded-[10px] px-3 py-2.5 text-sm font-medium transition-colors duration-150"
        :class="[
          isActive('/settings') ? 'bg-pink/40 text-accent' : 'text-ink-soft hover:bg-bg-secondary hover:text-ink',
          collapsed ? 'justify-center' : '',
        ]"
      >
        <i class="pi pi-cog text-[15px] shrink-0" />
        <span v-if="!collapsed" class="whitespace-nowrap">Settings</span>
        <span
          v-if="collapsed"
          class="pointer-events-none absolute left-full ml-3 whitespace-nowrap rounded-md bg-ink px-2.5 py-1.5 text-xs font-medium text-bg opacity-0 shadow-elevated transition-opacity duration-150 group-hover:opacity-100 z-50"
        >
          Settings
        </span>
      </RouterLink>

      <button
        type="button"
        class="flex items-center gap-3 rounded-[10px] px-3 py-2.5 text-sm font-medium text-ink-soft hover:bg-bg-secondary hover:text-ink transition-colors duration-150"
        :class="collapsed ? 'justify-center' : ''"
        :title="collapsed ? 'Expand sidebar' : 'Collapse sidebar'"
        @click="toggle"
      >
        <i :class="['pi', collapsed ? 'pi-angle-right' : 'pi-angle-left', 'text-[15px] shrink-0']" />
        <span v-if="!collapsed" class="whitespace-nowrap">Collapse</span>
      </button>
    </div>
  </aside>
</template>
