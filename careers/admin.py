from django.contrib import admin
from django.utils.html import format_html
from .models import JobOpening, JobApplication


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'department',
        'location',
        'employment_type',
        'vacancies_badge',
        'is_urgent',
        'active',
        'display_order',
    )
    list_display_links = ('title',)
    list_editable = ('is_urgent', 'active', 'display_order')
    list_filter = ('department', 'location', 'employment_type', 'is_urgent', 'active')
    search_fields = ('title', 'description', 'responsibilities', 'requirements')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

    fieldsets = (
        ("Role Information", {
            "fields": ("title", "slug", "department", "location", "employment_type", "number_of_vacancies")
        }),
        ("Experience & Academic Profile", {
            "fields": ("experience_required", "education")
        }),
        ("Job Description & Scope", {
            "fields": ("description", "responsibilities", "requirements", "benefits")
        }),
        ("Hiring Status & Visibility", {
            "fields": ("is_urgent", "active", "display_order")
        }),
    )

    def vacancies_badge(self, obj):
        return format_html('<span class="badge bg-secondary">{} Open</span>', obj.number_of_vacancies)
    vacancies_badge.short_description = "Vacancies"


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'applicant_name',
        'job',
        'phone',
        'email',
        'current_city',
        'years_of_experience',
        'resume_link',
        'status',
        'status_badge',
        'created_at',
    )
    list_display_links = ('applicant_name',)
    list_editable = ['status']
    list_filter = ('status', 'job', 'current_city', ('created_at', admin.DateFieldListFilter))
    search_fields = ('applicant_name', 'email', 'phone', 'current_city', 'current_company', 'cover_note')
    date_hierarchy = 'created_at'
    readonly_fields = ('resume_link', 'created_at')

    fieldsets = (
        ("Candidate Credentials", {
            "fields": ("applicant_name", "email", "phone", "current_city", "years_of_experience", "current_company")
        }),
        ("Applied Position & Cover Letter", {
            "fields": ("job", "resume", "resume_link", "cover_note")
        }),
        ("Recruitment Workflow & Notes", {
            "fields": ("status", "admin_notes", "created_at")
        }),
    )

    def resume_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener" class="btn btn-sm btn-primary" style="padding: 2px 8px; font-size: 12px;">'
                '<i class="bi bi-file-earmark-arrow-down"></i> View Resume</a>',
                obj.resume.url
            )
        return "No resume file"
    resume_link.short_description = "Resume CV"

    def status_badge(self, obj):
        colors = {
            'New': '#3b82f6',               # blue
            'Under Review': '#06b6d4',      # cyan
            'Shortlisted': '#8b5cf6',       # purple
            'Interview Scheduled': '#f59e0b',# amber
            'Offered': '#10b981',           # emerald green
            'Rejected': '#ef4444',          # red
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px;">{}</span>',
            color,
            obj.status
        )
    status_badge.short_description = "Pipeline Stage"
