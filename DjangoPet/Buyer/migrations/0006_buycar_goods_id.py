# Generated by Django 2.1.8 on 2019-11-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0005_auto_20191104_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='buycar',
            name='goods_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]