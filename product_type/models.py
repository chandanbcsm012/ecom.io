from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length = 30)
    code = models.CharField(max_length = 30)
    def __str__(self):
        return self.name