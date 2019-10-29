from django.db import models
from ckeditor.fields import RichTextField


class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    number = models.IntegerField()
    production = models.DateTimeField()
    safe_date = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='pshop/img', default='pshop/img/1.jpg')
    description = RichTextField(null=True)
    statue = models.IntegerField(null=True)

