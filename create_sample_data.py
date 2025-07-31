#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job
from accounts.models import UserProfile

def create_sample_data():
    print("Creating sample data...")
    
    # Create sample employer
    employer, created = User.objects.get_or_create(
        username='employer',
        defaults={
            'email': 'employer@example.com',
            'first_name': 'John',
            'last_name': 'Employer',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        employer.set_password('employer123')
        employer.save()
        print(f"Created employer user: {employer.username}")
    
    # Create employer profile
    employer_profile, created = UserProfile.objects.get_or_create(
        user=employer,
        defaults={
            'user_type': 'employer',
            'phone': '+1-555-0101',
            'address': '123 Business St, Tech City, TC 12345',
            'bio': 'Experienced tech company looking for talented developers.'
        }
    )
    if created:
        print(f"Created employer profile for {employer.username}")
    
    # Create sample applicant
    applicant, created = User.objects.get_or_create(
        username='applicant',
        defaults={
            'email': 'applicant@example.com',
            'first_name': 'Jane',
            'last_name': 'Applicant',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        applicant.set_password('applicant123')
        applicant.save()
        print(f"Created applicant user: {applicant.username}")
    
    # Create applicant profile
    applicant_profile, created = UserProfile.objects.get_or_create(
        user=applicant,
        defaults={
            'user_type': 'applicant',
            'phone': '+1-555-0102',
            'address': '456 Developer Ave, Code City, CC 67890',
            'bio': 'Passionate software developer with 3 years of experience in Python and Django.'
        }
    )
    if created:
        print(f"Created applicant profile for {applicant.username}")
    
    # Create sample jobs
    sample_jobs = [
        {
            'title': 'Senior Python Developer',
            'company_name': 'TechCorp Solutions',
            'location': 'San Francisco, CA',
            'description': 'We are looking for an experienced Python developer to join our team. You will be working on cutting-edge web applications using Django and modern frontend technologies.',
            'requirements': '• 5+ years of Python experience\n• Strong knowledge of Django\n• Experience with PostgreSQL\n• Familiarity with AWS\n• Excellent problem-solving skills',
            'salary_min': 120000,
            'salary_max': 150000,
            'job_type': 'full-time',
            'experience_level': 'senior',
            'posted_by': employer
        },
        {
            'title': 'Frontend Developer',
            'company_name': 'WebFlow Inc',
            'location': 'New York, NY',
            'description': 'Join our frontend team to build beautiful and responsive user interfaces. We use modern JavaScript frameworks and focus on user experience.',
            'requirements': '• 3+ years of JavaScript experience\n• Proficiency in React or Vue.js\n• Experience with CSS preprocessors\n• Understanding of responsive design\n• Git workflow experience',
            'salary_min': 80000,
            'salary_max': 110000,
            'job_type': 'full-time',
            'experience_level': 'mid-level',
            'posted_by': employer
        },
        {
            'title': 'DevOps Engineer',
            'company_name': 'CloudTech Systems',
            'location': 'Remote',
            'description': 'We need a DevOps engineer to help us scale our infrastructure and improve our deployment processes. Experience with Docker and Kubernetes is essential.',
            'requirements': '• 4+ years of DevOps experience\n• Strong knowledge of Docker and Kubernetes\n• Experience with AWS or GCP\n• CI/CD pipeline experience\n• Linux system administration',
            'salary_min': 100000,
            'salary_max': 130000,
            'job_type': 'full-time',
            'experience_level': 'senior',
            'posted_by': employer
        },
        {
            'title': 'Junior Developer Intern',
            'company_name': 'StartupXYZ',
            'location': 'Austin, TX',
            'description': 'Great opportunity for recent graduates to learn and grow in a fast-paced startup environment. We provide mentorship and hands-on experience.',
            'requirements': '• Computer Science degree or equivalent\n• Basic knowledge of Python/JavaScript\n• Eager to learn and grow\n• Good communication skills\n• Team player attitude',
            'salary_min': 40000,
            'salary_max': 50000,
            'job_type': 'internship',
            'experience_level': 'entry-level',
            'posted_by': employer
        },
        {
            'title': 'Data Scientist',
            'company_name': 'DataInsights Co',
            'location': 'Seattle, WA',
            'description': 'Join our data science team to work on machine learning projects and data analysis. You will help us extract insights from large datasets.',
            'requirements': '• MS/PhD in Statistics, Computer Science, or related field\n• Experience with Python data science stack\n• Knowledge of machine learning algorithms\n• Experience with SQL and big data tools\n• Strong analytical skills',
            'salary_min': 110000,
            'salary_max': 140000,
            'job_type': 'full-time',
            'experience_level': 'senior',
            'posted_by': employer
        }
    ]
    
    for job_data in sample_jobs:
        job, created = Job.objects.get_or_create(
            title=job_data['title'],
            company_name=job_data['company_name'],
            defaults=job_data
        )
        if created:
            print(f"Created job: {job.title}")
    
    print("\n✅ Sample data created successfully!")
    print("\n📋 Login Credentials:")
    print("Admin: admin / (no password set)")
    print("Employer: employer / employer123")
    print("Applicant: applicant / applicant123")
    print("\n🚀 You can now run: python manage.py runserver")

if __name__ == '__main__':
    create_sample_data() 