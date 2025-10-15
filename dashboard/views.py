from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.db.models import Count, Q
from companies.models import Company
from contacts.models import Contact
import json


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
def company_list(request):
    """View to list all companies."""
    # Get filter and search parameters
    milestone_filter = request.GET.get('milestone', '')
    search_query = request.GET.get('search', '')
    
    # Start with all companies
    companies = Company.objects.all()
    
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
    
    context = {
        'companies': companies,
        'milestone_choices': Company.MILESTONE_CHOICES,
        'current_milestone': milestone_filter,
        'search_query': search_query,
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
            milestone=request.POST.get('milestone', 'not_contacted'),
            notes=request.POST.get('notes') or None,
        )
        company.save()
        return redirect('company_detail', pk=company.pk)
    
    context = {
        'milestone_choices': Company.MILESTONE_CHOICES,
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
        company.milestone = request.POST.get('milestone')
        company.notes = request.POST.get('notes') or None
        company.save()
        return redirect('company_detail', pk=company.pk)
    
    context = {
        'company': company,
        'milestone_choices': Company.MILESTONE_CHOICES,
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
    if request.method == 'POST':
        import json
        from django.http import JsonResponse
        
        try:
            company = get_object_or_404(Company, pk=pk)
            data = json.loads(request.body)
            milestone = data.get('milestone')
            
            # Validate milestone
            valid_milestones = [choice[0] for choice in Company.MILESTONE_CHOICES]
            if milestone not in valid_milestones:
                return JsonResponse({'error': 'Invalid milestone'}, status=400)
            
            company.milestone = milestone
            company.save()
            
            return JsonResponse({
                'success': True,
                'milestone': milestone,
                'milestone_display': company.get_milestone_display()
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
