from django.db import models
# Create your models here.
class User(models.Model): #创建一个表
    username = models.CharField(max_length=32) #varchar
    password = models.CharField(max_length=32)