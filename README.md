# Django CRM API

A simple yet powerful CRM (Customer Relationship Management) REST API built with Django and Django REST Framework.

## Features

- **Contacts Management**: Create, read, update, and delete contact information
- **Companies Management**: Manage company/organization details
- **Deals Management**: Track sales opportunities and deals
- **RESTful API**: Full-featured REST API with proper HTTP methods
- **Admin Interface**: Django admin panel for easy data management
- **Search & Filtering**: Search and filter across all entities
- **Relationships**: Link contacts to companies and deals

## Project Structure

```
ai_test_loop/
├── contacts/           # Contacts app
│   ├── models.py      # Contact model
│   ├── serializers.py # Contact serializers
│   ├── views.py       # Contact viewsets
│   └── urls.py        # Contact URLs
├── companies/         # Companies app
│   ├── models.py      # Company model
│   ├── serializers.py # Company serializers
│   ├── views.py       # Company viewsets
│   └── urls.py        # Company URLs
├── deals/             # Deals app
│   ├── models.py      # Deal model
│   ├── serializers.py # Deal serializers
│   ├── views.py       # Deal viewsets
│   └── urls.py        # Deal URLs
├── crm_project/       # Main project directory
│   ├── settings.py    # Project settings
│   └── urls.py        # Main URL configuration
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## Installation

1. **Ensure Python environment is activated** (already configured)

2. **Install dependencies** (already installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Contacts
- `GET /api/contacts/` - List all contacts
- `POST /api/contacts/` - Create a new contact
- `GET /api/contacts/{id}/` - Retrieve a contact
- `PUT /api/contacts/{id}/` - Update a contact
- `PATCH /api/contacts/{id}/` - Partial update a contact
- `DELETE /api/contacts/{id}/` - Delete a contact
- `GET /api/contacts/{id}/deals/` - Get deals for a contact

### Companies
- `GET /api/companies/` - List all companies
- `POST /api/companies/` - Create a new company
- `GET /api/companies/{id}/` - Retrieve a company
- `PUT /api/companies/{id}/` - Update a company
- `PATCH /api/companies/{id}/` - Partial update a company
- `DELETE /api/companies/{id}/` - Delete a company
- `GET /api/companies/{id}/contacts/` - Get contacts for a company
- `GET /api/companies/{id}/deals/` - Get deals for a company

### Deals
- `GET /api/deals/` - List all deals
- `POST /api/deals/` - Create a new deal
- `GET /api/deals/{id}/` - Retrieve a deal
- `PUT /api/deals/{id}/` - Update a deal
- `PATCH /api/deals/{id}/` - Partial update a deal
- `DELETE /api/deals/{id}/` - Delete a deal
- `GET /api/deals/?status={status}` - Filter deals by status

### Deal Status Options
- `lead` - Lead
- `qualified` - Qualified
- `proposal` - Proposal
- `negotiation` - Negotiation
- `closed_won` - Closed Won
- `closed_lost` - Closed Lost

## Admin Interface

Access the Django admin interface at: `http://localhost:8000/admin/`

Log in with the superuser credentials you created.

## API Authentication

Currently configured with Session Authentication. You can extend it with:
- Token Authentication
- JWT Authentication
- OAuth2

## Search & Filtering

All endpoints support search functionality:
- Contacts: Search by name, email, phone, position
- Companies: Search by name, industry, email
- Deals: Search by title, description, company name

## Development

### Running Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Creating Sample Data
Use the Django admin interface or Django shell to create sample data:
```bash
python manage.py shell
```

## Technology Stack

- **Django 5.2.7** - Web framework
- **Django REST Framework 3.15.2** - REST API toolkit
- **django-cors-headers 4.5.0** - CORS support
- **SQLite** - Default database (can be changed to PostgreSQL, MySQL, etc.)

## Next Steps

1. Add authentication and authorization
2. Implement unit tests
3. Add API documentation (Swagger/OpenAPI)
4. Add more filtering options
5. Implement email notifications
6. Add activity logging
7. Create frontend application

## License

This project is open source and available for educational purposes.
