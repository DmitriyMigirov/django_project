import re

from django.db import models
from django.contrib.auth import get_user_model
from onlinestore.mixins.models_mixins import PKMixin
from django.core.validators import MinValueValidator, MaxValueValidator



class Feedback(PKMixin):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(5))
    )


def reformat_text(self):
    incoming_feedback = self
    checked_feedback = "".join(c for c in incoming_feedback if c.isalnum())
    self = checked_feedback
    return self
