import { defineStore } from 'pinia'
import { ref,reactive, createApp } from "vue"
import { onMounted, onRenderTriggered } from "vue"

import {useRouter } from 'vue-router'
export const useLoginStore = defineStore('Loginuser',() => {
     const showlogout = ref(false)
     const router = useRouter()
      function getCookie(name) {
      const cookie = `; ${document.cookie}`;
      const parts = cookie.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
 
    function loginusername(){
    const requestOptions = {
        method: "POST",
        headers: { 
        'Content-Type': 'application/json' ,
        'X-CSRF-TOKEN': getCookie('csrf_access_token')},
      };
      fetch('api/username', requestOptions)
      .then(data => {if(data ===  false){ window.alert("signup or check email")}
   
      else{console.log(data); 
      showlogout.value = true;

 }}) 
    }
   
  return { showlogout, loginusername} 
})