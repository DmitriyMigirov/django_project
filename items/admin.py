from django.contrib import admin
from django.utils.safestring import mark_safe
from items.models import Item, Product, Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('render_item_image', 'name', 'created_at')
    list_filter = ('created_at',)


    def render_item_image(self, obj):
        if obj.image:
            return mark_safe((
                '<img src="{}" width="64" height="64" />'.format(
                obj.image.url)))
        return ''

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
    list_display = ('name', 'price', 'sku', 'created_at')
    list_filter = ('price',)
    readonly_fields = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...