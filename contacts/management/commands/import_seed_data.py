import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from companies.models import Company
from contacts.models import Contact


class Command(BaseCommand):
    help = 'Import seed data from CSV file (seed_data/test_data.csv)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before importing',
        )
        parser.add_argument(
            '--file',
            type=str,
            default='seed_data/test_data.csv',
            help='Path to CSV file (default: seed_data/test_data.csv)',
        )

    def handle(self, *args, **options):
        csv_file = options['file']
        clear_data = options['clear']
        
        # Build full path
        csv_path = os.path.join(settings.BASE_DIR, csv_file)
        
        # Check if file exists
        if not os.path.exists(csv_path):
            self.stdout.write(
                self.style.WARNING(f'CSV file not found: {csv_path}')
            )
            self.stdout.write(
                self.style.WARNING('Skipping seed data import.')
            )
            return
        
        # Clear existing data if requested
        if clear_data:
            self.stdout.write('Clearing existing data...')
            Contact.objects.all().delete()
            Company.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing data cleared'))
        
        # Check if data already exists
        if Company.objects.exists() and not clear_data:
            self.stdout.write(
                self.style.WARNING(
                    f'Database already contains {Company.objects.count()} companies. '
                    'Skipping import. Use --clear to force reimport.'
                )
            )
            return
        
        self.stdout.write(f'Importing seed data from {csv_path}...')
        
        companies_created = 0
        contacts_created = 0
        errors = 0
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                    try:
                        company_name = row.get('Company Name', '').strip()
                        contact_name = row.get('Contact Name', '').strip()
                        email = row.get('Email', '').strip()
                        phone = row.get('Phone Number', '').strip()
                        notes = row.get('Notes', '').strip()
                        
                        # Skip empty rows
                        if not company_name and not email:
                            continue
                        
                        # Create or get company
                        company = None
                        if company_name:
                            company, created = Company.objects.get_or_create(
                                name=company_name,
                                defaults={
                                    'milestone': 'not_contacted',
                                    'notes': notes if notes else None,
                                }
                            )
                            if created:
                                companies_created += 1
                                self.stdout.write(f'  ✓ Created company: {company_name}')
                        
                        # Create contact if email is provided
                        if email:
                            # Parse contact name into first and last name
                            first_name = ''
                            last_name = ''
                            if contact_name:
                                name_parts = contact_name.split(maxsplit=1)
                                first_name = name_parts[0]
                                last_name = name_parts[1] if len(name_parts) > 1 else ''
                            else:
                                # Use company name as fallback
                                first_name = company_name if company_name else 'Contact'
                                last_name = ''
                            
                            # Check if contact already exists
                            if not Contact.objects.filter(email=email).exists():
                                contact = Contact.objects.create(
                                    first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone if phone else None,
                                    company=company,
                                    notes=notes if notes else None,
                                )
                                contacts_created += 1
                                self.stdout.write(
                                    f'  ✓ Created contact: {contact.full_name} ({email})'
                                )
                            else:
                                self.stdout.write(
                                    self.style.WARNING(
                                        f'  - Skipped duplicate contact: {email}'
                                    )
                                )
                        
                    except Exception as e:
                        errors += 1
                        self.stdout.write(
                            self.style.ERROR(
                                f'  ✗ Error on row {row_num}: {str(e)}'
                            )
                        )
        
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to read CSV file: {str(e)}')
            )
            return
        
        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS('Import completed!'))
        self.stdout.write(self.style.SUCCESS(f'Companies created: {companies_created}'))
        self.stdout.write(self.style.SUCCESS(f'Contacts created: {contacts_created}'))
        if errors > 0:
            self.stdout.write(self.style.WARNING(f'Errors: {errors}'))
        self.stdout.write(self.style.SUCCESS('=' * 50))
