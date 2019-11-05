from django.db import models
from ckeditor.fields import RichTextField
from PUser.models import *


class GoodsType(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='pshop/img', default='pshop/img/1.jpg')


class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    number = models.IntegerField()
    production = models.DateTimeField()
    safe_date = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='pshop/img', default='pshop/img/1.jpg')
    description = RichTextField(null=True)
    statue = models.IntegerField(null=True)
    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)
    goods_store = models.ForeignKey(to=User, on_delete=models.CASCADE)
