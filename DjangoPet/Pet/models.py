from django.db import models


class GoodsType(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.label


class Goods(models.Model):
    name = models.CharField(max_length=32, verbose_name='商品名称')
    price = models.CharField(max_length=32)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/upload')
    origin = models.CharField(max_length=32)
    type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DogType(models.Model):
    label = models.CharField(max_length=32, verbose_name='犬种')
    type = models.CharField(max_length=32)
    type_id = models.ManyToManyField(to=Goods)

    def __str__(self):
        return self.label
# Create your models here.
