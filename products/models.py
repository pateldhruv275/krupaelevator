from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    """
    Elevator product category (e.g. Passenger Elevator, Hospital Elevator, Home Elevator).
    Controls dynamic navigation bar dropdown and category catalog views.
    """
    name = models.CharField(
        max_length=150, 
        unique=True,
        help_text="Category name, e.g. 'Passenger Elevator'"
    )
    slug = models.SlugField(
        max_length=160, 
        unique=True,
        help_text="SEO-friendly URL identifier"
    )
    short_description = models.CharField(
        max_length=255, 
        blank=True,
        help_text="Brief tagline or summary for cards and menus"
    )
    description = models.TextField(
        blank=True,
        help_text="Detailed category overview explaining engineering and use cases"
    )
    image = models.ImageField(
        upload_to='categories/', 
        blank=True, 
        null=True,
        help_text="Thumbnail image for category grids and preview cards"
    )
    banner_image = models.ImageField(
        upload_to='categories/banners/', 
        blank=True, 
        null=True,
        help_text="Header banner image for category landing pages"
    )
    icon = models.CharField(
        max_length=100, 
        default='bi-building',
        help_text="Bootstrap Icons class (e.g. bi-person-walking, bi-hospital, bi-house-heart)"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Ordering priority in menus and lists"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle visibility across website and navbar"
    )
    
    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, help_text="Custom HTML title for SEO")
    meta_description = models.TextField(blank=True, help_text="Meta description for search engines")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})

    @property
    def product_count(self):
        return self.products.filter(active=True).count()


class Product(models.Model):
    """
    Individual elevator models and engineered vertical mobility systems.
    """
    category = models.ForeignKey(
        ProductCategory, 
        on_delete=models.CASCADE, 
        related_name='products',
        help_text="Parent category"
    )
    name = models.CharField(
        max_length=180,
        help_text="Model / Product name (e.g. 'Standard Passenger Elevator')"
    )
    slug = models.SlugField(
        max_length=190, 
        unique=True,
        help_text="SEO-friendly URL identifier"
    )
    short_description = models.CharField(
        max_length=350, 
        blank=True,
        help_text="Concise product overview for catalog cards"
    )
    description = models.TextField(
        help_text="Comprehensive product description, architecture, and technology"
    )
    featured_image = models.ImageField(
        upload_to='products/featured/', 
        blank=True, 
        null=True,
        help_text="Primary product photograph for catalog and detail hero"
    )

    # Engineering Specifications
    capacity = models.CharField(
        max_length=120, 
        blank=True,
        help_text="e.g. 4 to 26 Passengers (320 kg - 2000 kg)"
    )
    speed = models.CharField(
        max_length=100, 
        blank=True,
        help_text="e.g. 0.65 m/s to 2.5 m/s"
    )
    number_of_stops = models.CharField(
        max_length=100, 
        blank=True,
        help_text="e.g. Up to 35 Floors (G+34)"
    )
    drive_type = models.CharField(
        max_length=120, 
        blank=True,
        help_text="e.g. Regenerative V3F Microprocessor Controller"
    )
    machine_type = models.CharField(
        max_length=120, 
        blank=True,
        help_text="e.g. Gearless PMSM / Geared Traction"
    )
    door_type = models.CharField(
        max_length=120, 
        blank=True,
        help_text="e.g. Center Opening / Side Opening Telescopic Automatic"
    )
    application = models.CharField(
        max_length=150, 
        blank=True,
        help_text="e.g. Residential High-Rises, Commercial Towers, Hotels"
    )
    pit_depth = models.CharField(
        max_length=100,
        blank=True,
        default="Min. 1400 mm",
        help_text="Minimum hoistway pit depth requirement"
    )
    overhead = models.CharField(
        max_length=100,
        blank=True,
        default="Min. 4200 mm",
        help_text="Minimum clear overhead clearance requirement"
    )
    power_supply = models.CharField(
        max_length=100,
        blank=True,
        default="415V, 3-Phase, 50Hz (Single-Phase option available)",
        help_text="Electrical power requirements"
    )

    # Narrative Lists
    features = models.TextField(
        blank=True,
        help_text="Key features and safety mechanisms (one item per line)"
    )
    technical_specifications = models.TextField(
        blank=True,
        help_text="Additional specifications in 'Key: Value' format (one per line)"
    )
    finishes = models.TextField(
        blank=True,
        help_text="Available cabin interior finishes and decorative styles (one per line)"
    )

    # Document & Marketing
    brochure = models.FileField(
        upload_to='products/brochures/', 
        blank=True, 
        null=True,
        help_text="Upload technical brochure (PDF format recommended)"
    )
    featured = models.BooleanField(
        default=False,
        help_text="Highlight on homepage or top catalog section"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle product visibility"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Display sequence"
    )

    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, help_text="Custom HTML page title")
    meta_description = models.TextField(blank=True, help_text="Meta description for search engines")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Elevator Product"
        verbose_name_plural = "Elevator Products"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'category_slug': self.category.slug, 'slug': self.slug})

    def get_features_list(self):
        """Returns features as a clean list stripped of whitespace."""
        if not self.features:
            return []
        return [f.strip() for f in self.features.splitlines() if f.strip()]

    def get_finishes_list(self):
        """Returns finishes as a clean list stripped of whitespace."""
        if not self.finishes:
            return []
        return [f.strip() for f in self.finishes.splitlines() if f.strip()]

    def get_specs_list(self):
        """Returns technical specifications as a list of (key, value) tuples."""
        if not self.technical_specifications:
            return []
        specs = []
        for line in self.technical_specifications.splitlines():
            line = line.strip()
            if ':' in line:
                key, val = line.split(':', 1)
                specs.append((key.strip(), val.strip()))
            elif line:
                specs.append((line, ''))
        return specs


class ProductImage(models.Model):
    """
    Supplementary gallery photographs for a product (cabin interiors, machines, finishes).
    """
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(
        upload_to='products/gallery/',
        help_text="Gallery image photograph"
    )
    caption = models.CharField(
        max_length=200, 
        blank=True,
        help_text="Optional description for lightbox and alt tag"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in product gallery"
    )

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Product Gallery Image"
        verbose_name_plural = "Product Gallery Images"

    def __str__(self):
        return f"Image for {self.product.name} ({self.caption or self.id})"
