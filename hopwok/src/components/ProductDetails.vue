<script setup>
import {ref } from 'vue';
import {onMounted, onRenderTriggered } from 'vue';
const props =  defineProps({
      msg :{
        type: String,
        required: true

      },
      image: {
        type: String,
        

      },
      Instock:{
        type: Boolean
        
        
      },

      image :{
        type:String
      },
  
      id:{
            type:Number
        
      },

      cart_item :{
          type : Object,
        
      

        },

    })
const product = ref({})
  
async function api(url) {
  const response = await fetch(url);
if (!response.ok) {
throw new Error(response.statusText);
}
return await response.json();
}
function getproduct() {

api(`http://127.0.0.1:9000/product/${props.id}`)
   .then((data) => {product.value = data})
   .catch(error => {console.log(error.toString())

  }
)  
}
onMounted(() => getproduct())

function addtoCart(_cart_item ){
const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ userId: "1",productId: "2", price:"1600.5",quantity:"1"})
  };
  fetch("http://127.0.0.1:9000/carts", requestOptions)
    .then(response => response.json())
    .then(data => (_cart_item = data.id));
}

    </script>
    
    




    <template>
      <header>

      <div class = "cart" > cart{{cart_item}} </div>

  
    <section>
      <main>
      <div class = "fetch" >
        <div class="container"> 
          <div class="card">
          <div class="imgBx">
        
            <img v-bind:src = "product.image" >
          </div>
        
           <h2>{{product.product_name}}</h2>
           <h3>Price : ₹{{product.product_rate}}</h3>
        
         

        <button class ="button" @click="addtoCart({ product_id: product.id})"> Add to cart </button>
        <button class ="button2"> Wishlist </button>


    </div>
    </div>

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

 
  margin: 0.2em;
  padding: 0;
  list-style-type: none;

}
.card {

  width: 1000px;
  
  gap: 2rem;
  padding: 0;
  list-style-type: none;
}
.container .card{
  position: relative;
  width: 1020px;
  height: 420px;
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
.imgBx{
  position: absolute;
  top: 50%;
  left: -600px;
  transform: translateY(-50%);
  z-index: 1;
  width: 90%;

  transition: 0.5s;
}

.container .card .imgBx{
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10000;
  width: 70%;
  height: 120px;
  transition: 0.5s;
}

.container .card:hove{
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
 
}
.fetch {
    list-style: none;
    padding: 0;
    margin: 0;
    width:1200px;

  
  
  }
.container .card:hover .contentBx{
  height: 210px;
}
h2{
  position: relative;
  font-weight: 600;
  letter-spacing: 1px;
  color: #000;
  margin: 0;
  left:250px;
  top:80px;
  

}
h3{
  position: relative;
 
  letter-spacing: 1px;
  color: #000;
  margin: 0;
  left:250px;
  top:80px;
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;

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
  height: 100px;
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
  height: 100px;
  background: #ff0;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}


.button{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  left:250px;
  top:200px;
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
.container .card:hover {
  opacity: 1;
  transform: translateY(0px);
  transition-delay: 0.75s;
  
}

   
    </style>
    

    
