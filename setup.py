#!/usr/bin/env python3
"""
Setup script for JobPortal Django application.
This script helps with initial setup and creates sample data.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line
from django.contrib.auth.models import User
from jobs.models import Job
from accounts.models import UserProfile

def setup_django():
    """Setup Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
    django.setup()

def create_sample_data():
    """Create sample users and jobs for testing"""
    print("Creating sample data...")
    
    # Create sample employer
    employer, created = User.objects.get_or_create(
        username='employer',
        defaults={
            'email': 'employer@example.com',
            'first_name': 'John',
            'last_name': 'Employer',
            'is_staff': True
        }
    )
    if created:
        employer.set_password('employer123')
        employer.save()
        print("✓ Created sample employer: employer@example.com / employer123")
    
    # Create sample applicant
    applicant, created = User.objects.get_or_create(
        username='applicant',
        defaults={
            'email': 'applicant@example.com',
            'first_name': 'Jane',
            'last_name': 'Applicant'
        }
    )
    if created:
        applicant.set_password('applicant123')
        applicant.save()
        print("✓ Created sample applicant: applicant@example.com / applicant123")
    
    # Create sample jobs
    sample_jobs = [
        {
            'title': 'Senior Python Developer',
            'company_name': 'TechCorp Inc.',
            'location': 'San Francisco, CA',
            'description': 'We are looking for an experienced Python developer to join our team. You will be responsible for developing and maintaining web applications using Django and Python.',
            'requirements': '• 5+ years of Python experience\n• Strong knowledge of Django\n• Experience with PostgreSQL\n• Git version control\n• Agile development experience',
            'salary_min': 80000,
            'salary_max': 120000,
            'job_type': 'full-time',
            'experience_level': 'senior'
        },
        {
            'title': 'Frontend Developer',
            'company_name': 'WebSolutions Ltd.',
            'location': 'New York, NY',
            'description': 'Join our frontend team to create beautiful and responsive user interfaces. We use modern technologies like React, Vue.js, and Bootstrap.',
            'requirements': '• 3+ years of JavaScript experience\n• Proficiency in React or Vue.js\n• CSS/SCSS expertise\n• Responsive design skills\n• Portfolio of work',
            'salary_min': 60000,
            'salary_max': 90000,
            'job_type': 'full-time',
            'experience_level': 'mid'
        },
        {
            'title': 'Data Scientist Intern',
            'company_name': 'DataTech Analytics',
            'location': 'Remote',
            'description': 'Exciting internship opportunity for data science students. Work on real projects using Python, pandas, and machine learning libraries.',
            'requirements': '• Currently pursuing degree in Computer Science or related field\n• Basic Python knowledge\n• Interest in data science\n• Strong analytical skills',
            'salary_min': 25000,
            'salary_max': 35000,
            'job_type': 'internship',
            'experience_level': 'entry'
        },
        {
            'title': 'DevOps Engineer',
            'company_name': 'CloudFirst Systems',
            'location': 'Austin, TX',
            'description': 'Help us build and maintain our cloud infrastructure. Work with AWS, Docker, Kubernetes, and CI/CD pipelines.',
            'requirements': '• 4+ years of DevOps experience\n• AWS certification preferred\n• Docker and Kubernetes experience\n• Linux administration skills\n• CI/CD pipeline knowledge',
            'salary_min': 90000,
            'salary_max': 130000,
            'job_type': 'full-time',
            'experience_level': 'senior'
        },
        {
            'title': 'UI/UX Designer',
            'company_name': 'Creative Design Studio',
            'location': 'Los Angeles, CA',
            'description': 'Create amazing user experiences and beautiful interfaces. Work with our design team to create products that users love.',
            'requirements': '• 3+ years of UI/UX design experience\n• Proficiency in Figma or Sketch\n• Portfolio showcasing work\n• User research experience\n• Prototyping skills',
            'salary_min': 70000,
            'salary_max': 100000,
            'job_type': 'full-time',
            'experience_level': 'mid'
        }
    ]
    
    for job_data in sample_jobs:
        job, created = Job.objects.get_or_create(
            title=job_data['title'],
            company_name=job_data['company_name'],
            defaults={
                'location': job_data['location'],
                'description': job_data['description'],
                'requirements': job_data['requirements'],
                'salary_min': job_data['salary_min'],
                'salary_max': job_data['salary_max'],
                'job_type': job_data['job_type'],
                'experience_level': job_data['experience_level'],
                'posted_by': employer
            }
        )
        if created:
            print(f"✓ Created sample job: {job.title}")
    
    print("\n🎉 Sample data created successfully!")
    print("\nSample Accounts:")
    print("Employer: employer@example.com / employer123")
    print("Applicant: applicant@example.com / applicant123")

def main():
    """Main setup function"""
    print("🚀 JobPortal Setup Script")
    print("=" * 40)
    
    try:
        setup_django()
        
        # Run migrations
        print("Running migrations...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("✓ Migrations completed")
        
        # Create sample data
        create_sample_data()
        
        print("\n✅ Setup completed successfully!")
        print("\nTo start the development server:")
        print("python manage.py runserver")
        print("\nThen visit: http://127.0.0.1:8000")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 