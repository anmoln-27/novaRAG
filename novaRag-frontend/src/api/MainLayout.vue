<script setup>
// App shell: fixed sidebar, sticky navbar, scrollable content area with a
// subtle fade+rise transition between routes. This is the only place that
// knows both Sidebar and Navbar exist — pages themselves stay unaware of layout.
import { RouterView } from 'vue-router'
import Sidebar from './Sidebar.vue'
import Navbar from './Navbar.vue'
</script>

<template>
  <div class="flex min-h-screen bg-bg">
    <Sidebar />
    <div class="flex-1 flex flex-col min-w-0">
      <Navbar />
      <main class="flex-1">
        <RouterView v-slot="{ Component, route }">
          <Transition name="page-fade" mode="out-in">
            <component :is="Component" :key="route.path" />
          </Transition>
        </RouterView>
      </main>
    </div>
  </div>
</template>

<style scoped>
.page-fade-enter-active,
.page-fade-leave-active {
  transition:
    opacity 220ms var(--ease-elegant, ease),
    transform 220ms var(--ease-elegant, ease);
}
.page-fade-enter-from {
  opacity: 0;
  transform: translateY(6px);
}
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
