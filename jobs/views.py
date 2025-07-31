from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Job, Application, Company, CompanyGallery
from .forms import JobForm, ApplicationForm, JobSearchForm, CompanyForm, CompanyGalleryForm


def home(request):
    """Home page view"""
    featured_jobs = Job.objects.filter(is_active=True).order_by('-created_at')[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    total_applications = Application.objects.count()
    total_companies = Company.objects.count()
    
    context = {
        'featured_jobs': featured_jobs,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'total_companies': total_companies,
    }
    return render(request, 'jobs/home.html', context)


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)
        form = JobSearchForm(self.request.GET)
        
        if form.is_valid():
            query = form.cleaned_data.get('query')
            job_type = form.cleaned_data.get('job_type')
            experience_level = form.cleaned_data.get('experience_level')
            location = form.cleaned_data.get('location')
            company = form.cleaned_data.get('company')
            
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query) |
                    Q(company__name__icontains=query) |
                    Q(location__icontains=query)
                )
            
            if job_type:
                queryset = queryset.filter(job_type=job_type)
            
            if experience_level:
                queryset = queryset.filter(experience_level=experience_level)
            
            if location:
                queryset = queryset.filter(location__icontains=location)
            
            if company:
                queryset = queryset.filter(company=company)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = JobSearchForm(self.request.GET)
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        
        # Check if user has applied
        has_applied = False
        if self.request.user.is_authenticated:
            has_applied = Application.objects.filter(
                job=job, 
                applicant=self.request.user
            ).exists()
        
        context['has_applied'] = has_applied
        context['applications_count'] = job.get_applications_count()
        return context


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('employer_dashboard')
    
    def test_func(self):
        return hasattr(self.request.user, 'profile') and self.request.user.profile.user_type == 'employer'
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, 'Job posted successfully!')
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('employer_dashboard')
    
    def test_func(self):
        job = self.get_object()
        return (hasattr(self.request.user, 'profile') and 
                self.request.user.profile.user_type == 'employer' and 
                job.posted_by == self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Job updated successfully!')
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('employer_dashboard')
    
    def test_func(self):
        job = self.get_object()
        return (hasattr(self.request.user, 'profile') and 
                self.request.user.profile.user_type == 'employer' and 
                job.posted_by == self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Job deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def apply_to_job(request, pk):
    """Apply to a job"""
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if user has already applied
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied to this job.')
        return redirect('job_detail', pk=pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', pk=pk)
    else:
        form = ApplicationForm()
    
    return render(request, 'jobs/apply_to_job.html', {
        'form': form,
        'job': job
    })


@login_required
def employer_dashboard(request):
    """Employer dashboard"""
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'employer':
        messages.error(request, 'Access denied. Employer account required.')
        return redirect('home')
    
    posted_jobs = Job.objects.filter(posted_by=request.user).order_by('-created_at')
    total_applications = Application.objects.filter(job__posted_by=request.user).count()
    
    context = {
        'posted_jobs': posted_jobs,
        'total_jobs': posted_jobs.count(),
        'total_applications': total_applications,
    }
    return render(request, 'jobs/employer_dashboard.html', context)


@login_required
def applicant_dashboard(request):
    """Applicant dashboard"""
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'applicant':
        messages.error(request, 'Access denied. Applicant account required.')
        return redirect('home')
    
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_at')
    
    context = {
        'applications': applications,
        'total_applications': applications.count(),
    }
    return render(request, 'jobs/applicant_dashboard.html', context)


@login_required
def job_applications(request, pk):
    """View applications for a specific job"""
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    applications = Application.objects.filter(job=job).order_by('-applied_at')
    
    return render(request, 'jobs/job_applications.html', {
        'job': job,
        'applications': applications
    })


@login_required
def application_detail(request, pk):
    """View application details"""
    application = get_object_or_404(Application, pk=pk)
    
    # Check permissions
    if (application.applicant != request.user and 
        application.job.posted_by != request.user):
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    return render(request, 'jobs/application_detail.html', {
        'application': application
    })


@login_required
def update_application_status(request, pk):
    """Update application status (employer only)"""
    application = get_object_or_404(Application, pk=pk)
    
    if application.job.posted_by != request.user:
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
            messages.success(request, 'Application status updated successfully!')
        else:
            messages.error(request, 'Invalid status.')
    
    return redirect('application_detail', pk=pk)


def search_jobs(request):
    """AJAX endpoint for job search"""
    query = request.GET.get('query', '')
    jobs = Job.objects.filter(is_active=True)
    
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company__name__icontains=query) |
            Q(location__icontains=query)
        )
    
    jobs = jobs[:10]  # Limit results
    
    data = []
    for job in jobs:
        data.append({
            'id': job.id,
            'title': job.title,
            'company': job.company.name,
            'location': job.location,
            'url': job.get_absolute_url(),
        })
    
    return JsonResponse({'jobs': data})


def contact_view(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        newsletter = request.POST.get('newsletter')
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        messages.success(request, f'Thank you {name}! Your message has been sent successfully. We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'jobs/contact.html')


# Company Views
class CompanyListView(ListView):
    model = Company
    template_name = 'jobs/company_list.html'
    context_object_name = 'companies'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Company.objects.all()
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(industry__icontains=query)
            )
        
        return queryset


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'jobs/company_detail.html'
    context_object_name = 'company'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.get_object()
        context['jobs'] = company.jobs.filter(is_active=True).order_by('-created_at')
        context['gallery'] = company.gallery.all()
        return context


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'jobs/company_form.html'
    success_url = reverse_lazy('company_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Company created successfully!')
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'jobs/company_form.html'
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        messages.success(self.request, 'Company updated successfully!')
        return super().form_valid(form)


@login_required
def company_gallery_upload(request, slug):
    """Upload images to company gallery"""
    company = get_object_or_404(Company, slug=slug)
    
    if request.method == 'POST':
        form = CompanyGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_item = form.save(commit=False)
            gallery_item.company = company
            gallery_item.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('company_detail', slug=slug)
    else:
        form = CompanyGalleryForm()
    
    return render(request, 'jobs/company_gallery_upload.html', {
        'form': form,
        'company': company
    })


@login_required
def company_gallery_delete(request, pk):
    """Delete gallery image"""
    gallery_item = get_object_or_404(CompanyGallery, pk=pk)
    company_slug = gallery_item.company.slug
    
    gallery_item.delete()
    messages.success(request, 'Image deleted successfully!')
    return redirect('company_detail', slug=company_slug) 