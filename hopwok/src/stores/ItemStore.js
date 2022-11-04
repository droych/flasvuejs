import { defineStore } from 'pinia'
import { ref,reactive } from "vue"
import { onMounted, onRenderTriggered } from "vue"


export const useItemtStore = defineStore('products',() => {
    const products = ref([])
    async function api(url) {
      const response = await fetch(url);
    if (!response.ok) {
    throw new Error(response.statusText);
    }
    return await response.json();
    }
    function getproduct() {
    api('api/products')
        .then((data) => {products.value = data})
        .catch(error => {console.log(error.toString())
      }
    )  
    }
    onMounted(() => getproduct())
    async function apis(url,options) {
      const response = await fetch(url,options);
    if (!response.ok) {
    throw new Error(response.statusText);
    }
    return await response.json();
    }
    let clicked = false
    function addtoCart(cart_item){
      console.log(cart_item)
    const requestOptions = {
        method: 'POST',
        credentials: 'same-origin',
        headers: {"Content-Type": "application/json" },
         body: JSON.stringify(cart_item)
      };
      apis('/api/carts', requestOptions)
        .then(response => console.log(response))
        .catch((error) => {console.log(error.toString())})
      
    }



  return { products, getproduct, addtoCart } 

})