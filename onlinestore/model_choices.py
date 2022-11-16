from django.db.models import IntegerChoices, TextChoices


class DiscountTypes(IntegerChoices):
    VALUE = 0, 'Value'
    PERCENTS = 1, 'Percents'


class Currency(TextChoices):
    UAH = 'UAH', 'UAH'
    USD = 'USD', 'USD'
    EUR = 'EUR', 'EUR'