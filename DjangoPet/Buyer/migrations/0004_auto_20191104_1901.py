# Generated by Django 2.1.8 on 2019-11-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_auto_20191104_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_info',
            old_name='goods_time',
            new_name='goods_name',
        ),
    ]
