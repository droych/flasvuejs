<script setup>
import { ref } from "vue";
import { onMounted, onRenderTriggered } from "vue";
import { useProductStore } from "@/stores/productCart"
import { storeToRefs } from 'pinia'
const props = defineProps({
  
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
  c:
  {
    type:Number
  }


});
const product = useProductStore();
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
product.getcart();
console.log(props.c);

</script>

<template>
<div>
<header></header>
  <section>
    <main>

                    <button class="plus-btn" v-on:click.prevent="increment(c)"> <b> + </b></button>
                    <input type = "text" v-model="counts" />
                    <button class="minus-btn"  v-on:click.prevent="decrement(c)"> <b> - </b> </button>
                    <button class="bin"  @click = " product.deletecart(c) " >
                      <img class ="dust" src="/public/bin.png" alt="-" />
                    </button> 
                    <button class="rot"  @click = " product.patchcart({productId : c , quantity: counts}) " >
                      <img class ="update" src="/public/rotate.png" alt="-" />
                    </button> 
     
    </main>
  </section>
</div>
</template>

<style scoped>

 
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
.cc{
  position: relative;
  left:1240px;
  top:-60px;
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
  border-radius: 10%;
        width: 20px;
        height: 20px;
      
        background: rgb(230, 206, 20);
        border: 3px solid rgb(23, 5, 105);
        color: rgb(159, 78, 78);
        text-align: center;
  font-size: 15px;
  left:40px;
  top:-75px;
}
</style>
