#!/bin/bash
# Master AI Development Pipeline
# This script orchestrates the entire AI-powered development cycle

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC}  $1"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

# Main pipeline
main() {
    clear
    print_header "🤖 AI-POWERED DEVELOPMENT PIPELINE (Develop Branch)"
    echo ""
    echo "This will:"
    echo "  1. Ensure you're on develop branch"
    echo "  2. Check for code changes"
    echo "  3. Run tests locally"
    echo "  4. Auto-commit with AI message"
    echo "  5. Push to develop (NO deployment)"
    echo "  6. Iterate on issues"
    echo ""
    echo "💡 To deploy to production, manually run: ./scripts/deploy_to_production.sh"
    echo ""
    read -p "Continue? (y/n): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    
    # Ensure we're on develop branch
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    if [ "$CURRENT_BRANCH" != "develop" ]; then
        print_info "Switching to develop branch..."
        git checkout develop
        git pull origin develop
        print_success "Now on develop branch"
    else
        print_success "Already on develop branch"
        git pull origin develop
    fi
    echo ""
    
    # Step 1: Check for changes
    print_header "STEP 1: Checking for changes"
    if [ -z "$(git status --porcelain)" ]; then
        print_info "No changes detected. Nothing to do."
        exit 0
    fi
    print_success "Changes detected"
    git status --short
    echo ""
    
    # Step 2: Run tests locally
    print_header "STEP 2: Running tests locally"
    if python manage.py test; then
        print_success "All tests passed locally"
    else
        print_error "Tests failed locally"
        echo ""
        print_info "Do you want to continue anyway? (y/n): "
        read -p "" -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "Fix the tests and try again"
            exit 1
        fi
    fi
    echo ""
    
    # Step 3: AI-powered commit
    print_header "STEP 3: Creating AI-powered commit"
    read -p "📝 Describe your changes: " COMMIT_DESC
    
    git add .
    
    # Generate AI commit message
    print_info "Generating AI commit message..."
    COMMIT_MSG="$COMMIT_DESC"
    
    # Commit
    git commit -m "$COMMIT_MSG"
    print_success "Changes committed: $COMMIT_MSG"
    echo ""
    
    # Step 4: Push to develop branch
    print_header "STEP 4: Pushing to develop branch"
    git push origin develop
    print_success "Pushed to develop branch"
    print_info "✨ Changes are safely committed to develop (no deployment triggered)"
    echo ""
    
    # Step 5: Run AI iteration
    print_header "STEP 5: Running AI iteration analysis"
    read -p "Run AI iteration to analyze and suggest improvements? (y/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python scripts/ai_iterate.py
    fi
    echo ""
    
    # Step 6: Summary
    print_header "🎉 PIPELINE COMPLETE"
    echo ""
    echo "Summary:"
    echo "  ✅ Code committed and pushed to develop"
    echo "  ✅ Tests run locally"
    echo "  ✅ Changes are safe on develop branch"
    echo ""
    echo "Next steps:"
    echo "  • Continue development: Make more changes and run pipeline again"
    echo "  • Deploy to production: ./scripts/deploy_to_production.sh"
    echo "  • View workflow status: ./scripts/workflow_status.sh"
    echo "  • Check repository: gh repo view --web"
    echo ""
    print_info "Remember: develop branch does NOT auto-deploy"
    print_info "When ready, merge to main with: ./scripts/deploy_to_production.sh"
    echo ""
    
    # Optional: Start log monitoring
    read -p "Start continuous log monitoring? (y/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_info "Starting log monitor (Ctrl+C to stop)..."
        python scripts/monitor_logs.py --continuous --interval 30
    fi
}

# Run the pipeline
main "$@"
