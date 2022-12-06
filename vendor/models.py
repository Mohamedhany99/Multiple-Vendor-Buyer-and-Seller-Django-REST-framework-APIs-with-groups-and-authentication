from django.db import models

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