from django.contrib import admin
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'value', 'status', 'expected_close_date', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'company__name']
    ordering = ['-created_at']
