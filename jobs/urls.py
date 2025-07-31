from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Jobs
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('jobs/new/', views.JobCreateView.as_view(), name='job_create'),
    path('jobs/<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('jobs/<int:pk>/apply/', views.apply_to_job, name='apply_to_job'),
    
    # Applications
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/status/', views.update_application_status, name='update_application_status'),
    path('jobs/<int:pk>/applications/', views.job_applications, name='job_applications'),
    
    # Companies
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<slug:slug>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/new/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companies/<slug:slug>/edit/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<slug:slug>/gallery/upload/', views.company_gallery_upload, name='company_gallery_upload'),
    path('gallery/<int:pk>/delete/', views.company_gallery_delete, name='company_gallery_delete'),
    
    # Dashboards
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('applicant/dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
    
    # Search
    path('search/', views.search_jobs, name='search_jobs'),
    
    # Contact
    path('contact/', views.contact_view, name='contact'),
] 