from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.title

class Dict(models.Model):
    title = models.CharField(max_length=255, default='default title')
    data = models.JSONField()

    def __str__(self):
        return self.title
