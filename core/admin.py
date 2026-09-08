from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, HeroSlider, Statistic, Feature, ProcessStep, Industry, Service, Client, Testimonial


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Corporate Identity", {
            "fields": ("company_name", "tagline", "logo", "favicon", "logo_preview")
        }),
        ("Direct Contact Channels", {
            "fields": ("phone", "alternate_phone", "email", "whatsapp", "emergency_helpline")
        }),
        ("Physical Location & Operations", {
            "fields": ("address", "working_hours", "google_map_embed")
        }),
        ("Social Presence", {
            "fields": ("facebook", "instagram", "linkedin", "youtube", "twitter"),
            "classes": ("collapse",)
        }),
        ("Footer & Summary Content", {
            "fields": ("footer_description",)
        }),
    )
    readonly_fields = ("logo_preview",)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 4px;" />', obj.logo.url)
        return "No logo uploaded"
    logo_preview.short_description = "Logo Preview"

    def has_add_permission(self, request):
        # Prevent creating multiple SiteSettings rows
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Disallow accidental deletion of core site configuration
        return False


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "title", "subtitle", "button_text", "display_order", "active", "created_at")
    list_display_links = ("title",)
    list_editable = ("display_order", "active")
    list_filter = ("active",)
    search_fields = ("title", "subtitle", "description")
    readonly_fields = ("image_preview_large",)
    fieldsets = (
        ("Slide Content", {
            "fields": ("title", "subtitle", "description")
        }),
        ("Visual Banner", {
            "fields": ("image", "image_preview_large")
        }),
        ("Call To Actions", {
            "fields": (("button_text", "button_url"), ("secondary_button_text", "secondary_button_url"))
        }),
        ("Display Settings", {
            "fields": ("display_order", "active")
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 40px; width: 70px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Preview"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; border-radius: 6px;" />', obj.image.url)
        return "No image uploaded"
    image_preview_large.short_description = "Banner Preview"


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("title", "number", "suffix", "icon_badge", "display_order", "active")
    list_editable = ("number", "suffix", "display_order", "active")
    list_filter = ("active",)
    search_fields = ("title",)

    def icon_badge(self, obj):
        return format_html('<span style="font-family: monospace; background: #f0f0f0; padding: 2px 6px; border-radius: 4px;"><i class="bi {}"></i> {}</span>', obj.icon, obj.icon)
    icon_badge.short_description = "Icon Class"


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "badge_text", "icon", "display_order", "active")
    list_editable = ("display_order", "active")
    list_filter = ("active",)
    search_fields = ("title", "description", "badge_text")


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ("step_number", "title", "icon", "display_order", "active")
    list_display_links = ("title",)
    list_editable = ("step_number", "display_order", "active")
    list_filter = ("active",)
    search_fields = ("title", "short_description")


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "name", "icon", "display_order", "active")
    list_editable = ("display_order", "active")
    list_filter = ("active",)
    search_fields = ("name", "description")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 35px; width: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Image"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "title", "icon", "display_order", "active")
    list_display_links = ("title",)
    list_editable = ("display_order", "active")
    list_filter = ("active",)
    search_fields = ("title", "short_description", "description", "features")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("image_preview_large",)

    fieldsets = (
        ("Service Details", {
            "fields": ("title", "slug", "icon", "short_description", "description")
        }),
        ("Visuals", {
            "fields": ("image", "image_preview_large")
        }),
        ("Scope & Deliverables", {
            "fields": ("features",)
        }),
        ("Display & Ordering", {
            "fields": ("display_order", "active")
        }),
        ("SEO Meta Tags", {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse",)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 35px; width: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Thumbnail"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 160px; border-radius: 6px;" />', obj.image.url)
        return "No image uploaded"
    image_preview_large.short_description = "Image Preview"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("logo_preview", "name", "industry", "website_link", "display_order", "active")
    list_display_links = ("name",)
    list_editable = ("display_order", "active")
    list_filter = ("active", "industry")
    search_fields = ("name", "description", "industry")
    readonly_fields = ("logo_preview_large",)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 30px; max-width: 60px; object-fit: contain;" />', obj.logo.url)
        return "—"
    logo_preview.short_description = "Logo"

    def logo_preview_large(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.logo.url)
        return "No logo uploaded"
    logo_preview_large.short_description = "Logo Preview"

    def website_link(self, obj):
        if obj.website:
            return format_html('<a href="{}" target="_blank" rel="noopener">{}</a>', obj.website, obj.website)
        return "—"
    website_link.short_description = "Website"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("photo_thumb", "client_name", "company", "city", "rating_stars", "featured", "display_order", "active")
    list_display_links = ("client_name",)
    list_editable = ("featured", "display_order", "active")
    list_filter = ("active", "featured", "rating", "city")
    search_fields = ("client_name", "company", "city", "quote", "elevator_type_installed")
    readonly_fields = ("photo_preview", "created_at")
    fieldsets = (
        ("Client Details", {
            "fields": ("client_name", "client_title", "company", "city", "photo", "photo_preview")
        }),
        ("Elevator Installation & Rating", {
            "fields": ("elevator_type_installed", "rating", "quote")
        }),
        ("Display Controls", {
            "fields": ("featured", "display_order", "active", "created_at")
        }),
    )

    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 36px; height: 36px; border-radius: 50%; object-fit: cover;" />', obj.photo.url)
        return format_html('<div style="width: 36px; height: 36px; border-radius: 50%; background: #333; color: #d4af37; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">{}</div>', obj.client_name[:1])
    photo_thumb.short_description = "Photo"

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 120px; border-radius: 8px;" />', obj.photo.url)
        return "No photo uploaded"
    photo_preview.short_description = "Photo Preview"

    def rating_stars(self, obj):
        stars = "★" * obj.rating + "☆" * (5 - obj.rating)
        return format_html('<span style="color: #f59e0b; font-size: 14px;">{}</span>', stars)
    rating_stars.short_description = "Rating"

