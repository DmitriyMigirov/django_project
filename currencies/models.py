from django.db import models

from onlinestore.constants import DECIMAL_PLACES, MAX_DIGITS
from onlinestore.mixins.models_mixins import PKMixin
from onlinestore.model_choices import Currency


class CurrencyHistory(PKMixin):
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    buy = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )
    sale = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )

    def __str__(self):
        return f'{self.currency} | {self.created_at} |{self.buy} | {self.sale}'

    def __str__(self):
        return f'{self.currency} | {self.created_at} |{self.buy} | {self.sale}'