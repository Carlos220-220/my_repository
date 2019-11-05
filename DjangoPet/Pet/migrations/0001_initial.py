# Generated by Django 2.1.8 on 2019-10-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32, verbose_name='犬种')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('price', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='images/upload')),
                ('origin', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pet.GoodsType'),
        ),
        migrations.AddField(
            model_name='dogtype',
            name='type_id',
            field=models.ManyToManyField(to='Pet.Goods'),
        ),
    ]