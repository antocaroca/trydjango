from django.db import models

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120) # max_length = is required
    description = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=200, blank=True, null=True)
    

