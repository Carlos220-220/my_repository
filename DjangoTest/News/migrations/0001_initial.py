# Generated by Django 2.1.8 on 2019-10-16 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='新闻标题')),
                ('time', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='img/upload')),
                ('content', models.TextField()),
                ('editor_id', models.ManyToManyField(to='News.Editor')),
            ],
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.NewsType'),
        ),
    ]