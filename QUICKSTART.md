# Quick Start Guide

## Getting Started

Your Django CRM API is ready to use! Follow these steps:

### 1. Create a Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin user.

### 2. Populate Sample Data (Optional)

```bash
python manage.py populate_sample_data
```

This will create sample companies, contacts, and deals for testing.

### 3. Start the Development Server

You can start the server in two ways:

**Option A: Using VS Code Task**
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Type "Tasks: Run Task"
- Select "Run Django Server"

**Option B: Using Terminal**
```bash
python manage.py runserver
```

### 4. Access the Application

- **API Root**: http://localhost:8000/api/
- **Admin Interface**: http://localhost:8000/admin/
- **Contacts API**: http://localhost:8000/api/contacts/
- **Companies API**: http://localhost:8000/api/companies/
- **Deals API**: http://localhost:8000/api/deals/

## Testing the API

### Using Browser
Simply visit any of the API endpoints in your browser. Django REST Framework provides a browsable API interface.

### Using curl

**List all contacts:**
```bash
curl http://localhost:8000/api/contacts/
```

**Create a new company:**
```bash
curl -X POST http://localhost:8000/api/companies/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Company", "industry": "Technology"}'
```

**Get a specific contact:**
```bash
curl http://localhost:8000/api/contacts/1/
```

### Using httpie

```bash
# Install httpie
pip install httpie

# List contacts
http http://localhost:8000/api/contacts/

# Create a deal
http POST http://localhost:8000/api/deals/ \
  title="New Deal" \
  value=10000 \
  status=lead \
  company=1
```

## API Features

### Search
Add `?search=query` to search endpoints:
```
http://localhost:8000/api/contacts/?search=john
```

### Ordering
Add `?ordering=field` to sort results:
```
http://localhost:8000/api/deals/?ordering=-value
```

### Filtering
Filter deals by status:
```
http://localhost:8000/api/deals/?status=proposal
```

### Related Data
Get related records:
```
http://localhost:8000/api/companies/1/contacts/
http://localhost:8000/api/companies/1/deals/
http://localhost:8000/api/contacts/1/deals/
```

## Development Tips

### Django Shell
Access Django shell for quick testing:
```bash
python manage.py shell
```

### Database Inspection
```bash
python manage.py dbshell
```

### Create New Migrations
After model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests
```bash
python manage.py test
```

## Troubleshooting

### Port Already in Use
If port 8000 is busy, specify a different port:
```bash
python manage.py runserver 8080
```

### Database Issues
Reset the database (⚠️ deletes all data):
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_sample_data
```

## Next Steps

1. ✅ Create superuser
2. ✅ Run server
3. ✅ Load sample data
4. 🔨 Test API endpoints
5. 🔨 Explore admin interface
6. 🔨 Build your own features!

Happy coding! 🚀
