from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Company URLs
    path('companies/', views.company_list, name='company_list'),
    path('companies/new/', views.company_create, name='company_create'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('companies/<int:pk>/edit/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),
    path('companies/<int:pk>/update-milestone/', views.company_update_milestone, name='company_update_milestone'),
    
    # Contact URLs
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/new/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/edit/', views.contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]
