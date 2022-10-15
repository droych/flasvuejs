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
function login(){
const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: `${props.email}`,password:`${props.password}`})
  };
  
  fetch("http://127.0.0.1:9000/login", requestOptions)
    .then(response => response.json())
    .then(data => console.log(data));
}

    </script>
    
    <template>
     
    <section>
      <main>
      <div class="card-wrapper">
        <div class="container" >
        
    
            <div class="card">
            <form @submit.prevent="signup" >
            
            <div class="form-group">
                <h3>Login In</h3>
              
 
                <div >
                <label>Email</label>
                <input type="email" class="form-control form-control-lg"  v-model="email" />
                </div>
            
               
                <div>
                <label>Password</label>
                <input type="password" class="form-control form-control-lg"  v-model="password"/>
                </div>       
                <button  type="submit"  class ="button" v-on:click="login" > sign up </button> 
            </div>        
          </form>
        </div>
      </div>
    </div>

    </main>
    






  </section>
    

        

    </template>
    
    
    <style scoped>
    
    .card-wrapper {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 1.5rem;
  
    width: 120ch;
    padding-left: 1rem;
    padding-right: 1rem;
  }
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

 
  margin-right: -20px;
  padding: 2px;
  list-style-type: none;

}
.card {


  gap: 2rem;
  padding: 0;
  list-style-type: none;
}
.container .card{
  position: relative;
  width: 1020px;
  height: 550px;
  background: rgba(136, 105, 129, 0.39);
  border-radius: 20px;
  overflow: hidden;
  margin: 2em;
  left: -35px;
  flex-direction: row;

  list-style-type: none;
  
  
}

.container .card:before{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #3c383b;
  clip-path: circle(150px at 80% 20%);
  transition: 0.3s ease-in-out;
}

.container .card:hover:before{
  clip-path: circle(300px at 80% -20%);
}

.container .card:after{

  position: absolute;
  top: 30%;
  left: -20%;
  font-size: 12em;
  font-weight: 800;
  font-style: italic;
  color: rgba(101, 101, 100, 0.05)
}

.container .card .imgBx{
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10000;
  width: 50%;
  height: 120px;
  transition: 0.5s;
}

.container .card:hover .imgBx{
  top: 0%;
  transform: translateY(0%);
    
}

.container .card .imgBx img{
  position: absolute;
  top: 35%;
  left: 100%;
  transform: translate(-50%, -50%);
  width: 170px;
}

.container .card .contentBx{
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 100px;
  text-align: center;
  transition: 1s;
  z-index: 10;
}
.fetch {
    list-style: none;
    padding: 0;
    margin: 0;
    width:400px;

  
  
  }
.container .card:hover .contentBx{
  height: 210px;
}

.container .card .contentBx h2{
  position: relative;
  font-weight: 600;
  letter-spacing: 1px;
  color: #000;
  margin: 0;
}

.container .card .contentBx .price, .container .card .contentBx .color {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  transition: 0.5s;opacity: 0;
  visibility: hidden;
  padding-top: 0;
  padding-bottom: 0;
}

.container .card:hover .contentBx .price{
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card:hover .contentBx .color{
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card .contentBx .price h3, .container .card .contentBx .color h3{
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;

}

.container .card .contentBx .price span{
  width: 26px;
  height: 26px;
  text-align: center;
  line-height: 26px;
  font-size: 14px;
  display: inline-block;
  color: #111;
  background: rgb(121, 102, 102);
  margin: 0 5px;
  transition: 0.5s;
  color: #111;
  border-radius: 4px;
  cursor: pointer;

}

.container .card .contentBx .price span:hover{
  background: #9bdc28;
}

.container .card .contentBx .color span{
  width: 20px;
  height: 20px;
  background: #ff0;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}



.container .card .contentBx .a{
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  border-radius: 4px;
  margin-top: 10px;
  text-decoration: none;
  font-weight: 600;
  color: #111;
  opacity: 0;
  transform: translateY(50px);
  transition: 0.5s;
  margin-right: 0.2cm;
  

}
a{
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;

  letter-spacing: 2px;
  margin-right: 10px;
  top: -5px;
}
.container .card:hover .contentBx .a{
  opacity: 1;
  transform: translateY(0px);
  transition-delay: 0.75s;
  
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
.button2{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #981515;
  margin-left: 10px;
  left:250px;
  top:200px;
  font-weight: 600;
  color: #111;
  border-radius: 8px;

  

}
.form-group {
  overflow: hidden;
  background-color: rgb(237, 227, 227);
  padding: 20px 25px 30px 20px;
  border-radius: 10px;
  position: relative;
  top: 10%;
  left: 20%;
  width: 400px;
  height :420;
  margin :4px;

  

}



</style>



