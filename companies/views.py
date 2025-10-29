from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
import csv
import io
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
    
    @action(detail=False, methods=['post'])
    def upload_csv(self, request):
        """Upload companies from CSV file."""
        csv_file = request.FILES.get('file')
        
        if not csv_file:
            return Response(
                {'error': 'No file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not csv_file.name.endswith('.csv'):
            return Response(
                {'error': 'File must be a CSV'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Read CSV file
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)
            
            created_count = 0
            updated_count = 0
            errors = []
            
            for row_num, row in enumerate(reader, start=2):
                try:
                    # Get company name (required field)
                    name = row.get('name', '').strip()
                    if not name:
                        errors.append(f"Row {row_num}: Company name is required")
                        continue
                    
                    # Check if company exists
                    company, created = Company.objects.get_or_create(
                        name=name,
                        defaults={
                            'website': row.get('website', '').strip() or None,
                            'email': row.get('email', '').strip() or None,
                            'phone': row.get('phone', '').strip() or None,
                            'address': row.get('address', '').strip() or None,
                            'industry': row.get('industry', '').strip() or None,
                            'milestone': row.get('milestone', 'not_contacted').strip(),
                            'notes': row.get('notes', '').strip() or None,
                        }
                    )
                    
                    if created:
                        created_count += 1
                    else:
                        # Update existing company
                        if row.get('website'):
                            company.website = row.get('website').strip()
                        if row.get('email'):
                            company.email = row.get('email').strip()
                        if row.get('phone'):
                            company.phone = row.get('phone').strip()
                        if row.get('address'):
                            company.address = row.get('address').strip()
                        if row.get('industry'):
                            company.industry = row.get('industry').strip()
                        if row.get('milestone'):
                            milestone = row.get('milestone').strip()
                            if milestone in dict(Company.MILESTONE_CHOICES):
                                company.milestone = milestone
                        if row.get('notes'):
                            company.notes = row.get('notes').strip()
                        company.save()
                        updated_count += 1
                        
                except Exception as e:
                    errors.append(f"Row {row_num}: {str(e)}")
            
            return Response({
                'message': 'CSV upload completed',
                'created': created_count,
                'updated': updated_count,
                'errors': errors
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Error processing CSV: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        """Export companies to CSV, grouped by industry."""
        # Get queryset with any applied filters
        queryset = self.filter_queryset(self.get_queryset()).order_by('industry', 'name')
        
        # Create CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="companies_export.csv"'
        
        writer = csv.writer(response)
        
        # Write header
        writer.writerow([
            'Industry',
            'Company Name',
            'Website',
            'Email',
            'Phone',
            'Address',
            'Milestone',
            'Milestone Status',
            'Notes',
            'Created Date',
            'Updated Date'
        ])
        
        # Group companies by industry and write rows
        current_industry = None
        for company in queryset:
            industry = company.industry or 'No Industry Specified'
            
            # Add a blank row between industry groups for readability
            if current_industry is not None and current_industry != industry:
                writer.writerow([])  # Blank row
            
            current_industry = industry
            
            writer.writerow([
                industry,
                company.name,
                company.website or '',
                company.email or '',
                company.phone or '',
                company.address or '',
                company.milestone,
                company.get_milestone_display(),
                company.notes or '',
                company.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                company.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            ])
        
        return response
