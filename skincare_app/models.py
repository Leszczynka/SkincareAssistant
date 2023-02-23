from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images', max_length=200)

    def __str__(self):
        return self.name
