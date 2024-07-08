from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import (
    Customer,
    Product,
    Purchase,
    PurchaseDetails,
    PurchaseOrder,
    PurchaseOrderDetails,
)
from .serializers import (
    CustomerSerializer,
    ProductSerializer,
    PurchaseSerializer,
    PurchaseDetailsSerializer,
    PurchaseOrderSerializer,
    PurchaseOrderDetailsSerializer
)
from server.mixins import StandardResultsSetPagination


class CustomerList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


customer_list_view = CustomerList.as_view()


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'customer_id'
    lookup_url_kwarg = 'pk'


customer_details_view = CustomerDetail.as_view()


class CustomerCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


customer_create_view = CustomerCreate.as_view()


class CustomerUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'customer_id'
    lookup_url_kwarg = 'pk'


customer_update_view = CustomerUpdate.as_view()


class PurchaseOrderList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    pagination_class = StandardResultsSetPagination
    pagination_class.page_size = 50


purchase_order_list_view = PurchaseOrderList.as_view()