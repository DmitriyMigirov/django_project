from django.contrib import admin
from items.models import Name, Category, Product, Discount

admin.site.register(Name)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
