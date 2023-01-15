from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    pubdate = models.DateTimeField()