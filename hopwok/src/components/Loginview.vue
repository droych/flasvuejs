<script  setup>
import {ref} from 'vue'
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
const router = useRouter()
function getCookie(name) {
  const cookie = `; ${document.cookie}`;
  const parts = cookie.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function login(){
const requestOptions = {
    method: "POST",
    headers: { 
    'Content-Type': 'application/json' ,
    'X-CSRF-TOKEN': getCookie('csrf_access_token')},
     body: JSON.stringify({ email: `${props.email}`,password:`${props.password}`})
  };
  
  fetch('api/login', requestOptions).then(response => response.json())
  .then(data => {if(data === 400){ window.alert("signup or check email")}
  else if(data === 409){ window.alert("wrong password")}
  else{console.log(data); router.push({name: "products" }) }})

  
    
   
}
    </script>
    
<template>
<div>
<section>
      <main>
            <form @submit.prevent="login" >
            <div class="form-group">
                <h3>Login</h3>
                <div class = "card">
                <input type="email" class="form-control" placeholder="email" v-model="email" />
                </div>
                <div class = "card">  
                <input type="password" class="form-control2" placeholder="password"  v-model="password"/>
                </div>       
                <button  type="submit"  class ="button" > Login </button> 
            </div>  
          </form>
    </main>
  </section>
</div>
</template>
    
    
    <style scoped>
    

body{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #131313;
}
.form-group {
  overflow: hidden;
  background-color: rgb(237, 227, 227);
  padding: 20px 25px 30px 20px;
  border-radius: 10px;
  position: relative;
  top: 50%;
  left:30%;
  width: 400px;
  height :420;
  margin :4px;
}



.card{
  width:100%;
  display: flex;
  margin:5px;

}


.button{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  font-weight: 300;
  font-size: 14px;
  letter-spacing: 2px;
  margin-right: 10px;
  top: 15px;
  left: 40%;
  font-weight: 600;
  color: #111;
  border-radius: 8px;
  
}

input {
    font-family: fontAsap;
    position: relative;
    display: block;
    border-radius: 5px;
    font-size: 16px;
    background: white;
    width: 80%;
    border: 0;
    padding: 10px 10px;
    margin: 15px ;
    left:15px;
   

  }

</style>
