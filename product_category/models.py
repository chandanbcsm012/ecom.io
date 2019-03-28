from django.db import models
from django.urls import reverse

# Create your models here.
class ProductCategory(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    about = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category') 