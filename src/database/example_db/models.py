from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User)
    facebook_profile = models.OneToOneField(FacebookProfile)
    phone_number = models.IntegerField(max_length=8)
    email = models.EmailField() # Possible duplicate with Facebook, but can have different email.


class FacebookProfile(models.Model):  # Inherits from django's Model class
    first_name = models.CharField(max_length=30)  # Character field with length 30
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    access_token = models.CharField(max_length=128)
    profile_img_url = models.URLField()
    last_modified = models.DateTimeField(auto_now=True)
    datetime_created = models.DateTimeField(auto_now_add=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(max_length=100)


class Table(models.Model):
    number = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant)


class Service(models.Model): # Like an order session
    table = models.ForeignKey(Table)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)
    description = models.TextField()


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=50)
    description = models.TextField()


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    service = models.ForeignKey(Service)
    last_modified = models.DateTimeField(auto_now=True)
    datetime_created = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    menu_item = models.ForeignKey(MenuItem)
    quantity = models.IntegerField(max_length=100)


class Bill(models.Model):
    service = models.ForeignKey(Service)
    customer = models.ForeignKey(Customer, blank=True)
    payment_amount = models.IntegerField()
    payment_datetime = models.DateTimeField(auto_now_add=True)