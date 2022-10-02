from django.db import models

DISCOUNT_CHOICES = (
    ("0", "В деньгах"),
    ("1", "Проценты"),

)

class Name(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    price = models.PositiveIntegerField()
    sku = models.CharField(max_length=255)

class Discount(models.Model):
    amount = models.PositiveIntegerField(null=True, blank=True)
    code  = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    discount_type = models.PositiveIntegerField(
        choices = DISCOUNT_CHOICES,
        default = '0'
        )
