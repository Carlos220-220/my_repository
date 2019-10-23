from django.db import models


class Editor(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class NewsType(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.label


class News(models.Model):
    title = models.CharField(max_length=32, verbose_name="新闻标题")
    time = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="img/upload")
    content = models.TextField()
    type_id = models.ForeignKey(to=NewsType, on_delete=models.CASCADE)
    editor_id = models.ManyToManyField(to=Editor)

    def __str__(self):
        return self.title
# Create your models here.
