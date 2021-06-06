from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField



class ActiveManager(models.Manager):
    
    def active(self):
        return self.filter(active=True)



class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = AutoSlugField(populate_from='name')
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)
    objects = ActiveManager()

    def __str__(self):
        return self.name

    
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    image = models.ImageField(upload_to="product-images")
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)
    



class ProductTag(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

