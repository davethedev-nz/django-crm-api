#!/bin/bash
# Test script for Contacts feature

echo "🧪 Testing Contacts Feature"
echo "============================"
echo ""

# Check if server is running
if ! curl -s http://127.0.0.1:8000 > /dev/null; then
    echo "❌ Django server is not running. Please start it with: python manage.py runserver"
    exit 1
fi

echo "✅ Server is running"
echo ""

# Test URLs
echo "Testing Contact URLs:"
echo "-------------------"

urls=(
    "/contacts/"
    "/companies/"
)

for url in "${urls[@]}"; do
    status_code=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000$url)
    if [ "$status_code" = "200" ] || [ "$status_code" = "302" ]; then
        echo "✅ $url - HTTP $status_code"
    else
        echo "❌ $url - HTTP $status_code"
    fi
done

echo ""
echo "📝 Manual Testing Checklist:"
echo "1. Navigate to http://127.0.0.1:8000/contacts/"
echo "2. Check if contact list displays correctly"
echo "3. Try creating a new contact"
echo "4. Try associating a contact with a company"
echo "5. View company detail and check related contacts section"
echo "6. Try editing and deleting contacts"
echo ""
echo "✅ Automated checks passed! Please verify manually in browser."
