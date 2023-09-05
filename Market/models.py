from django.db import models


class Product(models.Model):
    Name = models.CharField(max_length=64)
    Description = models.TextField()
    Tag = models.CharField(max_length=32)
    Price = models.IntegerField()
    Image = models.ImageField(upload_to="ProductImage/")
