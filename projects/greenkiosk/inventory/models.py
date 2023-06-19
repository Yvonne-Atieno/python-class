from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
