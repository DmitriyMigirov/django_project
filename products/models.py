from django.db import models

from onlinestore.constants import MAX_DIGITS, DECIMAL_PLACES
from onlinestore.mixins.models_mixins import PKMixin
from os import path
from onlinestore.model_choices import  Currency
from django.core.cache import cache
from django_lifecycle import LifecycleModelMixin, hook, AFTER_CREATE, \
    AFTER_DELETE, AFTER_UPDATE, BEFORE_DELETE, AFTER_SAVE

DISCOUNT_CHOICES = (
    ("0", "В деньгах"),
    ("1", "Проценты"),

)


def upload_image(instance, filename):
    _name, extension = path.splitext(filename)
    return f'images/{instance.__class__.__name__.lower()}/' \
           f'{instance.pk}/image{extension}'


class Category(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/category')

    def __str__(self):
        return f'{self.name} | {self.description}'


class Product(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/product',
                              default='static/images/products/no_image.jpg')
    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    sku = models.CharField(
        max_length=64,
        blank=True,
        null=True)
    products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def _cache_key(self):
        return 'products'

    @classmethod
    def get_products(cls):
        products = cache.get(cls._cache_key())
        if not products:
            products = Product.objects.all()
            cache.set(cls._cache_key(), products)
        return products

    @hook(AFTER_SAVE)
    @hook(AFTER_DELETE)
    def clear_products_cache(self):
        cache.delete(self._cache_key())