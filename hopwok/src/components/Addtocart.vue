<script setup>
import { ref } from "vue";
import { onMounted, onRenderTriggered } from "vue";
const props = defineProps({
  msg: {
    type: String,
    required: true,
  },
  image: {
    type: String,
  },
  Instock: {
    type: Boolean,
  },

  id: {
    type: Number,
  },
  cart_item: {
    type: Object,
  },
  quantity: {
    type: Number,
  },


});
const counts = ref(1)
function increment()
{
  counts.value =  counts.value + 1;

    return counts.value = counts.value;
    }
function decrement()
{
      if (counts.value > 1) { 
        counts.value =  counts.value - 1;
        return counts.value = counts.value;
      }
}
const carts = ref([])
async function api(url,options) {
  const response = await fetch(url,options);
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return await response.json();
}
function getcart() {
const requestOptions = {
    method: "GET",
    credentials: "same-origin",
    headers: { "Content-Type": "application/json" },
  };
  api('/api/carts',requestOptions)
   
    .then((data) => {carts.value = data})
    .catch(error => {console.log(error.toString())
  }
)  
}
onMounted(() => getcart())

function deletecart(cart_item){
  const requestOptions = {
    method: 'DELETE',
    credentials: 'same-origin',
    headers: {"Content-Type": "application/json" },
     body: JSON.stringify(cart_item)
  };
let url = `/api/cart/${cart_item}`
console.log(cart_item)
async function api(url,requestOptions) {
const response = await fetch(url,requestOptions);
if (!response.ok) {
throw new Error(response.statusText);
}
return await response.json();
}


  api(url, requestOptions)
    
    .then(data => (cart_item = data.id))
    .catch((error) => {console.log(error.toString())})
    
}
function patchcart(cart_item){
  const requestOptions = {
    method: 'PATCH',
    credentials: 'same-origin',
    headers: {"Content-Type": "application/json" },
     body: JSON.stringify(cart_item)
  };
let url = `/api/cart/${cart_item}`
console.log(cart_item)
async function api(url,requestOptions) {
const response = await fetch(url,requestOptions);
if (!response.ok) {
throw new Error(response.statusText);
}
return await response.json();
}


  api(url, requestOptions)
    
    .then(data => (cart_item = data.id))
    .catch((error) => {console.log(error.toString())})
    
}
</script>

<template>
<div>
<header><div><img class ="cart" src =  "/public/shopp.png"  alt="-" /></div></header>
  <section>
    <main>
        <div class="fetch">
          <div class="card">
            <ul v-for="c in carts.items" :key="c.productId">
              <li >
                <div class = "container">
                  <img v-bind:src = "c.image" />
                  <div class="quantity">
                    <p>{{ c.product_name }}</p>
                    <p>quantity:   {{ c.quantity }}</p>
                    <p>price:      {{ c.product_rate }}</p> 
                    <button class="plus-btn"   v-on:click.prevent="increment()"> <b> + </b></button>
                    <input type = "text" v-model="counts" />
                    <button class="minus-btn"  v-on:click.prevent="decrement()"> <b> - </b> </button>
                    <button class="bin"  @click = " deletecart(c.productId) " >
                      <img class ="dust" src="/public/bin.png" alt="-" />
                    </button> 
                    <button class="rot"  @click = " patchcart({productId : c.productId , quantity: counts}) " >
                      <img class ="update" src="/public/rotate.png" alt="-" />
                    </button> 
                      
                </div>
                </div>
              </li>
            </ul>    
          </div>
        </div>
    </main>
  </section>
</div>
</template>

<style scoped>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #131313;
}

.container {
  position: relative;
  display: flex;
  top: 30px;
  left: 50px;
  margin: 0.2em;
  padding: 0;
  list-style-type: none;
   background-color: rgb(190, 180, 190);
}
.card {
  width: 1000px;

  gap: 2rem;
  padding: 0;
  list-style-type: none;
}
.container .card {
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

.container .card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #3c383b;
  clip-path: circle(150px at 80% 20%);
  transition: 0.3s ease-in-out;
}

.container .card:hover:before {
  clip-path: circle(300px at 80% -20%);
}

.container .card:after {
  position: absolute;
  top: 30%;
  left: -20%;
  font-size: 12em;
  font-weight: 800;
  font-style: italic;
  color: rgba(101, 101, 100, 0.05);
}
.imgBx {
  position: absolute;
  top: 50%;
  left: -60px;
 
}

.container .card  {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10000;
  width: 70%;
  height: 120px;
  transition: 0.5s;
}

.container .card:hove {
  top: 0%;
  transform: translateY(0%);
}

.container .card  img {
  position: absolute;
  top: 35%;
  left: 100%;
  transform: translate(-50%, -50%);
  width: 170px;
}

.container .card .contentBx {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 100px;
  text-align: center;
}
.container img{

  width: 10%;
  top: 150px;
  
}

.fetch {
  position:relative;
  list-style: none;
  padding: 0;
  margin: 0;
  left : 120px;
  width: 1200px;
 

}
.container .card:hover .contentBx {
  height: 210px;
}
h2 {
  position: relative;
  font-weight: 600;
  letter-spacing: 1px;
  color: #000;
  margin: 0;
  left: 250px;
  top: 80px;
}
h3 {
  position: relative;

  letter-spacing: 1px;
  color: #000;
  margin: 0;
  left: 250px;
  top: 80px;
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;
}

.container .card .contentBx h2 {
  position: relative;
  font-weight: 600;
  letter-spacing: 1px;
  color: #000;
  margin: 0;
}

.container .card .contentBx .price,
.container .card .contentBx .color {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  transition: 0.5s;
  opacity: 0;
  visibility: hidden;
  padding-top: 0;
  padding-bottom: 0;
}

.container .card:hover .contentBx .price {
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card:hover .contentBx .color {
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card .contentBx .price h3,
.container .card .contentBx .color h3 {
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;
}

.container .card .contentBx .price span {
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

.container .card .contentBx .price span:hover {
  background: #9bdc28;
}

.container .card .contentBx .color span {
  width: 20px;
  height: 100px;
  background: #ff0;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}

.button {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  left: 250px;
  top: 200px;
  font-weight: 600;
  color: #111;
  border-radius: 8px;
}
.button2 {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: #981515;
  margin-left: 10px;
  left: 250px;
  top: 200px;
  font-weight: 600;
  color: #111;
  border-radius: 8px;
}

.container .card .contentBx .a {
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
a {
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
ul{
  list-style: none;
}
.quantity {
  position: relative;
  top: -20px;
  left: 20px;
}
.quantity input {
  -webkit-appearance: none;
  border: none;
  text-align: center;
  width: 32px;
  font-size: 16px;
  color: #43484D;
  font-weight: 300;
}
 
button[class*=btn] {
  width: 30px;
  height: 30px;
  background-color: #E1E8EE;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}

button:focus,
input:focus {
  outline:0;
}

.quantity .minus-btn{
  background-color:
  #a71818;
}
.quantity .plus-btn{

  background-color:#23730f;
} 
.quantity .bin{
position:relative;
left: 15px;
top:2px;
width:30px;
height: 30px;
} 
.quantity .dust{


width:70%;
height:60%;
} 
.quantity .rot{
position:relative;
left: 15px;
top:3px;
width:30px;
height: 30px;
margin: 2px;
} 
.quantity .update{
width:90%;
} 
.cart{
width:5%;
} 
</style>
