from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = is required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(blank=False, null=False) # this field is required. This field cannot be empty in the database.
    featured    = models.BooleanField(default=False) # null=True, default=True
# blank = True/False has to do with how the field is rendered. Null has to do with the database
# if blank =  False means that the field is required

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id":self.id}) # f"/products/{self.id}/
        # self is referring to the instamce of the object
        # yo need to call tha name of the url that is going to handle the data "products:product-detail"