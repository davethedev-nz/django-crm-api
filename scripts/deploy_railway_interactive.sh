#!/bin/bash
# Interactive Railway Deployment Guide

echo "🚀 Django CRM API - Railway Deployment"
echo "========================================"
echo ""
echo "Railway CLI is installed! ✅"
echo ""
echo "Let's deploy your app step by step..."
echo ""

# Step 1: Login
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: Login to Railway"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "This will open your browser for authentication."
echo ""
read -p "Press Enter to login to Railway..."

railway login

if [ $? -ne 0 ]; then
    echo "❌ Login failed. Please try again."
    exit 1
fi

echo ""
echo "✅ Logged in successfully!"
echo ""

# Step 2: Initialize project
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: Create Railway Project"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "You'll be asked to:"
echo "  1. Choose: Create new project"
echo "  2. Enter project name (e.g., django-crm-api)"
echo "  3. Confirm"
echo ""
read -p "Press Enter to create project..."

railway init

if [ $? -ne 0 ]; then
    echo "❌ Project creation failed."
    exit 1
fi

echo ""
echo "✅ Project created!"
echo ""

# Step 3: Link project (if needed)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 3: Add PostgreSQL Database"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
read -p "Press Enter to add PostgreSQL..."

railway add --plugin postgresql

if [ $? -ne 0 ]; then
    echo "⚠️  Database add may have failed, but we'll continue..."
fi

echo ""
echo "✅ Database added!"
echo ""

# Step 4: Set environment variables
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 4: Set Environment Variables"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Generating secure SECRET_KEY..."

# Generate SECRET_KEY
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

echo ""
echo "Setting variables..."
railway variables set SECRET_KEY="$SECRET_KEY"
railway variables set DEBUG="False"
railway variables set ALLOWED_HOSTS="*"

echo ""
echo "✅ Environment variables set!"
echo ""

# Step 5: Deploy
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 5: Deploy Application"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "This will:"
echo "  • Build your Docker container"
echo "  • Install dependencies"
echo "  • Run migrations"
echo "  • Start the server"
echo ""
echo "This may take 3-5 minutes..."
echo ""
read -p "Press Enter to start deployment..."

railway up

if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  Deployment may have issues. Check with: railway logs"
else
    echo ""
    echo "✅ Deployment initiated!"
fi

echo ""

# Step 6: Get domain
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 6: Generate Public URL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Generating a public domain for your app..."

railway domain

DOMAIN=$(railway domain 2>/dev/null || echo "")

if [ -n "$DOMAIN" ]; then
    echo ""
    echo "🌐 Your app is deployed at:"
    echo "   https://$DOMAIN"
    echo ""
    echo "Updating ALLOWED_HOSTS..."
    railway variables set ALLOWED_HOSTS="$DOMAIN,*.up.railway.app,*"
else
    echo ""
    echo "⚠️  Domain not generated yet. Run 'railway domain' manually."
fi

echo ""

# Final steps
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ DEPLOYMENT COMPLETE!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 Check deployment status:"
echo "   railway status"
echo ""
echo "📝 View logs:"
echo "   railway logs --follow"
echo ""
echo "🌐 Open in browser:"
echo "   railway open"
echo ""
echo "🧑‍💼 Create superuser:"
echo "   railway run python manage.py createsuperuser"
echo ""
echo "📊 Load sample data:"
echo "   railway run python manage.py populate_sample_data"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔄 To enable auto-deploy from GitHub:"
echo "   1. Get token: railway whoami"
echo "   2. Add to GitHub: gh secret set RAILWAY_TOKEN"
echo "   3. Push code: git push"
echo ""
echo "🎉 Your Django CRM API is LIVE!"
echo ""
