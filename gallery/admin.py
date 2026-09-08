from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryCategory, GalleryImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_count_badge', 'display_order')
    list_editable = ('display_order',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def image_count_badge(self, obj):
        return format_html('<span class="badge" style="background:#222; color:#fff; padding:4px 8px; border-radius:10px;">{} Photos</span>', obj.image_count)
    image_count_badge.short_description = "Images"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'category', 'display_order', 'active', 'created_at')
    list_display_links = ('title',)
    list_editable = ('display_order', 'active')
    list_filter = ('category', 'active')
    search_fields = ('title', 'description')
    readonly_fields = ('image_preview_large',)

    fieldsets = (
        ("Image Details", {
            "fields": ("category", "title", "description")
        }),
        ("Photograph", {
            "fields": ("image", "image_preview_large")
        }),
        ("Display Settings", {
            "fields": ("display_order", "active")
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 35px; width: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Preview"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; border-radius: 6px;" />', obj.image.url)
        return "No image uploaded"
    image_preview_large.short_description = "Image Preview"
