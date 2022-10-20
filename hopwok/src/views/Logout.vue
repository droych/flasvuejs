<script setup>
import TryComp from '@/components/TryComp.vue';
import Loginview from '../components/Loginview.vue';
import LogoutUser from '../components/LogoutUser.vue';
</script>
<template>
    <div > 
   <LogoutUser />
    </div>
</template>
   
  
<style>

  @media (min-width: 1024px) {
    .products {
      min-height: 20vh;
      position: relative;
      left: -250px; top: -250px;
      display: flex;
      align-items: center;
    }
  }
</style>
  