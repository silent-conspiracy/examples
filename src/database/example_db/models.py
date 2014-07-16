from django.db import models

# Create your models here.


class Person(models.Model):  # Inherits from django's Model class
    first_name = models.CharField(max_length=30)  # Character field with length 30
    last_name = models.CharField(max_length=30)
    #fb_account = models.OneToOneField(FacebookUser)  # Relates person to his fb
    last_login = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

#class FacebookUser(models.Model):
#    email = models.EmailField()
#    profile_img = models.ImageField(upload_to="/path/to/media/uploads/")
#    access_token = models.CharField(max_length=256)


class Diner(models.Model):
    diner_num = models.AutoField(primary_key=True)
    diner_name = models.CharField(max_length=30)
    diner_address = models.CharField(max_length=30)
    diner_website = models.URLField(max_length=100)


class Table(models.Model):
    table_num= models.AutoField(primary_key=True)
    diner=models.ForeignKey(Diner)


class Service(models.Model):
    service_id= models.AutoField(primary_key=True)
    table=models.ForeignKey(Table)


class Customer(Person):
    customer_num = models.AutoField(primary_key=True)
    phone_number = models.IntegerField(max_length=8)


class Menu(models.Model):
    menu_num = models.AutoField(primary_key=True)
    diner=models.ForeignKey(Diner)
    menu_name=models.CharField(max_length=30)


class MenuItem(models.Model):
    menu_item_num = models.AutoField(primary_key=True)
    menu=models.ForeignKey(Menu)
    menu_item_name = models.CharField(max_length=30)


class Order(models.Model):
    order_num= models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    #2 foreign keys to customer and menu, one to many relationship
    customer = models.ForeignKey(Customer)
    service=models.ForeignKey(Service)


class OrderItem(models.Model):
    menu_item=models.OneToOneField(MenuItem, primary_key=True)
    order=models.ForeignKey(Order)
    quantity = models.IntegerField(max_length=100)


class Bill(models.Model):
    bill_num=models.AutoField(primary_key=True)
    service=models.ForeignKey(Service)
