from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)


class Book(models.Model):
    name=models.CharField(max_length=32)
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE) #级联删除
    """  
    on_delete 2.0后必填
    models.CASCADE 级联删除
    models.PROTECT 保护
    models.SET
    models.SETDEFAULT
    models.SET_NULL
    """
class Author(models.Model):
    name=models.CharField(max_length=32)
    books = models.ManyToManyField('Book') #创建多对多关系的conjunc table


