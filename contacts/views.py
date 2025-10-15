from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer, ContactListSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing contacts.
    
    Provides CRUD operations for contacts with search and filtering.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'position']
    ordering_fields = ['first_name', 'last_name', 'created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        return ContactSerializer
    
    @action(detail=True, methods=['get'])
    def deals(self, request, pk=None):
        """Get all deals associated with this contact."""
        contact = self.get_object()
        deals = contact.deals.all()
        from deals.serializers import DealListSerializer
        serializer = DealListSerializer(deals, many=True)
        return Response(serializer.data)
