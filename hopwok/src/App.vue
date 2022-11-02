<script setup>
import { RouterLink, RouterView,useRouter } from 'vue-router'
import {ref, onMounted } from 'vue';

import { useProductStore } from "@/stores/productCart"
import { storeToRefs } from 'pinia';
import HelloWorld from './components/HelloWorld.vue'
import { useLoginStore } from "@/stores/LoginStore"
const router = useRouter()

const Loginuser = useLoginStore();
const product = useProductStore();
const { carts } = storeToRefs(product); 
  
</script> 
<template>
  <div>
<header>
    <div class="navigation-bar">
     <HelloWorld msg="ungenericmart" />
    <div id ="menu dev">
       <nav >
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/products">Products</RouterLink>
        <RouterLink to="/cart">cart</RouterLink>
        <button  v-if = "!Loginuser.showlogout" class ="button" @click='$router.push({name: "login"})'> login </button>
        <button  v-if = "!Loginuser.showlogout" class ="button2" @click='$router.push({name: "signup"})'> sign up </button>
  
        <button  v-if = "Loginuser.showlogout" class ="button3" @click='$router.push({name: "logout"})'> logout </button>
            
      </nav>
      <div class = "cc"><img class ="cart" src =  "/public/shopp.png"  alt="-" /><p class = "cartcount">{{carts.data.count}}</p> </div>
    </div>
    </div>
</header>

 

<RouterView/>

</div>
</template>
  
  




<style scoped>
 @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
* {
  box-sizing: border-box;
}


*{
  font-family: 'Poppins', sans-serif;
}
header {
  overflow: hidden;
  background-color: #d9d9d9;
  line-height: .5;
  max-height: 100vh;
  
}
  
  .logo {
  
    margin: 0 auto 2rem 0;
    width: 5%;
    top :-15px;left:-70px;
  }
  
  nav {
    color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;
  }
  
  nav a.router-link-exact-active {
    color: var(--color-text);
  }
  
  nav a.router-link-exact-active:hover {
    background-color: transparent;
  }
  
  nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
  }
  
  nav a:first-of-type {
    border: 0;
  }
  .button{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  left:760px;
  top:-70px;
  font-weight: 600;
  color: rgb(255, 255, 255);
  border-radius: 8px;

  

}
.button2{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #13abd5;
  margin-left: 10px;
  left:760px;
  top:-70px;
  font-weight: 600;
  color: rgb(255, 254, 254);
  border-radius: 8px;

  

}
.button3{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #d54713;
  margin-left: 10px;
  left:760px;
  top:-70px;
  font-weight: 600;
  color: rgb(255, 254, 254);
  border-radius: 8px;

  

}
  @media (min-width: 1024px) {
    header {
      
      place-items: center;
    
    }
  
    .logo {
      margin: 0 2rem -10 0;
    }
  
 
  
    nav {
      text-align: left;
      margin-left: -1rem;
      font-size: 1rem;
  
      padding: 1rem 0;
      margin-top: 1rem;
    }
  }
  .cc{
  position: relative;
  left:1240px;
  top:-60px;
  width:90%;
}
.cart{
  position: relative;
  left:10px;
  width:3%;
  transform: rotate(-0.0turn);
  

} 
.cartcount{
  position: relative;
  font-family: 'Poppins', sans-serif;
  border-radius: 20%;
        width: 20px;
        height: 20px;
      
        background: rgb(230, 206, 20);
        border: 3px solid rgb(23, 5, 105);
        color: rgb(159, 78, 78);
        text-align:center;
        font-weight: 600;
  font-size: 15px;
  left:40px;
  top:-60px;
}

  </style>
  