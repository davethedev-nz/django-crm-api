from django.db import models


class Company(models.Model):
    """Model representing a company in the CRM system."""
    
    # Milestone choices for lead journey
    MILESTONE_CHOICES = [
        ('not_contacted', 'Not yet contacted'),
        ('first_call', 'First Call'),
        ('not_interested', 'Not interested'),
        ('email_sent', 'Email sent'),
        ('meeting_arranged', 'Meeting arranged'),
        ('waiting_on_contact', 'Waiting on Contact'),
        ('successful', 'Successful'),
    ]
    
    name = models.CharField(max_length=200, unique=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    primary_contact = models.ForeignKey(
        'contacts.Contact',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='primary_for_companies',
        help_text='Primary contact person for this company'
    )
    milestone = models.CharField(
        max_length=50,
        choices=MILESTONE_CHOICES,
        default='not_contacted',
        help_text='Current stage in the lead journey'
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.name
    
    def get_milestone_display_with_emoji(self):
        """Get milestone display with emoji indicator."""
        emoji_map = {
            'not_contacted': '⚪',
            'first_call': '🔵',
            'not_interested': '🔴',
            'email_sent': '📧',
            'meeting_arranged': '📅',
            'waiting_on_contact': '⏳',
            'successful': '✅',
        }
        emoji = emoji_map.get(self.milestone, '⚪')
        return f"{emoji} {self.get_milestone_display()}"
