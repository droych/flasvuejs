import { defineStore } from 'pinia'
import { ref,reactive } from "vue"
import { onMounted, onRenderTriggered } from "vue"


export const useProductStore = defineStore('product',() => {
const carts = reactive({data: {}})
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
   
    .then((data) => {carts.data= data})
    .catch(error => {console.log(error.toString())})  
}


onMounted(() => getcart())

function deletecart(cart_item){
    const requestOptions = {
      method: 'DELETE',
      credentials: 'same-origin',
      headers: {"Content-Type": "application/json" },
       body: JSON.stringify(cart_item)
    };
getcart();
  let url = `/api/cart/${cart_item}`
  console.log(cart_item)
  async function api(url,requestOptions) {
  const response = await fetch(url,requestOptions);
  if (!response.ok) {
  throw new Error(response.statusText);
  }

  }
  
  api(url, requestOptions)
  .catch((error) => {console.log(error.toString())})





getcart();
      
  }
  
function patchcart(cart_item){
    const requestOptions = {
      method: 'PATCH',
      credentials: 'same-origin',
      headers: {"Content-Type": "application/json" },
       body: JSON.stringify(cart_item)
    };
  let url = `/api/cart/${cart_item.productId}`
  console.log(cart_item)
  async function api(url,requestOptions) {
  const response = await fetch(url,requestOptions);
  if (!response.ok) {
  throw new Error(response.statusText);
  }
  return await response.json();
  }
  
  
    api(url, requestOptions).then(data => {(cart_item = data.id);console.log(data)}).catch((error) => {console.log(error.toString())})
    getcart();
  }
  
  return { carts, getcart,deletecart,patchcart} 

})