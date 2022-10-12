from django.shortcuts import render

from items.models import Item


def items(request, *args, **kwargs):
    context = {
        'items': Item.objects.only('name').all()
    }
    return render(request, 'items/index.html', context=context)
