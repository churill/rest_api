from django.urls import path
from .views import (
    customer_list_view,
    customer_details_view,
    customer_create_view,
    customer_update_view,
    purchase_order_list_view
)


urlpatterns = [
    path('customer/list/', customer_list_view, name='customer_list'),
    path('customer/detail/<int:pk>/', customer_details_view, name='customer_details'),
    path('customer/create/', customer_create_view, name='customer_create'),
    path('customer/update/<int:pk>/', customer_update_view, name='customer_update'),

    path('purchase_order/list/', purchase_order_list_view, name='purchase_order_list'),
]