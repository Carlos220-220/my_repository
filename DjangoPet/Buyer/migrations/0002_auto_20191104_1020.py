# Generated by Django 2.1.8 on 2019-11-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buycar',
            name='car_user',
            field=models.CharField(max_length=32),
        ),
    ]
