#!/bin/bash
# Quick Deploy Setup Script for Railway

echo "🚀 Django CRM API - Railway Deployment Setup"
echo "=============================================="
echo ""

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
    echo "✅ Railway CLI installed"
else
    echo "✅ Railway CLI already installed"
fi

echo ""
echo "🔐 Step 1: Login to Railway"
echo "This will open a browser window..."
read -p "Press Enter to continue..."
railway login

echo ""
echo "✅ Logged in successfully!"
echo ""

echo "🏗️  Step 2: Create Railway Project"
echo "Choose a name for your project (e.g., django-crm-api)"
railway init

echo ""
echo "✅ Project created!"
echo ""

echo "🗄️  Step 3: Add PostgreSQL Database"
echo "This will provision a PostgreSQL database..."
railway add --plugin postgresql

echo ""
echo "✅ Database added!"
echo ""

echo "🔧 Step 4: Set Environment Variables"
echo ""
echo "Setting production environment variables..."

# Generate a secure SECRET_KEY
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

railway variables set SECRET_KEY="$SECRET_KEY"
railway variables set DEBUG="False"
railway variables set ALLOWED_HOSTS="*"  # Will be updated after deployment

echo "✅ Environment variables set!"
echo ""

echo "🚀 Step 5: Deploy to Railway"
echo "This will build and deploy your application..."
echo ""
read -p "Ready to deploy? Press Enter to continue..."

railway up

echo ""
echo "✅ Deployment complete!"
echo ""

# Get the deployment URL
RAILWAY_URL=$(railway domain)

if [ -n "$RAILWAY_URL" ]; then
    echo "🌐 Your app is live at: https://$RAILWAY_URL"
    echo ""
    echo "📝 Update ALLOWED_HOSTS:"
    railway variables set ALLOWED_HOSTS="$RAILWAY_URL,*.up.railway.app"
else
    echo "⚠️  To get a domain, run: railway domain"
fi

echo ""
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "  1. Check deployment: railway status"
echo "  2. View logs: railway logs"
echo "  3. Open app: railway open"
echo "  4. Test API: curl https://your-domain/api/"
echo ""
echo "To redeploy after changes:"
echo "  git push && railway up"
echo ""
