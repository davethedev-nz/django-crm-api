from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company
from .serializers import CompanySerializer, CompanyListSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing companies.
    
    Provides CRUD operations for companies with search and filtering.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'industry', 'email']
    ordering_fields = ['name', 'created_at', 'milestone']
    filterset_fields = ['milestone', 'industry']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyListSerializer
        return CompanySerializer
    
    @action(detail=True, methods=['post'])
    def update_milestone(self, request, pk=None):
        """Update the milestone status of a company."""
        company = self.get_object()
        milestone = request.data.get('milestone')
        
        if milestone not in dict(Company.MILESTONE_CHOICES):
            return Response(
                {'error': 'Invalid milestone value'},
                status=400
            )
        
        company.milestone = milestone
        company.save()
        serializer = self.get_serializer(company)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_milestone(self, request):
        """Get companies grouped by milestone."""
        milestone_data = {}
        for milestone_key, milestone_label in Company.MILESTONE_CHOICES:
            companies = Company.objects.filter(milestone=milestone_key)
            milestone_data[milestone_key] = {
                'label': milestone_label,
                'count': companies.count(),
                'companies': CompanyListSerializer(companies, many=True).data
            }
        return Response(milestone_data)
    
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
