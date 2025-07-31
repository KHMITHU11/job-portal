# Static Files Directory

This directory contains all static files for the JobPortal application.

## Structure

```
static/
├── css/
│   └── custom.css          # Custom CSS styles for the application
├── js/
│   └── custom.js           # Custom JavaScript functionality
├── images/
│   └── logo.svg            # Application logo
└── README.md               # This file
```

## Files Description

### CSS Files
- **custom.css**: Contains additional styling for the job portal including:
  - Enhanced hover effects
  - Animation effects
  - Responsive design improvements
  - Dark mode support
  - Custom component styling

### JavaScript Files
- **custom.js**: Contains interactive functionality including:
  - Form validation enhancement
  - File upload preview
  - Search form enhancement
  - Dashboard statistics animation
  - Mobile menu improvements
  - Back to top button
  - Password strength indicator

### Images
- **logo.svg**: Custom SVG logo for the application

## Usage

These static files are automatically loaded by the base template and provide enhanced functionality and styling for the JobPortal application.

## Development

When making changes to static files:
1. Edit the files in this directory
2. Run `python manage.py collectstatic` to collect static files for production
3. The changes will be reflected in the development server immediately 