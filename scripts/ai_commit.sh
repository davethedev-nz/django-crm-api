#!/bin/bash
# AI-Powered Auto-Commit Script (Develop Branch)
# Usage: ./scripts/ai_commit.sh "Your prompt describing changes"

set -e

PROMPT="$1"

if [ -z "$PROMPT" ]; then
    echo "Usage: ./scripts/ai_commit.sh 'Description of changes'"
    exit 1
fi

echo "🤖 AI Auto-Commit Pipeline (Develop Branch)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Ensure we're on develop branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "develop" ]; then
    echo "⚠️  Switching to develop branch..."
    git checkout develop
    git pull origin develop
fi

# Check for changes
if [ -z "$(git status --porcelain)" ]; then
    echo "❌ No changes to commit"
    exit 0
fi

echo "📝 Changes detected:"
git status --short

# Stage all changes
echo ""
echo "📦 Staging changes..."
git add .

# Generate AI commit message using GitHub CLI
echo ""
echo "🧠 Generating AI commit message..."

# Use GitHub CLI to generate commit message based on diff
COMMIT_MSG=$(git diff --cached | gh copilot suggest -t shell "Generate a concise git commit message for these changes: $PROMPT" || echo "$PROMPT")

if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="$PROMPT"
fi

echo "💬 Commit message: $COMMIT_MSG"

# Commit changes
echo ""
echo "✅ Committing changes..."
git commit -m "$COMMIT_MSG"

# Push to develop branch
echo ""
echo "🚀 Pushing to develop branch..."
git push origin develop

echo ""
echo "✨ Changes committed to develop (no deployment triggered)"
echo "💡 To deploy to production: ./scripts/deploy_to_production.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Auto-commit complete!"
echo ""
echo "Next steps:"
echo "  1. GitHub Actions will run tests"
echo "  2. Check status: gh run watch"
echo "  3. View logs: gh run view"
