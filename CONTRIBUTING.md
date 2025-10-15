# Contributing to Django CRM API

Thank you for your interest in contributing to this project! This guide will help you get started.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-crm-api.git
   cd django-crm-api
   ```
3. **Set up the development environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

## Development Workflow

### 1. Create a Branch

Always create a new branch for your work:

```bash
# Feature branch
git checkout -b feature/add-activity-tracking

# Bug fix branch
git checkout -b fix/contact-email-validation

# Documentation branch
git checkout -b docs/update-readme
```

### 2. Make Your Changes

- Follow the coding guidelines below
- Write clear, concise code
- Add docstrings to functions and classes
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run tests
python manage.py test

# Check for issues
python manage.py check

# Run a specific test
python manage.py test contacts.tests.TestContactModel
```

### 4. Commit Your Changes

Use clear, descriptive commit messages. If you have GitHub Copilot, use the AI commit message feature:

```bash
# Stage changes
git add .

# Commit (use AI suggestion in VS Code or write manually)
git commit -m "Add email validation to Contact model"
```

**Commit Message Guidelines:**
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issues when applicable: "Fix #123: Resolve contact duplication"

### 5. Push and Create Pull Request

```bash
# Push your branch
git push origin feature/add-activity-tracking
```

Then create a Pull Request on GitHub:
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the PR template
4. Submit for review

## Coding Guidelines

### Django Best Practices

- Follow [Django coding style](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/)
- Follow [PEP 8](https://pep8.org/) for Python code
- Use meaningful variable and function names
- Keep functions small and focused
- Avoid code duplication (DRY principle)

### Models

```python
class Contact(models.Model):
    """Model representing a contact in the CRM system."""
    
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        """Return the contact's full name."""
        return f"{self.first_name} {self.last_name}"
```

### Views and ViewSets

```python
class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing contacts.
    
    Provides CRUD operations for contacts with search and filtering.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
```

### Serializers

```python
class ContactSerializer(serializers.ModelSerializer):
    """Serializer for Contact model."""
    
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email']
```

### API Endpoints

- Use RESTful conventions
- Prefix all API endpoints with `/api/`
- Use plural nouns: `/api/contacts/` not `/api/contact/`
- Return appropriate HTTP status codes
- Include pagination for list endpoints

## Testing Guidelines

Write tests for new features and bug fixes:

```python
from django.test import TestCase
from .models import Contact

class ContactModelTest(TestCase):
    """Test cases for Contact model."""
    
    def setUp(self):
        """Set up test data."""
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com'
        )
    
    def test_full_name_property(self):
        """Test that full_name returns correct value."""
        self.assertEqual(self.contact.full_name, 'John Doe')
    
    def test_email_uniqueness(self):
        """Test that email must be unique."""
        with self.assertRaises(Exception):
            Contact.objects.create(
                first_name='Jane',
                last_name='Doe',
                email='john.doe@example.com'  # Duplicate
            )
```

## Pull Request Process

1. **Update documentation** if you're adding/changing features
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** with your changes
5. **Fill out the PR template** completely
6. **Request review** from maintainers

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] CHANGELOG.md updated

## Code Review

All submissions require review before merging:

- Be patient and respectful
- Address feedback constructively
- Make requested changes promptly
- Ask questions if something is unclear

## What to Contribute

### Good First Issues

Look for issues labeled `good first issue` or `help wanted`:

- Documentation improvements
- Bug fixes
- Test coverage improvements
- Code refactoring

### Feature Ideas

- Activity tracking
- Email notifications
- Advanced search and filtering
- Custom fields
- Reporting and analytics
- API authentication improvements
- Export/import functionality

### Bug Reports

When reporting bugs, include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: How to replicate the bug
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Python version, Django version, OS
6. **Screenshots**: If applicable

### Feature Requests

When requesting features, include:

1. **Use Case**: Why is this feature needed?
2. **Description**: What should the feature do?
3. **Alternatives**: Any alternative solutions considered?
4. **Additional Context**: Any other relevant information

## Development Setup Tips

### Pre-commit Hooks (Optional)

Install pre-commit hooks for automatic checks:

```bash
pip install pre-commit
pre-commit install
```

### IDE Configuration

**VS Code Recommended Extensions:**
- Python
- Pylance
- Django
- GitHub Copilot
- GitLens

**VS Code Settings:**
```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "[python]": {
    "editor.formatOnSave": true
  }
}
```

## Questions?

- Open an issue for questions about the project
- Check existing issues and PRs first
- Be respectful and constructive

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing! 🎉
