from rest_framework import viewsets, filters
from .models import Deal
from .serializers import DealSerializer, DealListSerializer


class DealViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing deals.
    
    Provides CRUD operations for deals with filtering by status.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'company__name']
    ordering_fields = ['value', 'expected_close_date', 'created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DealListSerializer
        return DealSerializer
    
    def get_queryset(self):
        queryset = Deal.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset
