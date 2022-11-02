<script  setup>
import {ref, onMounted } from 'vue';
import LoginVue from '../views/Login.vue';

import {useRouter } from 'vue-router'
const props = defineProps({
       email: {
        type: String,
      },
  
      password:
        {
            type:String
        }
    }) 
function getCookie(name) {
  const cookie = `; ${document.cookie}`;
  const parts = cookie.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
const router = useRouter()
function logout(){
const requestOptions = {
    method: "POST",
    headers: { 
    'Content-Type': 'application/json' ,
    'X-CSRF-TOKEN': getCookie('csrf_access_token')},
  };
  
  fetch('/api/logout', requestOptions)
    .then(response => response.json())
    .then(data =>{console.log(data); router.push({name: "home"})})

}

    </script>
    
    <template>
     
    <section>
      <main>
     
        <div class="container" >
        
            <p >Sure you want to logout?</p>
                 
            <button  type="submit"  class ="button"  v-on:click= "logout" > Yes </button> 
                  
            <button class="button"  v-on:click.prevent="redirect()"> <b> NO</b> </button>
               
   
            
        </div>

  

    </main>
    






  </section>
    

        

    </template>
    
    
    <style scoped>

body{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #131313;

}

.container{
  position: relative;
  display: flex;
  left:-800px;
  top:150px;

  margin-right: -20px;
  padding: 2px;
  list-style-type: none;
  border-radius: 20%;
  width:350px;
  height:200px;
  
  background: rgba(136, 105, 129, 0.39);
  border-radius: 20px;
  overflow: hidden;
  margin: 2em;
  left: -35px;
 
  

}


.container  .button :hover {
  background-color: rgb(213, 95, 95);
}

p{
    position: relative;
    text-align: center;
    left:50px;
    top:50px;
}

.button{
  position: relative;
  top:150px;
  background: #d54713;
  margin-left: 10px;
  width:50px;
  height:30px;
  font-weight: 600;
  color: rgb(255, 254, 254);
  border-radius: 8px;

  

}


</style>



