from django.db import models

# Create your models here.

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120) # max_length = is required
    description = models.TextField(blank=True, null=True)
    summary     = models.TextField(blank=False, null=False) # this field is not required. This field can be empty in the database.
    

