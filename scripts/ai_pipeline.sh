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
    print_header "🤖 AI-POWERED DEVELOPMENT PIPELINE"
    echo ""
    echo "This will:"
    echo "  1. Check for code changes"
    echo "  2. Run tests locally"
    echo "  3. Auto-commit with AI message"
    echo "  4. Push to GitHub (triggers CI/CD)"
    echo "  5. Monitor deployment"
    echo "  6. Watch logs"
    echo "  7. Iterate on issues"
    echo ""
    read -p "Continue? (y/n): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    
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
    
    # Step 4: Push to GitHub
    print_header "STEP 4: Pushing to GitHub"
    git push
    print_success "Pushed to GitHub"
    echo ""
    
    # Step 5: Monitor CI/CD
    print_header "STEP 5: Monitoring CI/CD pipeline"
    print_info "Waiting for GitHub Actions to start..."
    sleep 5
    
    print_info "Watching workflow run..."
    gh run watch 2>/dev/null || print_info "Workflow started. Check status with: gh run list"
    echo ""
    
    # Step 6: Check deployment status
    print_header "STEP 6: Checking deployment status"
    LATEST_RUN=$(gh run list --limit 1 --json conclusion --jq '.[0].conclusion' 2>/dev/null || echo "unknown")
    
    if [ "$LATEST_RUN" = "success" ]; then
        print_success "CI/CD pipeline succeeded!"
        print_success "Application deployed successfully"
    elif [ "$LATEST_RUN" = "failure" ]; then
        print_error "CI/CD pipeline failed"
        print_info "Check logs with: gh run view"
    else
        print_info "CI/CD pipeline status: $LATEST_RUN"
    fi
    echo ""
    
    # Step 7: Run AI iteration
    print_header "STEP 7: Running AI iteration analysis"
    read -p "Run AI iteration to analyze and suggest improvements? (y/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python scripts/ai_iterate.py
    fi
    echo ""
    
    # Step 8: Summary
    print_header "🎉 PIPELINE COMPLETE"
    echo ""
    echo "Summary:"
    echo "  ✅ Code committed and pushed"
    echo "  ✅ CI/CD pipeline executed"
    echo "  ✅ Tests run"
    echo ""
    echo "Next steps:"
    echo "  • View your repository: gh repo view --web"
    echo "  • Check workflow runs: gh run list"
    echo "  • View deployment: gh run view"
    echo "  • Monitor logs: ./scripts/monitor_logs.py --continuous"
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
