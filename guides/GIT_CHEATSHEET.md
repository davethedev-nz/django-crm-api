# Git Commands Cheatsheet for This Project

## Daily Workflow

### Check Status
```bash
git status                    # See what's changed
git diff                      # See detailed changes
git log --oneline -10        # View recent commits
```

### Stage and Commit
```bash
# Stage specific files
git add contacts/models.py
git add companies/views.py

# Stage all changes
git add .

# Stage only modified files (not new files)
git add -u

# Commit with message
git commit -m "Add contact validation"

# Amend last commit (before pushing)
git commit --amend -m "Updated message"
```

### Push and Pull
```bash
git pull                     # Get latest changes
git push                     # Push commits to GitHub
git push -u origin main     # First time push (sets upstream)
```

## Branch Management

```bash
# List branches
git branch                   # Local branches
git branch -a               # All branches (local + remote)

# Create and switch to branch
git checkout -b feature/add-tasks
git checkout -b fix/contact-bug

# Switch branches
git checkout main
git checkout feature/add-tasks

# Delete branch
git branch -d feature/add-tasks       # Safe delete (merged only)
git branch -D feature/add-tasks       # Force delete
```

## Undoing Changes

```bash
# Discard changes in working directory
git checkout -- filename.py
git restore filename.py

# Unstage file (keep changes)
git reset HEAD filename.py
git restore --staged filename.py

# Discard all local changes
git reset --hard HEAD

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

## View History

```bash
# View commit history
git log
git log --oneline
git log --graph --oneline --all

# View changes in a commit
git show COMMIT_HASH

# View file history
git log -p filename.py

# Search commits
git log --grep="search term"
git log --author="Dave"
```

## Stashing (Temporary Save)

```bash
# Save current work temporarily
git stash
git stash save "WIP: working on contacts"

# List stashes
git stash list

# Apply most recent stash
git stash apply
git stash pop              # Apply and remove

# Apply specific stash
git stash apply stash@{1}

# Delete stash
git stash drop stash@{1}
git stash clear            # Delete all stashes
```

## Remote Management

```bash
# View remotes
git remote -v

# Add remote
git remote add origin https://github.com/username/repo.git

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git

# Remove remote
git remote remove origin

# Fetch without merging
git fetch origin

# View remote branches
git branch -r
```

## Merging and Rebasing

```bash
# Merge branch into current branch
git merge feature/add-tasks

# Rebase current branch onto main
git rebase main

# Continue rebase after resolving conflicts
git add .
git rebase --continue

# Abort rebase
git rebase --abort

# Interactive rebase (clean up commits)
git rebase -i HEAD~3
```

## Tags

```bash
# Create tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0 release"

# List tags
git tag

# Push tags
git push origin v1.0.0
git push origin --tags

# Delete tag
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

## Useful Aliases

Add these to your Git config for shortcuts:

```bash
# Set up aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'

# Usage
git st                      # Instead of git status
git co main                # Instead of git checkout main
git visual                 # Pretty log view
```

## Common Scenarios

### Forgot to Create Branch Before Changes
```bash
git stash
git checkout -b new-feature
git stash pop
```

### Merge Conflict Resolution
```bash
git pull origin main
# Fix conflicts in files
git add .
git commit -m "Resolve merge conflicts"
git push
```

### Sync Fork with Upstream
```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Delete Remote Branch
```bash
git push origin --delete feature/old-feature
```

### View What Changed in Last Commit
```bash
git show HEAD
git diff HEAD~1
```

### Cherry-pick a Commit
```bash
git cherry-pick COMMIT_HASH
```

## VS Code Git Integration

### Source Control Panel (Ctrl+Shift+G)
- View changes
- Stage/unstage files
- Commit with AI-generated messages (✨ sparkle icon)
- Push/pull
- Manage branches

### GitLens Extension
Highly recommended for enhanced Git capabilities:
- Line blame annotations
- File history
- Compare commits
- Search commits
- And much more!

## GitHub-Specific

### Create Pull Request
```bash
# Push feature branch
git push origin feature/new-feature

# Then create PR on GitHub web interface
# Or use GitHub CLI:
gh pr create --title "Add new feature" --body "Description"
```

### Clone Repository
```bash
git clone https://github.com/username/django-crm-api.git
cd django-crm-api
```

### Sync Local with Remote
```bash
# If remote has new commits
git fetch origin
git merge origin/main

# Or in one command
git pull origin main
```

## Tips

1. **Commit early, commit often** - Small commits are easier to manage
2. **Write descriptive commit messages** - Use AI assistance but review
3. **Pull before push** - Avoid conflicts
4. **Use branches** - Keep main stable
5. **Review before commit** - Always check `git diff`
6. **Don't commit sensitive data** - Check .gitignore
7. **Use .gitignore** - Keep repo clean

## Emergency Commands

### Completely Reset to Remote
```bash
git fetch origin
git reset --hard origin/main
git clean -fd
```

### Recover Deleted Commit
```bash
git reflog
git checkout COMMIT_HASH
```

### Remove File from Git History
```bash
git filter-branch --tree-filter 'rm -f sensitive-file.txt' HEAD
```

---

Keep this cheatsheet handy for quick reference! 📚
