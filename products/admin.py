from django.contrib import admin
from django.utils.html import format_html
from .models import ProductCategory, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'image_preview', 'caption', 'display_order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; width: 65px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Preview"


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'slug', 'category_icon', 'count_display', 'display_order', 'active', 'updated_at')
    list_display_links = ('name',)
    list_editable = ('display_order', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'short_description', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview_large', 'banner_preview_large')

    fieldsets = (
        ("Category Information", {
            "fields": ("name", "slug", "icon", "short_description", "description")
        }),
        ("Visuals", {
            "fields": (
                ("image", "image_preview_large"),
                ("banner_image", "banner_preview_large"),
            )
        }),
        ("Visibility & Ordering", {
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
            return format_html('<img src="{}" style="max-height: 150px; border-radius: 6px;" />', obj.image.url)
        return "No image uploaded"
    image_preview_large.short_description = "Thumbnail Preview"

    def banner_preview_large(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" style="max-height: 150px; border-radius: 6px;" />', obj.banner_image.url)
        return "No banner uploaded"
    banner_preview_large.short_description = "Banner Preview"

    def category_icon(self, obj):
        return format_html('<i class="bi {}" style="font-size: 1.2rem; color: #d4af37;"></i>', obj.icon)
    category_icon.short_description = "Icon"

    def count_display(self, obj):
        return format_html('<span class="badge" style="background:#222; color:#fff; padding:4px 8px; border-radius:10px;">{} Products</span>', obj.product_count)
    count_display.short_description = "Total Products"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'category', 'capacity', 'speed', 'machine_type', 'featured', 'active', 'display_order')
    list_display_links = ('name',)
    list_editable = ('featured', 'active', 'display_order')
    list_filter = ('category', 'featured', 'active', 'machine_type', 'door_type')
    search_fields = ('name', 'short_description', 'description', 'features', 'capacity', 'application')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('featured_image_preview',)
    inlines = [ProductImageInline]

    fieldsets = (
        ("Core Details", {
            "fields": ("category", "name", "slug", "short_description", "description", ("featured_image", "featured_image_preview"))
        }),
        ("Technical Specifications", {
            "fields": (
                ("capacity", "speed"),
                ("number_of_stops", "drive_type"),
                ("machine_type", "door_type"),
                ("pit_depth", "overhead"),
                ("power_supply", "application"),
            )
        }),
        ("Features & Custom Cabin Finishes", {
            "fields": ("features", "technical_specifications", "finishes")
        }),
        ("Marketing & Documentation", {
            "fields": ("brochure", ("featured", "active", "display_order"))
        }),
        ("SEO Meta Tags", {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse",)
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="height: 40px; width: 55px; object-fit: cover; border-radius: 4px;" />', obj.featured_image.url)
        return "—"
    image_preview.short_description = "Photo"

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 180px; border-radius: 6px;" />', obj.featured_image.url)
        return "No image uploaded"
    featured_image_preview.short_description = "Featured Image Preview"
