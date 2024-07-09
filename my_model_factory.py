import datetime

import django
import os

import tqdm
from django.db import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.local')
django.setup()

import random

from faker import Faker
from factory import SubFactory
from factory.django import DjangoModelFactory
from myapp_1.models import (
    Customer,
    Product,
    PurchaseOrder,
    PurchaseOrderDetails
)

fake = Faker('ja_JP')


def get_random_customer():
    all_records = Customer.objects.all()
    if not all_records:
        return None
    return random.choice(all_records)


def get_last_customer_id():
    result = Customer.objects.all().order_by('customer_id').last()
    if not result or not result.exists():
        return 1
    return result.id + 1


def get_last_product_id():
    result = Product.objects.all().order_by('product_id').last()
    if not result or not result.exists():
        return 1
    return result.product_id + 1


def get_last_purchase_order_id():
    result = PurchaseOrder.objects.all().order_by('purchase_order_id').last()
    if not result or not result.exists():
        return 1
    return result.purchase_order_id + 1


def get_last_purchase_order_details_row_number(purchase_order_id):
    result = PurchaseOrderDetails.objects.filter(purchase_order_id=purchase_order_id).order_by('row_number').last()
    if not result or not result.exists():
        return 1
    return result.row_number + 1


def generate_fake_product_name():
    adjective = fake.safe_color_name()  # 安全な色の名前
    noun = fake.word(ext_word_list=None)  # 一般的な単語
    material = fake.job()  # ランダムな職業名
    return f"{adjective.capitalize()} {noun.capitalize()} {material.capitalize()}"


def create_customer(size):
    for i in tqdm.tqdm(range(size)):
        Customer.objects.get_or_create(
            customer_id=i + 1,
            name=fake.company(),
            postal_code=fake.postcode(),
            address1=fake.address()[:40],
            address2=fake.address()[:40],
            phone_number=fake.phone_number(),
            fax_number=fake.phone_number(),
            cutoff_day1=fake.random_int(min=1, max=31),
            cutoff_day2=fake.random_int(min=1, max=31),
            cutoff_day3=fake.random_int(min=1, max=31),
            most_recent_cutoff_date=fake.date_between_dates(
                date_start=datetime.date(2024,1,1),
                date_end=datetime.date(2024,12,31)
            )
        )


def create_product(size):
    for i in tqdm.tqdm(range(size)):
        p_name = generate_fake_product_name()
        Product.objects.get_or_create(
            product_id=i + 1,
            name=p_name[:20],
            shortname=p_name[:10],
            retail_price=fake.random_int(min=1, max=999),
            unit_price=fake.random_int(min=1, max=999),
            purchase_price=fake.random_int(min=1, max=999),
        )


def get_product_id():
    all_records = Product.objects.all()
    if not all_records:
        return None
    return random.choice(all_records)


def create_purchase_order_details(purchase_order_id):
    for i in range(random.choice(range(1, 6))):
        PurchaseOrderDetails.objects.create(
            purchase_order_id=purchase_order_id,
            row_number=i + 1,
            product_id=get_product_id(),
            purchase_price=fake.random_int(min=1, max=999),
            order_quantity=fake.random_int(min=1, max=100),
            order_amount=fake.random_int(min=1, max=999),
            arrival_quantity=0,
            unit='個',
            order_status=0,
        )


def create_purchase_order(size):
    for i in tqdm.tqdm(range(size)):
        date_1 = fake.date_between_dates(
                date_start=datetime.date(2024,5,1),
                date_end=datetime.date(2024,7,31)
            )
        purchase_order = PurchaseOrder.objects.create(
            purchase_order_id=i + 1,
            order_date=date_1,
            due_date=date_1 + datetime.timedelta(days=7),
            arrival_date=date_1 + datetime.timedelta(days=7),
            status=0,
            customer_id=get_random_customer(),
        )

        create_purchase_order_details(purchase_order)


# class CustomerFactory(DjangoModelFactory):
#     class Meta:
#         model = Customer
#
#     customer_id = random.choice([n for n in range(1000)])
#     name = fake.company()
#     postal_code = fake.postcode()
#     address1 = fake.address()
#     address2 = fake.address()
#     phone_number = fake.phone_number()
#     fax_number = fake.phone_number()
#     cutoff_day1 = fake.random_int(min=1, max=31)
#     cutoff_day2 = fake.random_int(min=1, max=31)
#     cutoff_day3 = fake.random_int(min=1, max=31)
#     most_recent_cutoff_date = fake.date_between_dates(
#         date_start=datetime.date(2024,1,1),
#         date_end=datetime.date(2024,12,31)
#     )
#
#
# class ProductFactory(DjangoModelFactory):
#     class Meta:
#         model = Product
#
#     product_id = get_last_product_id()
#     name = fake.name()
#     short_name = fake.name()
#     retail_price = fake.random_int(min=1, max=9999)
#     purchase_price = fake.random_int(min=1, max=9999)
#
#
# class PurchaseOrderFactory(DjangoModelFactory):
#     class Meta:
#         model = PurchaseOrder
#
#     purchase_order_id = get_last_purchase_order_id()
#     order_date = fake.date()
#     due_date = fake.date()
#     arrive_date = fake.date()
#     status = 0
#     customer = get_random_customer()
#
#
# class PurchaseOrderDetailsFactory(DjangoModelFactory):
#     class Meta:
#         model = PurchaseOrderDetails
#
#     purchase_order_id = SubFactory(PurchaseOrderFactory)
#     row_number = 1
#     product_id = SubFactory(ProductFactory)
#     unit_price = fake.random_int(min=1, max=9999)
#     quantity = fake.random_int(min=1, max=9999)
#     line_total = 0
#     unit = '個'
#     order_status = 0


if '__main__' == __name__:
    # customer_factory = CustomerFactory.create_batch(1000)
    # purchase_order_details_factory = PurchaseOrderDetailsFactory.create_batch(10000)
    # create_customer(1000)
    create_product(5000)
    create_purchase_order(10000)
