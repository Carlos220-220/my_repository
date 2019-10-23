from django.db import models


class FoodsType(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()


class Foods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    description = models.TextField()
    picture = models.ImageField(upload_to='img')
    type_id = models.ForeignKey(to=FoodsType, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='img')
    foods_id = models.ManyToManyField(to=Foods)
    open_time = models.CharField(max_length=32)
    stop_car = models.CharField(max_length=32)
    address = models.TextField()
    label = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='img/upload')
    content = models.TextField()
    news_type = models.CharField(max_length=32)


class Company(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='img')
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    post_code = models.CharField(max_length=32)
    address = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


