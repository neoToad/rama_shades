from .models import Order, Item
import json
from decimal import Decimal
from .utils import cookie_cart


def cart_processor(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, ordered=False)
        items = order.user.orderitem_set.all().exclude(ordered=True)
        cart_items = order.get_cart_items
    else:
        return cookie_cart(request)
    return {'items': items, 'cart_items': cart_items, 'object': order}
