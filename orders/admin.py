from django.contrib import admin

from orders.models import Order, Discount


@admin.register(Order)
class OrdersAdminRegister(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'discount')
    filter_horizontal = ('products',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    ...