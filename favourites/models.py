from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product
from onlinestore.mixins.models_mixins import PKMixin


class Favourites(PKMixin):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
