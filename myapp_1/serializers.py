from rest_framework import serializers
from .models import (
    Customer,
    Product,
    Purchase,
    PurchaseDetails,
    PurchaseOrder,
    PurchaseOrderDetails,
)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id', 'create_at', 'update_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'create_at', 'update_at']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        read_only_fields = ['id', 'create_at', 'update_at']


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetails
        fields = '__all__'
        read_only_fields = ['id', 'create_at', 'update_at']


class PurchaseOrderDetailsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = PurchaseOrderDetails
        fields = '__all__'
        read_only_fields = ['create_at', 'update_at']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer(read_only=True)
    purchaseorderdetails_set = PurchaseOrderDetailsSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = PurchaseOrder
        fields = ['purchase_order_id', 'order_date', 'due_date', 'arrival_date', 'status', 'customer_id',
                  'purchaseorderdetails_set', 'create_at', 'update_at'
                  ]
        read_only_fields = ['create_at', 'update_at']

