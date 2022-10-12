from django.contrib import admin
from feedbacks.models import Feedback

@admin.register(Feedback)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created_at')
    list_filter = ('created_at',)
