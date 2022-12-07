from django.db import models
from django.contrib.auth import models as auth_models

# token authorization
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# to create tokens for already registered users uncomment the next section
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    # category = models.CharField(max_length=1000,default='None')
    name=models.CharField(max_length=1000)
    # price = models.FloatField()
    
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    # category = models.CharField(max_length=1000,default='None')
    name=models.CharField(max_length=1000)
    # price = models.FloatField()

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000)
    price = models.FloatField()



class User(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]