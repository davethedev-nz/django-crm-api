from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry', 'milestone', 'email', 'phone', 'created_at']
    list_filter = ['industry', 'milestone', 'created_at']
    search_fields = ['name', 'email', 'industry']
    ordering = ['name']
    
    def get_list_display(self, request):
        """Customize list display with milestone emoji."""
        return ['name', 'industry', 'milestone_with_emoji', 'email', 'phone', 'created_at']
    
    def milestone_with_emoji(self, obj):
        """Display milestone with emoji."""
        return obj.get_milestone_display_with_emoji()
    milestone_with_emoji.short_description = 'Milestone'
