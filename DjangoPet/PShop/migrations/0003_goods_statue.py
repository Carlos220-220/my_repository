# Generated by Django 2.1.8 on 2019-10-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PShop', '0002_goods_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='statue',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]