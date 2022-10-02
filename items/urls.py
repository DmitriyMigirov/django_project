from django.urls import path

from items.views import index

urlpatterns = [
    path('', index, name='index'),
]