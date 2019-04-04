from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120) # max_length = is required
    description = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=200, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id":self.id}) # f"/products/{self.id}/
        # return f"{self.id}"
        # return reverse("articles:article-detail", kwargs={"id":self.id})
        # this takes me to the article (url) that i am saving in the database



