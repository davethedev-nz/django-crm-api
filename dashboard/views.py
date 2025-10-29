from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import models
from django.db.models import Count, Q
from django.http import JsonResponse, HttpResponse
from companies.models import Company
from contacts.models import Contact
import json
import csv
import io


def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})


@login_required
def dashboard(request):
    """Dashboard view with milestone statistics."""
    # Get count of companies by milestone
    milestone_stats = []
    for milestone_key, milestone_label in Company.MILESTONE_CHOICES:
        count = Company.objects.filter(milestone=milestone_key).count()
        milestone_stats.append({
            'label': milestone_label,
            'count': count
        })
    
    # Get total counts for stats cards
    total_companies = Company.objects.count()
    successful_companies = Company.objects.filter(milestone='successful').count()
    active_companies = Company.objects.exclude(milestone__in=['successful', 'not_interested']).count()
    
    context = {
        'milestone_stats': json.dumps(milestone_stats),
        'total_companies': total_companies,
        'successful_companies': successful_companies,
        'active_companies': active_companies,
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
@ensure_csrf_cookie
def company_list(request):
    """View to list all companies."""
    # Get filter and search parameters
    milestone_filter = request.GET.get('milestone', '')
    search_query = request.GET.get('search', '')
    
    # Start with all companies and include primary_contact data
    companies = Company.objects.select_related('primary_contact').all()
    
    # Apply milestone filter
    if milestone_filter:
        companies = companies.filter(milestone=milestone_filter)
    
    # Apply search filter
    if search_query:
        companies = companies.filter(
            models.Q(name__icontains=search_query) |
            models.Q(industry__icontains=search_query) |
            models.Q(email__icontains=search_query)
        )
    
    # Get distinct industries for export dropdown
    industries = Company.objects.exclude(industry__isnull=True).exclude(industry='').values_list('industry', flat=True).distinct().order_by('industry')
    
    context = {
        'companies': companies,
        'milestone_choices': Company.MILESTONE_CHOICES,
        'current_milestone': milestone_filter,
        'search_query': search_query,
        'industries': industries,
    }
    return render(request, 'dashboard/company_list_table.html', context)


@login_required
def company_detail(request, pk):
    """View to show company details."""
    company = get_object_or_404(Company, pk=pk)
    
    context = {
        'company': company,
        'milestone_choices': Company.MILESTONE_CHOICES,
    }
    return render(request, 'dashboard/company_detail.html', context)


@login_required
def company_create(request):
    """View to create a new company."""
    if request.method == 'POST':
        company = Company(
            name=request.POST.get('name'),
            website=request.POST.get('website') or None,
            email=request.POST.get('email') or None,
            phone=request.POST.get('phone') or None,
            address=request.POST.get('address') or None,
            industry=request.POST.get('industry') or None,
            primary_contact_id=request.POST.get('primary_contact') or None,
            milestone=request.POST.get('milestone', 'not_contacted'),
            notes=request.POST.get('notes') or None,
        )
        company.save()
        return redirect('company_detail', pk=company.pk)
    
    contacts = Contact.objects.all().order_by('first_name', 'last_name')
    context = {
        'milestone_choices': Company.MILESTONE_CHOICES,
        'contacts': contacts,
    }
    return render(request, 'dashboard/company_form.html', context)


@login_required
def company_update(request, pk):
    """View to update a company."""
    company = get_object_or_404(Company, pk=pk)
    
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.website = request.POST.get('website') or None
        company.email = request.POST.get('email') or None
        company.phone = request.POST.get('phone') or None
        company.address = request.POST.get('address') or None
        company.industry = request.POST.get('industry') or None
        company.primary_contact_id = request.POST.get('primary_contact') or None
        company.milestone = request.POST.get('milestone')
        company.notes = request.POST.get('notes') or None
        company.save()
        return redirect('company_detail', pk=company.pk)
    
    contacts = Contact.objects.all().order_by('first_name', 'last_name')
    context = {
        'company': company,
        'milestone_choices': Company.MILESTONE_CHOICES,
        'contacts': contacts,
        'is_update': True,
    }
    return render(request, 'dashboard/company_form.html', context)


@login_required
def company_delete(request, pk):
    """View to delete a company."""
    company = get_object_or_404(Company, pk=pk)
    
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    
    context = {
        'company': company,
    }
    return render(request, 'dashboard/company_confirm_delete.html', context)


@login_required
def company_upload_csv(request):
    """View to upload companies from CSV file."""
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file:
            return JsonResponse({
                'success': False,
                'error': 'No file provided'
            }, status=400)
        
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({
                'success': False,
                'error': 'File must be a CSV'
            }, status=400)
        
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
                    
                    # Validate milestone if provided
                    milestone = row.get('milestone', 'not_contacted').strip()
                    if milestone and milestone not in dict(Company.MILESTONE_CHOICES):
                        milestone = 'not_contacted'
                    
                    # Check if company exists
                    company, created = Company.objects.get_or_create(
                        name=name,
                        defaults={
                            'website': row.get('website', '').strip() or None,
                            'email': row.get('email', '').strip() or None,
                            'phone': row.get('phone', '').strip() or None,
                            'address': row.get('address', '').strip() or None,
                            'industry': row.get('industry', '').strip() or None,
                            'milestone': milestone,
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
                            milestone_val = row.get('milestone').strip()
                            if milestone_val in dict(Company.MILESTONE_CHOICES):
                                company.milestone = milestone_val
                        if row.get('notes'):
                            company.notes = row.get('notes').strip()
                        company.save()
                        updated_count += 1
                        
                except Exception as e:
                    errors.append(f"Row {row_num}: {str(e)}")
            
            return JsonResponse({
                'success': True,
                'message': 'CSV upload completed',
                'created': created_count,
                'updated': updated_count,
                'errors': errors
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error processing CSV: {str(e)}'
            }, status=400)
    
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    }, status=405)


@login_required
def company_export_csv(request):
    """Export companies to CSV based on current filters (milestone and search)."""
    from datetime import datetime
    
    # Get filter parameters (same as list view)
    milestone_filter = request.GET.get('milestone', '')
    search_query = request.GET.get('search', '')
    
    # Start with all companies, ordered by industry for grouping
    companies = Company.objects.all().order_by('industry', 'name')
    
    # Apply milestone filter
    if milestone_filter:
        companies = companies.filter(milestone=milestone_filter)
    
    # Apply search filter
    if search_query:
        companies = companies.filter(
            models.Q(name__icontains=search_query) |
            models.Q(industry__icontains=search_query) |
            models.Q(email__icontains=search_query)
        )
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create CSV response with timestamped filename
    filename = f'companies_export_{timestamp}.csv'
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    writer = csv.writer(response)
    
    # Write export metadata as a single info row (will appear as first data row in spreadsheets)
    export_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total_records = companies.count()
    
    # Build filter info
    filter_info = []
    if milestone_filter:
        milestone_display = dict(Company.MILESTONE_CHOICES).get(milestone_filter, milestone_filter)
        filter_info.append(f'Milestone: {milestone_display}')
    if search_query:
        filter_info.append(f'Search: "{search_query}"')
    
    filters_text = '; '.join(filter_info) if filter_info else 'None (All companies)'
    
    # Write metadata row
    writer.writerow([
        f'EXPORT INFO - Generated: {export_date}',
        f'Total Records: {total_records}',
        f'Filters: {filters_text}',
        '', '', '', '', '', '', '', ''
    ])
    
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
    for company in companies:
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


# Contact Views

@login_required
def contact_list(request):
    """View to list all contacts."""
    # Get filter and search parameters
    company_filter = request.GET.get('company', '')
    search_query = request.GET.get('search', '')
    
    # Start with all contacts
    contacts = Contact.objects.select_related('company').all()
    
    # Apply company filter
    if company_filter:
        contacts = contacts.filter(company_id=company_filter)
    
    # Apply search filter
    if search_query:
        contacts = contacts.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(position__icontains=search_query) |
            Q(company__name__icontains=search_query)
        )
    
    # Get all companies for filter dropdown
    companies = Company.objects.all().order_by('name')
    
    context = {
        'contacts': contacts,
        'companies': companies,
        'current_company': company_filter,
        'search_query': search_query,
    }
    return render(request, 'dashboard/contact_list_table.html', context)


