from .models import Order, Item
import json
from decimal import Decimal


def cart_processor(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, ordered=False)
        items = order.user.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except KeyError:
            cart = {}
        print('Cart:', cart)
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

                order['get_shipping'] = Decimal(7 - 1 + (cart[i]['quantity'] * .5))

                order['total'] = order['get_cart_total'] + order['get_shipping']

                get_amount_saved = product.price - product.discount_price

                item = {
                    'product': {
                        'id': product.id,
                        'title': product.title,
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
    return {'items': items, 'cart_items': cart_items, 'object': order}
