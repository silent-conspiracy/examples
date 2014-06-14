from django.db import models

# Create your models here.

class Person(models.Model): # Inherits from django's Model class
    first_name = models.CharField(max_length=30)  # Character field with length 30
    last_name = models.CharField(max_length=30)
    fb_account = models.OneToOneField(FacebookUser) # Relates person to his fb
    last_login = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


class FacebookUser(models.Model):
    email = models.EmailField()
    profile_img = models.ImageField(upload_to="/path/to/media/uploads/")


class Customer(Person):
    customerID=models.AutoField(primary_key=True)
    phone_number=models.IntegerField(max_length=8)

class Order(models.Model):
    orderID= models.ForeignKey('Customer')
    quantity= models.IntegerField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order_itemID=models.ForeignKey('OrderItem')
    order_item_name=models.ForeignObject('MenuItem')

class Menu(models.Model):
    menuID=models.ForeignKey('FoodStall')
    #menuItems=models.ForeignObject()

class MenuItem(models.Model):
    menuItemID=models.ForeignKey('Menu')
    menuItemName=models.CharField(max_length=30)

class FoodStall(models.Model):
    #restaurantID ＝models.AutoField(primary_key=True)
    restaurantName=models.CharField()
    restaurantAddr=models.CharField()

class Bill(models.Model):
    billID= models.ForeignKey('Customer')