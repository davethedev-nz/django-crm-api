from rest_framework import serializers
from .models import Company


class PrimaryContactSerializer(serializers.Serializer):
    """Serializer for primary contact nested in Company."""
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    position = serializers.CharField(read_only=True)


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Company model."""
    
    contacts_count = serializers.SerializerMethodField()
    deals_count = serializers.SerializerMethodField()
    milestone_display = serializers.CharField(source='get_milestone_display', read_only=True)
    primary_contact_detail = PrimaryContactSerializer(source='primary_contact', read_only=True)
    
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'website', 'email', 'phone', 'address',
            'industry', 'primary_contact', 'primary_contact_detail',
            'milestone', 'milestone_display', 'notes', 
            'contacts_count', 'deals_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_contacts_count(self, obj):
        return obj.contacts.count()
    
    def get_deals_count(self, obj):
        return obj.deals.count()


class CompanyListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing companies."""
    
    milestone_display = serializers.CharField(source='get_milestone_display', read_only=True)
    primary_contact_name = serializers.CharField(source='primary_contact.full_name', read_only=True)
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'industry', 'primary_contact_name', 'milestone', 'milestone_display']
