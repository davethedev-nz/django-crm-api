from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
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
    
    context = {
        'milestone_stats': json.dumps(milestone_stats),
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)
