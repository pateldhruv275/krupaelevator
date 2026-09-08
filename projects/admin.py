from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'image_preview', 'caption', 'display_order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; width: 65px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Preview"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'city', 'project_type', 'elevator_type', 'number_of_elevators', 'completion_date', 'featured', 'active', 'display_order')
    list_display_links = ('title',)
    list_editable = ('featured', 'active', 'display_order')
    list_filter = ('city', 'project_type', 'elevator_type', 'featured', 'active')
    search_fields = ('title', 'client_name', 'location', 'city', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('featured_image_preview',)
    inlines = [ProjectImageInline]

    fieldsets = (
        ("Project Identification", {
            "fields": ("title", "slug", "client_name", ("location", "city"), ("project_type", "elevator_type"), "number_of_elevators")
        }),
        ("Visuals & Schedule", {
            "fields": (
                ("featured_image", "featured_image_preview"),
                "completion_date"
            )
        }),
        ("Narrative & Case Study", {
            "fields": ("description",)
        }),
        ("Visibility & Ordering", {
            "fields": ("featured", "active", "display_order")
        }),
        ("SEO Meta Tags", {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse",)
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="height: 35px; width: 50px; object-fit: cover; border-radius: 4px;" />', obj.featured_image.url)
        return "—"
    image_preview.short_description = "Photo"

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 180px; border-radius: 6px;" />', obj.featured_image.url)
        return "No image uploaded"
    featured_image_preview.short_description = "Image Preview"
