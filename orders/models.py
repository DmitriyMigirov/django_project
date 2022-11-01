from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django_lifecycle import LifecycleModel, hook, BEFORE_SAVE, AFTER_UPDATE


from onlinestore.constants import MAX_DIGITS, DECIMAL_PLACES
from onlinestore.mixins.models_mixins import PKMixin
from onlinestore.model_choices import DiscountTypes


class Discount(PKMixin):
    amount = models.DecimalField(max_digits=MAX_DIGITS,
                                 decimal_places=DECIMAL_PLACES,
                                 default=0)
    code = models.CharField(
        max_length=30)
    is_active = models.BooleanField(
        default=True)
    discount_type = models.PositiveSmallIntegerField(
        choices=DiscountTypes.choices,
        default=DiscountTypes.VALUE)

    def __str__(self):
        return f'{self.code} | {self.amount} | {self.is_active}'


class Order(PKMixin):
    total_amount = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    products = models.ManyToManyField('products.Product')
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    def count_total_amount(self):
        if self.discount:
            if self.discount.discount_type == DiscountTypes.VALUE:
                return (self.total_amount - self.discount.amount).quantize(
                    Decimal('.00'))
            elif self.discount.discount_type == DiscountTypes.PERCENTS:
                return (self.total_amount - ((self.total_amount * self.discount.amount) / 100)).quantize(Decimal('.00')) # noqa
        return self.total_amount

    @hook(BEFORE_SAVE)
    def order_after_save(self):
        self.total_amount = 0
        for product in self.products.all():
            self.total_amount += product.price

    @hook(AFTER_UPDATE)
    def order_after_update(self):
        if self.discount:
            self.total_amount = self.count_total_amount()
            self.save(update_fields=('total_amount',), skip_hooks=True)


