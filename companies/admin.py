from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry', 'email', 'phone', 'created_at']
    list_filter = ['industry', 'created_at']
    search_fields = ['name', 'email', 'industry']
    ordering = ['name']
