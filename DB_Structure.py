import datetime

from peewee import *

db = MySQLDatabase('graviola_test', user='root', password='P@ssw0rd', host='localhost', port=3306)

Status_Order = (
    (1, 'Prepare'),
    (2, 'Deliver'),
    (3, 'Done')
)

class Products(Model):
    code_Product = IntegerField(null=False)
    title_Product = CharField(null=False)
    description_Product = TextField(null=True)
    price_Product = DecimalField(null=True)
    image_Product = CharField(null=True)
    Product_unit = IntegerField(null=True)

    class Meta:
        database = db

class Locations(Model):
    governorate = CharField(null=False)
    city = CharField(null=False)
    area = CharField(null=False)

    class Meta:
        database = db

class Governorates_egy(Model):
    name_governorate = CharField(null=False)
    date = DateTimeField(null=True)

    class Meta:
        database = db

class Clients(Model):
    code_client = IntegerField(null=False)
    name_client = CharField(null=False)
    phone_client_1 = CharField(null=False)
    phone_client_2 = CharField(null=True)
    Promo_code = CharField(null=True)
    governorate_client = CharField(null=True)
    area_client = ForeignKeyField(Locations, backref='area', null=True)
    address_client = CharField(null=False)

    class Meta:
        database = db

class Delivery(Model):
    code_delivery = IntegerField(null=False)
    name_delivery = CharField(null=False)
    phone_delivery_1 = CharField(null=False)
    phone_delivery_2 = CharField(null=True)
    area_delivery_id = ForeignKeyField(Locations, backref='area', null=True)
    governorate_delivery = CharField(null=True)
    address_delivery = CharField(null=True)

    class Meta:
        database = db

class Employees(Model):
    code_employee = IntegerField(null=False)
    name_employee = CharField(null=False)
    email_employee = CharField(null=True)
    phone_employee = CharField(null=True)
    date = DateTimeField(null=True)
    national_id_employee = IntegerField(null=True)
    priority_employee = IntegerField(null=True)
    user_name_employee = CharField(null=False)
    password_employee = CharField(null=False)
    password2_employee = CharField(null=False)

    class Meta:
        database = db


class Orders(Model):
    code_order = IntegerField(null=False)
    code_clint = ForeignKeyField(Clients, backref='order_clint', null=False)
    employee = ForeignKeyField(Employees, backref='order_employee', null=False)
    code_delivery = ForeignKeyField(Delivery, backref='order_delivery', null=True)
    order_status = CharField(choices=Status_Order)  # [Prepare - Deliver - Done]
    date_order = DateTimeField()
    date_expected = DateField()
    date_deliver = DateField(null=True)
    id_itm_01 = CharField(null=False)
    number_itm_01 = IntegerField(null=False)
    code_itm_02 = CharField(null=True)
    number_itm_02 = IntegerField(null=True)
    code_itm_03 = CharField(null=True)
    number_itm_03 = IntegerField(null=True)
    code_itm_04 = CharField(null=True)
    number_itm_04 = IntegerField(null=True)
    code_itm_05 = CharField(null=True)
    number_itm_05 = IntegerField(null=True)
    code_itm_06 = CharField(null=True)
    number_itm_06 = IntegerField(null=True)
    code_itm_07 = CharField(null=True)
    number_itm_07 = IntegerField(null=True)
    code_itm_08 = CharField(null=True)
    number_itm_08 = IntegerField(null=True)
    code_itm_09 = CharField(null=True)
    number_itm_09 = IntegerField(null=True)
    code_itm_10 = CharField(null=True)
    number_itm_10 = IntegerField(null=True)
    discount = DecimalField(null=True)
    delivery_value = DecimalField(null=True)
    total_order = DecimalField(null=False)

    class Meta:
        database = db

class Daily_Movements(Model):
    order = ForeignKeyField(Products, backref='Daily_order')
    client = ForeignKeyField(Clients, backref='Product_Clint')
    date = DateTimeField(default=datetime.datetime.now)
    employee = ForeignKeyField(Employees, backref='Daily_Employee')

    class Meta:
        database = db

ACTION_TYPE = (
    (1, 'Login'),
    (2, 'Update'),
    (3, 'Create'),
    (4, 'Delete'),
)

TABLE_CHOICES = (
    (1, 'Products'),
    (2, 'Clients'),
    (3, 'Locations'),
    (4, 'Delivery'),
    (5, 'Employees'),
    (6, 'Orders'),
    (7, 'Daily_Movements'),
)

class History(Model):
    employee = ForeignKeyField(Employees, backref='History_Employee')
    action = CharField(choices=ACTION_TYPE) #Choices
    table = CharField(choices=TABLE_CHOICES) #Choices
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

db.connect()
db.create_tables([Products, Locations, Governorates_egy, Clients, Delivery, Employees, Orders, Daily_Movements, History])