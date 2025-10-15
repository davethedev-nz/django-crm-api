#!/bin/bash
# Local development startup script
# This script runs migrations, imports seed data, and starts the dev server

echo "🚀 Starting Django CRM Development Server"
echo "=========================================="
echo ""

# Run migrations
echo "📦 Running migrations..."
python manage.py migrate

# Import seed data (will skip if data already exists)
echo ""
echo "🌱 Importing seed data..."
python manage.py import_seed_data

# Start development server
echo ""
echo "🌐 Starting development server on http://127.0.0.1:8000"
echo "   Press CTRL+C to stop"
echo ""
python manage.py runserver
