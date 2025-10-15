from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer, CompanyListSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing companies.
    
    Provides CRUD operations for companies with search and filtering.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'industry', 'email']
    ordering_fields = ['name', 'created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyListSerializer
        return CompanySerializer
    
    @action(detail=True, methods=['get'])
    def contacts(self, request, pk=None):
        """Get all contacts associated with this company."""
        company = self.get_object()
        contacts = company.contacts.all()
        from contacts.serializers import ContactListSerializer
        serializer = ContactListSerializer(contacts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def deals(self, request, pk=None):
        """Get all deals associated with this company."""
        company = self.get_object()
        deals = company.deals.all()
        from deals.serializers import DealListSerializer
        serializer = DealListSerializer(deals, many=True)
        return Response(serializer.data)
