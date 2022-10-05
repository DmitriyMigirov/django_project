from django.db.models import IntegerChoices


class DiscountTypes(IntegerChoices):
    VALUE = 0, 'Value'
    PERCENTS = 1, 'Percents'
