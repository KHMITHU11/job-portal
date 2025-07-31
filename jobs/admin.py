from django.contrib import admin
from .models import Job, Application, Company, CompanyGallery


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'experience_level', 'posted_by', 'created_at', 'is_active')
    list_filter = ('job_type', 'experience_level', 'is_active', 'created_at', 'company')
    search_fields = ('title', 'company__name', 'location', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company', 'location', 'description', 'requirements')
        }),
        ('Job Details', {
            'fields': ('job_type', 'experience_level', 'salary_min', 'salary_max')
        }),
        ('Status', {
            'fields': ('is_active', 'posted_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job__company')
    search_fields = ('applicant__username', 'applicant__email', 'job__title', 'job__company__name')
    readonly_fields = ('applied_at',)
    date_hierarchy = 'applied_at'
    
    fieldsets = (
        ('Application Details', {
            'fields': ('job', 'applicant', 'resume', 'cover_letter')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('applied_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'headquarters', 'employee_count', 'is_verified', 'created_at')
    list_filter = ('industry', 'is_verified', 'created_at')
    search_fields = ('name', 'description', 'headquarters')
    list_editable = ('is_verified',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Company Information', {
            'fields': ('name', 'slug', 'description', 'industry')
        }),
        ('Company Details', {
            'fields': ('website', 'logo', 'founded_year', 'employee_count', 'headquarters')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'social_media')
        }),
        ('Status', {
            'fields': ('is_verified',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(CompanyGallery)
class CompanyGalleryAdmin(admin.ModelAdmin):
    list_display = ('company', 'caption', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at', 'company')
    search_fields = ('company__name', 'caption')
    list_editable = ('is_featured',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Gallery Item', {
            'fields': ('company', 'image', 'caption', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    ) 