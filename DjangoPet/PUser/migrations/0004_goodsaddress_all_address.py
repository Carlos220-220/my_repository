# Generated by Django 2.1.8 on 2019-11-05 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PUser', '0003_goodsaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsaddress',
            name='all_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PUser.User'),
            preserve_default=False,
        ),
    ]