from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.db.models import Count
from companies.models import Company
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
    return render(request, 'dashboard/company_list.html', context)


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
