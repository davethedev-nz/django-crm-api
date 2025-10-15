from rest_framework import serializers
from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    """Serializer for Deal model."""
    
    company_name = serializers.CharField(source='company.name', read_only=True)
    contact_name = serializers.CharField(source='contact.full_name', read_only=True)
    
    class Meta:
        model = Deal
        fields = [
            'id', 'title', 'description', 'value', 'status',
            'company', 'company_name', 'contact', 'contact_name',
            'expected_close_date', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class DealListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing deals."""
    
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = Deal
        fields = ['id', 'title', 'value', 'status', 'company_name', 'expected_close_date']
