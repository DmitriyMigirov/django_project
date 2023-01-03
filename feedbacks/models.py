from django.contrib.auth.models import User
from django.db import models
from onlinestore.mixins.models_mixins import PKMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.cache import cache


class Feedback(PKMixin):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user.username} | {self.text} | {self.rating}'


def reformat_text(self):
    incoming_feedback = self
    checked_feedback = "".join(c for c in incoming_feedback if c.isalnum())
    self = checked_feedback
    return self


@classmethod
def _cache_key(cls):
    return 'feedbacks'


@classmethod
def get_feedbacks(cls):
    feedbacks = cache.get(cls._cache_key())
    if feedbacks:
        cache.delete(cls._cache_key())
    cache.set(cls._cache_key(), Feedback.objects.all())
    return cache.get(cls._cache_key())
