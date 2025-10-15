from django.core.management.base import BaseCommand
from companies.models import Company
from contacts.models import Contact
from deals.models import Deal
from decimal import Decimal
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample CRM data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create Companies
        companies_data = [
            {
                'name': 'Tech Solutions Inc',
                'website': 'https://techsolutions.example.com',
                'email': 'info@techsolutions.example.com',
                'phone': '+1-555-0101',
                'industry': 'Technology',
                'address': '123 Tech Street, San Francisco, CA 94105',
            },
            {
                'name': 'Global Marketing Co',
                'website': 'https://globalmarketing.example.com',
                'email': 'contact@globalmarketing.example.com',
                'phone': '+1-555-0102',
                'industry': 'Marketing',
                'address': '456 Market Ave, New York, NY 10001',
            },
            {
                'name': 'Finance Pro LLC',
                'website': 'https://financepro.example.com',
                'email': 'hello@financepro.example.com',
                'phone': '+1-555-0103',
                'industry': 'Finance',
                'address': '789 Wall Street, New York, NY 10005',
            },
        ]

        companies = []
        for company_data in companies_data:
            company, created = Company.objects.get_or_create(
                name=company_data['name'],
                defaults=company_data
            )
            companies.append(company)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created company: {company.name}'))

        # Create Contacts
        contacts_data = [
            {
                'first_name': 'John',
                'last_name': 'Smith',
                'email': 'john.smith@techsolutions.example.com',
                'phone': '+1-555-1001',
                'position': 'CEO',
                'company': companies[0],
            },
            {
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'email': 'sarah.johnson@techsolutions.example.com',
                'phone': '+1-555-1002',
                'position': 'CTO',
                'company': companies[0],
            },
            {
                'first_name': 'Michael',
                'last_name': 'Brown',
                'email': 'michael.brown@globalmarketing.example.com',
                'phone': '+1-555-1003',
                'position': 'Marketing Director',
                'company': companies[1],
            },
            {
                'first_name': 'Emily',
                'last_name': 'Davis',
                'email': 'emily.davis@financepro.example.com',
                'phone': '+1-555-1004',
                'position': 'CFO',
                'company': companies[2],
            },
        ]

        contacts = []
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(
                email=contact_data['email'],
                defaults=contact_data
            )
            contacts.append(contact)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created contact: {contact.full_name}'))

        # Create Deals
        deals_data = [
            {
                'title': 'Enterprise Software License',
                'description': 'Annual enterprise software license for 100 users',
                'value': Decimal('50000.00'),
                'status': 'proposal',
                'company': companies[0],
                'contact': contacts[0],
                'expected_close_date': date.today() + timedelta(days=30),
            },
            {
                'title': 'Marketing Campaign Q4',
                'description': 'Complete marketing campaign for Q4 product launch',
                'value': Decimal('75000.00'),
                'status': 'negotiation',
                'company': companies[1],
                'contact': contacts[2],
                'expected_close_date': date.today() + timedelta(days=45),
            },
            {
                'title': 'Financial Consulting Services',
                'description': 'Six-month financial consulting engagement',
                'value': Decimal('120000.00'),
                'status': 'qualified',
                'company': companies[2],
                'contact': contacts[3],
                'expected_close_date': date.today() + timedelta(days=60),
            },
            {
                'title': 'Cloud Infrastructure Setup',
                'description': 'Initial cloud infrastructure setup and migration',
                'value': Decimal('35000.00'),
                'status': 'lead',
                'company': companies[0],
                'contact': contacts[1],
                'expected_close_date': date.today() + timedelta(days=90),
            },
        ]

        for deal_data in deals_data:
            deal, created = Deal.objects.get_or_create(
                title=deal_data['title'],
                company=deal_data['company'],
                defaults=deal_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created deal: {deal.title}'))

        self.stdout.write(self.style.SUCCESS('\nSample data created successfully!'))
        self.stdout.write(f'  Companies: {Company.objects.count()}')
        self.stdout.write(f'  Contacts: {Contact.objects.count()}')
        self.stdout.write(f'  Deals: {Deal.objects.count()}')
