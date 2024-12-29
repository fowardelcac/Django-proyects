from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=75, verbose_name="Author")
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.CharField(max_length=500, verbose_name="Content")

    def __str__(self):
        return self.author
