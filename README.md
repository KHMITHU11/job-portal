# JobPortal - Premium Job Portal Application

A modern, feature-rich job portal built with Django that connects employers with talented job seekers. This application provides a comprehensive platform for job posting, searching, and application management.

## 🌟 Features

### 🔐 Authentication & User Management
- **User Registration**: Sign up as either an Employer or Applicant
- **User Profiles**: Customizable profiles with contact information and bio
- **Role-based Access**: Different dashboards and permissions for each user type
- **Account Type Switching**: Users can change between employer and applicant roles

### 💼 Job Management
- **Job Posting**: Employers can create detailed job postings with comprehensive information
- **Job Categories**: Full-time, Part-time, Contract, Internship, Freelance
- **Experience Levels**: Entry, Mid, Senior, Executive levels
- **Salary Ranges**: Configurable salary ranges with proper validation
- **Job Status**: Active/Inactive job management

### 🔍 Advanced Search & Filtering
- **Multi-field Search**: Search by job title, company name, location, and description
- **Filter Options**: Filter by job type, experience level, and location
- **Real-time Results**: Dynamic search with pagination
- **Responsive Design**: Mobile-friendly search interface

### 📝 Application System
- **Resume Upload**: Support for PDF, DOC, DOCX files (5MB limit)
- **Cover Letters**: Rich text cover letter submission
- **Application Tracking**: Status tracking (Pending, Reviewed, Shortlisted, Rejected, Accepted)
- **Duplicate Prevention**: Users can only apply once per job

### 📊 Dashboard Analytics
- **Employer Dashboard**: Job posting statistics, application counts, and management tools
- **Applicant Dashboard**: Application tracking, status monitoring, and job search
- **Real-time Statistics**: Live counts and metrics

### 🎨 Modern UI/UX
- **Bootstrap 5**: Modern, responsive design
- **Font Awesome Icons**: Professional iconography
- **Gradient Backgrounds**: Attractive visual design
- **Card-based Layout**: Clean, organized information display
- **Interactive Elements**: Hover effects and smooth transitions

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Authentication**: Django Allauth
- **File Upload**: Django FileField with validation
- **Search**: Django ORM with Q objects

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow (for image processing)
- django-crispy-forms
- crispy-bootstrap5
- django-allauth
- python-decouple

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jobportal
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
jobportal/
├── jobportal/          # Main Django project
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── jobs/               # Jobs app
│   ├── models.py       # Job and Application models
│   ├── views.py        # Job-related views
│   ├── forms.py        # Job forms
│   ├── admin.py        # Admin configuration
│   └── urls.py         # Job URLs
├── accounts/           # Accounts app
│   ├── models.py       # UserProfile model
│   ├── views.py        # Authentication views
│   ├── forms.py        # User forms
│   ├── admin.py        # Admin configuration
│   └── urls.py         # Account URLs
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── jobs/           # Job templates
│   └── accounts/       # Account templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Usage Guide

### For Employers

1. **Register as an Employer**
   - Visit the registration page
   - Select "Employer" as account type
   - Complete your profile

2. **Post a Job**
   - Go to your dashboard
   - Click "Post New Job"
   - Fill in job details (title, company, location, description, requirements, salary)
   - Submit the job posting

3. **Manage Applications**
   - View applications for each job
   - Update application status
   - Review resumes and cover letters

### For Applicants

1. **Register as an Applicant**
   - Visit the registration page
   - Select "Applicant" as account type
   - Complete your profile

2. **Search for Jobs**
   - Use the search bar to find jobs
   - Apply filters by job type, experience level, location
   - Browse through job listings

3. **Apply to Jobs**
   - Click "Apply" on desired jobs
   - Upload your resume (PDF, DOC, DOCX)
   - Write a compelling cover letter
   - Submit your application

4. **Track Applications**
   - View your application status in the dashboard
   - Monitor application progress
   - Access application details

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
The default configuration uses SQLite. For production, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
For production, collect static files:

```bash
python manage.py collectstatic
```

## 🎨 Customization

### Styling
- Modify CSS in `templates/base.html`
- Update Bootstrap theme colors
- Customize component styles

### Features
- Add new job categories in `jobs/models.py`
- Extend application status options
- Add email notifications
- Implement job alerts

## 🔒 Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **File Upload Validation**: Secure file upload with type and size validation
- **User Authentication**: Secure login/logout system
- **Permission Checks**: Role-based access control
- **SQL Injection Prevention**: Django ORM protection

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Heroku Deployment
1. Create a `Procfile`:
   ```
   web: gunicorn jobportal.wsgi --log-file -
   ```

2. Add to `requirements.txt`:
   ```
   gunicorn
   whitenoise
   ```

3. Configure environment variables in Heroku dashboard

### Docker Deployment
Create a `Dockerfile`:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons
- All contributors and users of this project

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact: Kamrulhasan9047@gmaol.com
- Phone: 01757704783
- Location: Your Location
- Documentation: [Link to documentation]

---

**JobPortal** - Connecting talented professionals with amazing opportunities! 🚀 #   j o b - p o r t a l 
 
 
