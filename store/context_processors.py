from .models import Order, Item
import json


def cart_processor(request):
    # if request.user.is_authenticated:
    #     order, created = Order.objects.get_or_create(user=request.user, ordered=False)
    #     cart_items = order.get_cart_items
    # else:
    #     try:
    #         cart = json.loads(request.COOKIES['cart'])
    #     except KeyError:
    #         cart = {}
    #     print('Cart:', cart)
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_items': 0}
    #     cart_items = order['get_cart_items']
    #
    #     for i in cart:
    #         cart_items += cart[i]['quantity']
    #
    #         product = Item.objects.get(id=i)
    #         total = (product.price * cart[i]['quantity'])
    #
    #         order['get_cart_total'] += total
    #         order['get_cart_items'] += cart[i]['quantity']
    #
    #         item = {
    #             'product': {
    #                 'id': product.id,
    #                 'title': product.title,
    #                 'price': product.price,
    #             },
    #             'quantity': cart[i]['quantity'],
    #             'get_total': total,
    #         }
    #         items.append(item)
    pass
    # return {'items': items, 'cart_items': cart_items, 'object': order}