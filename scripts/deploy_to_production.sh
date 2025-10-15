#!/bin/bash

# Deploy script: Merge develop to main and trigger production deployment
# This script merges the develop branch into main and pushes to trigger auto-deploy

set -e

echo "🔄 Deploying develop branch to production..."
echo ""

# Make sure we're on develop and it's up to date
echo "📥 Updating develop branch..."
git checkout develop
git pull origin develop

# Switch to main and update
echo "📥 Updating main branch..."
git checkout main
git pull origin main

# Merge develop into main
echo "🔀 Merging develop into main..."
git merge develop -m "Merge develop into main for production deployment"

# Push to main (triggers auto-deploy to PRODUCTION)
echo "🚀 Pushing to main (this will trigger auto-deploy to Railway PRODUCTION)..."
git push origin main

echo ""
echo "✅ Successfully deployed to production!"
echo ""
echo "🌐 Production Environment:"
echo "   • View logs: railway logs -e production"
echo "   • Open site: railway open -e production"
echo "   • Check status: railway status"
echo ""
echo "🔧 Development Environment (for testing):"
echo "   • View logs: railway logs -e development"
echo "   • Open site: railway open -e development"
echo ""
echo "💡 To continue development, switch back to develop:"
echo "   git checkout develop"
echo ""
