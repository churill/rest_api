# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=15)
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    phone_number = models.CharField(db_column='Phone_number', max_length=20)
    fax_number = models.CharField(max_length=20)
    cutoff_day1 = models.SmallIntegerField()
    cutoff_day2 = models.SmallIntegerField()
    cutoff_day3 = models.SmallIntegerField()
    most_recent_cutoff_date = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Customer'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    shortname = models.CharField(max_length=10)
    retail_price = models.DecimalField(max_digits=19, decimal_places=4)
    unit_price = models.DecimalField(max_digits=19, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=19, decimal_places=4)
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Product'


class Purchase(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, to_field='customer_id', db_column='customer_id')
    input_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    purchase_division = models.SmallIntegerField()
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Purchase'


class PurchaseDetails(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.PROTECT, to_field='purchase_id', db_column='purchase_id')
    row_number = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, to_field='product_id', db_column='product_id')
    unit_price = models.DecimalField(max_digits=19, decimal_places=4)
    quantity = models.DecimalField(max_digits=19, decimal_places=4)
    line_total = models.DecimalField(max_digits=19, decimal_places=4)
    unit = models.CharField(max_length=5)
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Purchase_Details'
        unique_together = (('purchase_id', 'row_number'),)


class PurchaseOrder(models.Model):
    purchase_order_id = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, to_field='customer_id', db_column='customer_id')
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Purchase_Order'


class PurchaseOrderDetails(models.Model):
    purchase_order_id = models.ForeignKey(to=PurchaseOrder, on_delete=models.CASCADE, to_field='purchase_order_id', db_column='purchase_order_id')
    row_number = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='product_id', db_column='product_id')
    purchase_price = models.DecimalField(max_digits=19, decimal_places=4)
    order_quantity = models.DecimalField(max_digits=19, decimal_places=4)
    order_amount = models.DecimalField(max_digits=19, decimal_places=4)
    arrival_quantity = models.DecimalField(max_digits=19, decimal_places=4)
    unit = models.CharField(max_length=5)
    order_status = models.SmallIntegerField()
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'Purchase_Order_Details'
        unique_together = (('purchase_order_id', 'row_number'),)