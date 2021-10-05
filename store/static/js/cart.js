var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var style = this.dataset.style
        console.log('productId:', productId, 'action:', action,)

        console.log('USER:', user)
        console.log('STYLE:', style)

        if(user == 'AnonymousUser'){
            addCookieItem(productId, style, action)
        }else{
            updateUserOrder(productId, style, action)
        }
    })
}

function addCookieItem(productId, style, action){
    console.log('Not logged in')

    if(action == 'add'){
        if(cart[productId] == undefined){
          cart[productId] = {'quantity': 1}
          cart[productId][style] = {'quantity':1}

        }else if(cart[productId][style] == undefined ){
          cart[productId]['quantity']  += 1
          cart[productId][style] = {'quantity':1}
        }else{
          cart[productId][style]['quantity'] += 1
          cart[productId]['quantity']  += 1
        }


    }

    if(action == 'remove'){
        cart[productId]['quantity'] -= 1
        cart[productId][style]['quantity'] -= 1

        if(cart[productId][style]['quantity'] <= 0){
          delete cart[productId][style]
        }

        if(cart[productId]['quantity'] <= 0){
          console.log('Remove Item')
          delete cart[productId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, style, action){
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'style': style,'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}