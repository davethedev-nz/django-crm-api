<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Django CRM API Project

This is a Django REST Framework based CRM (Customer Relationship Management) API project.

## Project Structure
- **contacts**: Manages contact information (people)
- **companies**: Manages company/organization information
- **deals**: Manages sales deals and opportunities

## Coding Guidelines
- Follow Django best practices and naming conventions
- Use Django REST Framework for all API endpoints
- Keep models clean and follow DRY principles
- Add proper docstrings to all classes and functions
- Use appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Implement proper validation in serializers
- Follow PEP 8 style guide for Python code

## API Conventions
- All API endpoints are prefixed with `/api/`
- Use plural nouns for resource endpoints (e.g., `/api/contacts/`)
- Follow RESTful API design principles
- Return appropriate HTTP status codes
- Include pagination for list endpoints
