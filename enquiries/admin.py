from django.contrib import admin
from django.utils.html import format_html
from .models import ContactEnquiry, QuoteRequest


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone',
        'city',
        'company',
        'subject',
        'status',
        'status_badge',
        'created_at',
    )
    list_editable = ['status']
    list_filter = (
        'status',
        'city',
        ('created_at', admin.DateFieldListFilter),
    )
    search_fields = (
        'name',
        'phone',
        'email',
        'company',
        'city',
        'subject',
        'message',
    )
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Inquirer Information', {
            'fields': ('name', 'phone', 'email', 'company', 'city')
        }),
        ('Enquiry Message', {
            'fields': ('subject', 'message')
        }),
        ('Lead Status & Internal Workflow', {
            'fields': ('status', 'admin_notes')
        }),
        ('Audit Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        colors = {
            'New': '#3b82f6',         # blue
            'Contacted': '#06b6d4',   # cyan
            'Follow Up': '#f59e0b',   # amber
            'Converted': '#10b981',   # green
            'Closed': '#6b7280',      # gray
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px;">{}</span>',
            color,
            obj.status
        )
    status_badge.short_description = "Status Badge"


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone',
        'city',
        'building_type',
        'elevator_type',
        'number_of_elevators',
        'status',
        'status_badge',
        'created_at',
    )
    list_editable = ['status']
    list_filter = (
        'status',
        'city',
        'building_type',
        'elevator_type',
        'project_stage',
        ('created_at', admin.DateFieldListFilter),
    )
    search_fields = (
        'customer_name',
        'company_name',
        'phone',
        'email',
        'city',
        'project_location',
        'message',
    )
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Customer & Project Location', {
            'fields': (
                'customer_name',
                'company_name',
                'phone',
                'email',
                'city',
                'project_location'
            )
        }),
        ('Elevator Technical Requirements', {
            'fields': (
                'building_type',
                'elevator_type',
                'number_of_floors',
                'capacity_required',
                'number_of_elevators',
                'project_stage',
                'message'
            )
        }),
        ('Pipeline Stage & Estimation Notes', {
            'fields': ('status', 'admin_notes')
        }),
        ('Audit Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        colors = {
            'New': '#3b82f6',              # blue
            'Contacted': '#06b6d4',        # cyan
            'Survey Scheduled': '#8b5cf6', # purple
            'Quotation Sent': '#f59e0b',   # amber
            'Negotiation': '#ec4899',      # pink
            'Won': '#10b981',              # emerald green
            'Lost': '#ef4444',             # red
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px;">{}</span>',
            color,
            obj.status
        )
    status_badge.short_description = "Pipeline Badge"
