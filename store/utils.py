from .models import Item
import json
from decimal import Decimal


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except KeyError:
        cart = {}
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cart_items = order['get_cart_items']

    for i in cart:
        try:
            cart_items += cart[i]['quantity']

            product = Item.objects.get(id=i)
            total = (product.discount_price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            order['get_shipping'] = Decimal(7 + (cart[i]['quantity'] * .5))

            order['total'] = order['get_cart_total'] + order['get_shipping']

            get_amount_saved = product.price - product.discount_price

            item = {
                'product': {
                    'id': product.id,
                    'title': product.title,
                    # 'style': cart[i]['style'],
                    'price': product.price,
                    'discount_price': product.discount_price,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
                'get_amount_saved': get_amount_saved
            }
            items.append(item)
        except:
            cart_items -= cart[i]['quantity']
    return {'items': items, 'cart_items': cart_items, 'object': order,
            'categories': ['Square', 'Cat Eye', 'Round', 'Rectangular',
                  'Oval', 'Unique']}