<script  setup>
import {ref, onMounted } from 'vue';
const props = defineProps({
        username :{
        type: String,
       
     },
      email: {
        type: String,
      },
      phone_number:
        {
            type:Number
        },
      user_address :{
        type:String
      },
      password:
        {
            type:String
        }
    }) 
function signup(){
const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: `${props.username}`,email: `${props.email}`, phone_number:`${props.phone_number}`,user_address:`${props.user_address}`,password:`${props.password}`})
  };
  
  fetch("api/signup", requestOptions)
    .then(response => response.json())
    .then(data => console.log(data));
}

    </script>
    
    <template>
     
    <section>
      <main>
      
            <form @submit.prevent="signup" >
            <div class="form-group">
                <h3>Sign Up</h3>
                <div class = "card" >
                <input type="text" class="form-control" placeholder="username" v-model="username"/>
                </div>
                <div class = "card" >
                <input type="email" class="form-control"  placeholder="Email" v-model="email" />
                </div>
                <div class = "card" >
                <input type="tel" class="form-control "  placeholder="Phone number" v-model="phone_number"/>
                </div>
                <div class = "card" >
                <input type="tel" class="form-control"  placeholder="Address" v-model="user_address"/>
                </div>
                <div class = "card" >
                <input type="password" class="form-control"  placeholder="Password" v-model="password"/>
                </div>       
                <button  type="submit"  class ="button" v-on:click="signup" > sign up </button> 
            </div>        
          </form>
   

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
  top: -5px;
  font-weight: 600;
  color: #111;
  border-radius: 8px;


  

}

.form-group {
  overflow: visible;
  background-color: rgb(237, 227, 227);
  padding: 20px 25px 30px 20px;
  border-radius: 10px;
  position: relative;
  top: 40%;
  left:30%;
  width: 400px;
  height :420;
  margin :4px;
  animation: swings 2s infinite;

}



input {
    font-family: fontAsap;
    display: block;
    border-radius: 5px;
    font-size: 16px;
    background: white;
    width: 100%;
    border: 0;
    padding: 10px 10px;
    margin: 15px -10px;
  }


</style>



