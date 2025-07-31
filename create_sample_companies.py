#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job, Company
from accounts.models import UserProfile

def create_sample_companies():
    print("Creating sample companies...")
    
    # Create sample companies
    companies_data = [
        {
            'name': 'TechCorp Solutions',
            'slug': 'techcorp-solutions',
            'description': 'Leading technology solutions provider specializing in software development, cloud computing, and digital transformation. We help businesses innovate and grow through cutting-edge technology.',
            'industry': 'technology',
            'website': 'https://techcorp-solutions.com',
            'founded_year': 2018,
            'employee_count': '50-100 employees',
            'headquarters': 'San Francisco, CA',
            'contact_email': 'careers@techcorp-solutions.com',
            'contact_phone': '+1-555-123-4567',
            'social_media': {
                'linkedin': 'https://linkedin.com/company/techcorp-solutions',
                'twitter': 'https://twitter.com/techcorp',
                'facebook': 'https://facebook.com/techcorp',
            },
            'is_verified': True,
        },
        {
            'name': 'HealthFirst Medical',
            'slug': 'healthfirst-medical',
            'description': 'Innovative healthcare company focused on improving patient outcomes through advanced medical technology and compassionate care.',
            'industry': 'healthcare',
            'website': 'https://healthfirst-medical.com',
            'founded_year': 2015,
            'employee_count': '100-500 employees',
            'headquarters': 'Boston, MA',
            'contact_email': 'hr@healthfirst-medical.com',
            'contact_phone': '+1-555-234-5678',
            'social_media': {
                'linkedin': 'https://linkedin.com/company/healthfirst-medical',
                'twitter': 'https://twitter.com/healthfirst',
            },
            'is_verified': True,
        },
        {
            'name': 'GreenEnergy Innovations',
            'slug': 'greenenergy-innovations',
            'description': 'Pioneering renewable energy solutions to create a sustainable future. We develop solar, wind, and energy storage technologies.',
            'industry': 'manufacturing',
            'website': 'https://greenenergy-innovations.com',
            'founded_year': 2020,
            'employee_count': '25-50 employees',
            'headquarters': 'Denver, CO',
            'contact_email': 'jobs@greenenergy-innovations.com',
            'contact_phone': '+1-555-345-6789',
            'social_media': {
                'linkedin': 'https://linkedin.com/company/greenenergy-innovations',
                'instagram': 'https://instagram.com/greenenergy',
            },
            'is_verified': False,
        },
        {
            'name': 'EduTech Learning',
            'slug': 'edutech-learning',
            'description': 'Revolutionizing education through technology. We create interactive learning platforms and digital educational content.',
            'industry': 'education',
            'website': 'https://edutech-learning.com',
            'founded_year': 2019,
            'employee_count': '20-50 employees',
            'headquarters': 'Austin, TX',
            'contact_email': 'careers@edutech-learning.com',
            'contact_phone': '+1-555-456-7890',
            'social_media': {
                'linkedin': 'https://linkedin.com/company/edutech-learning',
                'twitter': 'https://twitter.com/edutech',
                'facebook': 'https://facebook.com/edutech',
            },
            'is_verified': True,
        },
        {
            'name': 'FinanceFlow Capital',
            'slug': 'financeflow-capital',
            'description': 'Modern financial services company providing innovative banking, investment, and fintech solutions for the digital age.',
            'industry': 'finance',
            'website': 'https://financeflow-capital.com',
            'founded_year': 2017,
            'employee_count': '100-500 employees',
            'headquarters': 'New York, NY',
            'contact_email': 'recruitment@financeflow-capital.com',
            'contact_phone': '+1-555-567-8901',
            'social_media': {
                'linkedin': 'https://linkedin.com/company/financeflow-capital',
                'twitter': 'https://twitter.com/financeflow',
            },
            'is_verified': True,
        },
    ]
    
    companies = []
    for data in companies_data:
        company, created = Company.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"✅ Created company: {company.name}")
        else:
            print(f"ℹ️  Company already exists: {company.name}")
        companies.append(company)
    
    # Update existing jobs with company relationships
    print("\nUpdating existing jobs with company relationships...")
    
    # Get all existing jobs
    existing_jobs = Job.objects.all()
    
    # Assign companies to jobs based on job titles/descriptions
    for job in existing_jobs:
        if not job.company:  # Only update jobs without a company
            # Simple logic to assign companies based on job content
            job_title_lower = job.title.lower()
            job_desc_lower = job.description.lower()
            
            if any(word in job_title_lower or word in job_desc_lower for word in ['software', 'developer', 'programming', 'tech']):
                job.company = companies[0]  # TechCorp Solutions
            elif any(word in job_title_lower or word in job_desc_lower for word in ['health', 'medical', 'nurse', 'doctor']):
                job.company = companies[1]  # HealthFirst Medical
            elif any(word in job_title_lower or word in job_desc_lower for word in ['energy', 'solar', 'renewable', 'green']):
                job.company = companies[2]  # GreenEnergy Innovations
            elif any(word in job_title_lower or word in job_desc_lower for word in ['education', 'teaching', 'learning', 'student']):
                job.company = companies[3]  # EduTech Learning
            elif any(word in job_title_lower or word in job_desc_lower for word in ['finance', 'banking', 'investment', 'accounting']):
                job.company = companies[4]  # FinanceFlow Capital
            else:
                # Default to TechCorp for remaining jobs
                job.company = companies[0]
            
            job.save()
            print(f"✅ Updated job '{job.title}' with company: {job.company.name}")
    
    print(f"\n🎉 Successfully created {len(companies)} companies and updated {existing_jobs.count()} jobs!")
    print("\n📋 Company Information:")
    for company in companies:
        print(f"  • {company.name} ({company.get_industry_display()}) - {company.get_jobs_count()} jobs")
    
    print("\n🚀 You can now:")
    print("  • Visit /companies/ to see all companies")
    print("  • Visit /companies/[slug]/ to see individual company pages")
    print("  • Add gallery images to companies")
    print("  • Test the dark/light theme toggle")

if __name__ == '__main__':
    create_sample_companies() 