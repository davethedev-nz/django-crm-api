from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Company model."""
    
    contacts_count = serializers.SerializerMethodField()
    deals_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'website', 'email', 'phone', 'address',
            'industry', 'notes', 'contacts_count', 'deals_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_contacts_count(self, obj):
        return obj.contacts.count()
    
    def get_deals_count(self, obj):
        return obj.deals.count()


class CompanyListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing companies."""
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'industry', 'email', 'phone']
