from django.contrib import admin
from django.utils.html import format_html
from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count_badge', 'display_order', 'active')
    list_editable = ('display_order', 'active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

    def post_count_badge(self, obj):
        return format_html('<span class="badge bg-secondary">{} Posts</span>', obj.post_count)
    post_count_badge.short_description = "Live Articles"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'title', 'category', 'author', 'reading_time_badge', 'views_count', 'published_date', 'featured', 'active')
    list_display_links = ('title',)
    list_editable = ('featured', 'active')
    list_filter = ('category', 'active', 'featured', 'published_date')
    search_fields = ('title', 'summary', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    readonly_fields = ('views_count', 'image_preview', 'created_at', 'updated_at')

    fieldsets = (
        ("Article Core", {
            "fields": ("title", "slug", "category", "author", "published_date")
        }),
        ("Content & Excerpt", {
            "fields": ("summary", "content")
        }),
        ("Media & Metrics", {
            "fields": ("featured_image", "image_preview", "reading_time", "views_count")
        }),
        ("Publication Controls", {
            "fields": ("featured", "active")
        }),
        ("Search Engine Optimization (SEO)", {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse",)
        }),
        ("Audit Logs", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    def image_thumb(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="width: 50px; height: 35px; object-fit: cover; border-radius: 4px;" />', obj.featured_image.url)
        return "—"
    image_thumb.short_description = "Thumbnail"

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 150px; border-radius: 8px;" />', obj.featured_image.url)
        return "No image uploaded"
    image_preview.short_description = "Image Preview"

    def reading_time_badge(self, obj):
        return f"{obj.reading_time} min"
    reading_time_badge.short_description = "Read Time"
