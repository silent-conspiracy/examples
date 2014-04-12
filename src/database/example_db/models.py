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
    access_token = models.CharField(max_length=256)