@login_required
def contact_detail(request, pk):
    """View to show contact details."""
    contact = get_object_or_404(Contact.objects.select_related('company'), pk=pk)
    
    context = {
        'contact': contact,
    }
    return render(request, 'dashboard/contact_detail.html', context)


@login_required
def contact_create(request):
    """View to create a new contact."""
    if request.method == 'POST':
        contact = Contact(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone') or None,
            position=request.POST.get('position') or None,
            company_id=request.POST.get('company') or None,
            notes=request.POST.get('notes') or None,
        )
        contact.save()
        return redirect('contact_detail', pk=contact.pk)
    
    # Get company from query parameter if provided
    company_id = request.GET.get('company')
    
    companies = Company.objects.all().order_by('name')
    context = {
        'companies': companies,
        'preselected_company': company_id,
    }
    return render(request, 'dashboard/contact_form.html', context)


@login_required
def contact_update(request, pk):
    """View to update a contact."""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone') or None
        contact.position = request.POST.get('position') or None
        contact.company_id = request.POST.get('company') or None
        contact.notes = request.POST.get('notes') or None
        contact.save()
        return redirect('contact_detail', pk=contact.pk)
    
    companies = Company.objects.all().order_by('name')
    context = {
        'contact': contact,
        'companies': companies,
        'is_update': True,
    }
    return render(request, 'dashboard/contact_form.html', context)


@login_required
def contact_delete(request, pk):
    """View to delete a contact."""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    
    context = {
        'contact': contact,
    }
    return render(request, 'dashboard/contact_confirm_delete.html', context)


@login_required
def company_update_milestone(request, pk):
    """AJAX endpoint to update company milestone."""
    from django.http import JsonResponse
    import json
    
    if request.method == 'POST':
        try:
            company = get_object_or_404(Company, pk=pk)
            
            # Parse JSON body
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError as e:
                return JsonResponse({'error': f'Invalid JSON: {str(e)}'}, status=400)
            
            milestone = data.get('milestone')
            
            if not milestone:
                return JsonResponse({'error': 'Milestone field is required'}, status=400)
            
            # Validate milestone
            valid_milestones = [choice[0] for choice in Company.MILESTONE_CHOICES]
            if milestone not in valid_milestones:
                return JsonResponse({
                    'error': f'Invalid milestone value. Valid options: {", ".join(valid_milestones)}'
                }, status=400)
            
            # Update the milestone
            company.milestone = milestone
            company.save()
            
            return JsonResponse({
                'success': True,
                'milestone': milestone,
                'milestone_display': company.get_milestone_display()
            })
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Error updating milestone: {error_details}")  # Log to console
            return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
