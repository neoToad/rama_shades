from django.urls import path
from .views import (
    item_detail_view,
    CheckoutView,
    home,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    update_item,
    order_success,
    category,
    about_us,
)
app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug>/', item_detail_view, name='product'),
    path('category/<prod_category>', category, name='prod_category'),

    # cart functions
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-to-cart/<slug>/!', add_to_cart, name='add-to-cart'),
    path('about_us', about_us, name='about_us'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('guest_order-summary/', OrderSummaryView.as_view(), name='guest_order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('update_item/', update_item, name='update_item'),
    path('order_success/', order_success, name='order_success')

]