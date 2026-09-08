from django.db import models
from django.urls import reverse


class SiteSettings(models.Model):
    """
    Global site configuration and corporate identity for Krupa Elevator.
    Enforces a singleton pattern so only one configuration row exists.
    """
    company_name = models.CharField(
        max_length=150, 
        default="Krupa Elevator",
        help_text="Corporate entity name"
    )
    tagline = models.CharField(
        max_length=255, 
        default="Engineering Precision. Supreme Safety. Elevated Living.",
        help_text="Brand slogan or tagline"
    )
    logo = models.ImageField(
        upload_to='settings/', 
        blank=True, 
        null=True,
        help_text="Primary corporate logo (PNG / SVG recommended)"
    )
    favicon = models.ImageField(
        upload_to='settings/', 
        blank=True, 
        null=True,
        help_text="Browser favicon icon"
    )
    phone = models.CharField(
        max_length=30, 
        default="+91 98765 43210",
        help_text="Primary business phone number"
    )
    alternate_phone = models.CharField(
        max_length=30, 
        blank=True, 
        default="+91 98765 43211",
        help_text="Secondary/sales phone number"
    )
    email = models.EmailField(
        default="info@krupaelevator.com",
        help_text="Primary contact email address"
    )
    whatsapp = models.CharField(
        max_length=30, 
        default="+919876543210",
        help_text="WhatsApp contact number including country code without spaces"
    )
    address = models.TextField(
        default="Plot No. 42, Engineering Zone, GIDC Industrial Estate, Ahmedabad, Gujarat 382445, India",
        help_text="Physical factory / corporate office address"
    )
    working_hours = models.CharField(
        max_length=150,
        default="Mon - Sat: 9:00 AM - 7:00 PM | 24x7 Breakdown Response",
        help_text="Operational office & emergency support timings"
    )
    emergency_helpline = models.CharField(
        max_length=30,
        default="+91 98765 43210",
        help_text="Dedicated 24/7 elevator rescue & breakdown hotline"
    )
    google_map_embed = models.TextField(
        blank=True,
        help_text="Google Maps iframe HTML or URL embed for contact section"
    )
    facebook = models.URLField(blank=True, help_text="Facebook Page URL")
    instagram = models.URLField(blank=True, help_text="Instagram Profile URL")
    linkedin = models.URLField(blank=True, help_text="LinkedIn Company Page URL")
    youtube = models.URLField(blank=True, help_text="YouTube Channel URL")
    twitter = models.URLField(blank=True, help_text="Twitter / X Profile URL")
    footer_description = models.TextField(
        blank=True,
        default="Krupa Elevator is a trusted pioneer in state-of-the-art vertical transport solutions. We specialize in precision engineering, modern passenger lifts, high-capacity freight elevators, and responsive 24/7 maintenance services.",
        help_text="Descriptive summary displayed in the website footer"
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """Ensure only one instance of SiteSettings exists."""
        if not self.pk and SiteSettings.objects.exists():
            self.pk = SiteSettings.objects.first().pk
            kwargs.pop('force_insert', None)
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        """Retrieve existing settings or create a clean default instance."""
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


class HeroSlider(models.Model):
    """
    Dynamic slides for the prominent homepage hero banner carousel.
    """
    title = models.CharField(
        max_length=200,
        help_text="Bold headline, e.g., 'Next-Generation Vertical Mobility'"
    )
    subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Accent badge text, e.g., 'ISO 9001:2015 Certified Elevator Solutions'"
    )
    description = models.TextField(
        blank=True,
        help_text="Short narrative detailing engineering standards and client benefits"
    )
    image = models.ImageField(
        upload_to='hero/',
        blank=True,
        null=True,
        help_text="High-resolution hero banner photograph (1920x1080 recommended)"
    )
    button_text = models.CharField(
        max_length=50,
        default="Explore Products",
        help_text="Primary CTA button label"
    )
    button_url = models.CharField(
        max_length=255,
        default="#products",
        help_text="Primary CTA target URL"
    )
    secondary_button_text = models.CharField(
        max_length=50,
        blank=True,
        default="Request A Quote",
        help_text="Secondary CTA button label"
    )
    secondary_button_url = models.CharField(
        max_length=255,
        blank=True,
        default="#contact",
        help_text="Secondary CTA target URL"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle visibility on the homepage"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Sliders"

    def __str__(self):
        return self.title


class Statistic(models.Model):
    """
    Key performance indicators and trust metrics displayed on the homepage.
    """
    title = models.CharField(
        max_length=100,
        help_text="e.g. Years of Excellence, Elevators Installed, Happy Clients"
    )
    number = models.CharField(
        max_length=20,
        help_text="Metric number value, e.g. 15, 1200, 99"
    )
    suffix = models.CharField(
        max_length=10,
        blank=True,
        default="+",
        help_text="e.g. +, %, /7"
    )
    icon = models.CharField(
        max_length=100,
        default="bi-award",
        help_text="Bootstrap icon class (e.g. bi-award, bi-building-up, bi-people, bi-geo-alt)"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which metric is rendered"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle display on the homepage"
    )

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.title} ({self.number}{self.suffix})"


class Feature(models.Model):
    """
    Key engineering and service differentiators ("Why Choose Krupa Elevator").
    """
    title = models.CharField(
        max_length=150,
        help_text="e.g. Advanced German Technology, Uncompromising Safety"
    )
    description = models.TextField(
        help_text="Concise description highlighting engineering precision and reliability"
    )
    icon = models.CharField(
        max_length=100,
        default="bi-shield-check",
        help_text="Bootstrap icon class (e.g. bi-shield-check, bi-cpu, bi-lightning-charge, bi-tools)"
    )
    badge_text = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional highlight tag, e.g. 'Safety First', 'Eco-Smart'"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Display priority"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle display on the website"
    )

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Why Choose Us Feature"
        verbose_name_plural = "Why Choose Us Features"

    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    """
    The end-to-end execution workflow ("Our Process").
    """
    step_number = models.PositiveIntegerField(
        help_text="Sequence number (1, 2, 3...)"
    )
    title = models.CharField(
        max_length=150,
        help_text="e.g. Consultation, Site Survey, Design & Engineering, Manufacturing, Installation, Rigorous Testing, Handover & AMC"
    )
    short_description = models.TextField(
        help_text="Summary of activities performed in this stage"
    )
    icon = models.CharField(
        max_length=100,
        default="bi-gear-wide-connected",
        help_text="Bootstrap icon class"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Sequence order"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle display"
    )

    class Meta:
        ordering = ['step_number', 'display_order']
        verbose_name = "Process Step"
        verbose_name_plural = "Process Steps"

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class Industry(models.Model):
    """
    Sectors and market segments served by Krupa Elevator systems.
    """
    name = models.CharField(
        max_length=150,
        help_text="e.g. Residential High-Rises, Commercial Towers, Hospitals & Healthcare, Luxury Hotels, Industrial Facilities"
    )
    description = models.TextField(
        blank=True,
        help_text="Overview of specific vertical transport solutions engineered for this sector"
    )
    icon = models.CharField(
        max_length=100,
        default="bi-buildings",
        help_text="Bootstrap icon class"
    )
    image = models.ImageField(
        upload_to='industries/',
        blank=True,
        null=True,
        help_text="Representative sector photography"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order of appearance"
    )
    active = models.BooleanField(
        default=True,
        help_text="Toggle visibility"
    )

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Industry We Serve"
        verbose_name_plural = "Industries We Serve"

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Elevator lifecycle services: Installation, AMC, Modernization, Repair, Inspection, etc.
    """
    title = models.CharField(max_length=150, help_text="Service title, e.g. 'Elevator Installation'")
    slug = models.SlugField(max_length=160, unique=True, help_text="SEO slug, e.g. 'elevator-installation'")
    short_description = models.CharField(max_length=255, blank=True, help_text="Brief tagline for cards")
    description = models.TextField(help_text="Detailed service overview, methodology, and commitment")
    icon = models.CharField(max_length=100, default='bi-tools', help_text="Bootstrap Icons class")
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Banner/featured photograph")
    features = models.TextField(blank=True, help_text="Service scope, deliverables, or checklist (one per line)")
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:service_detail', kwargs={'slug': self.slug})

    def get_features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Client(models.Model):
    """
    Corporate clients, developers, and partner credentials.
    """
    name = models.CharField(max_length=150, help_text="Client or corporate developer name")
    logo = models.ImageField(upload_to='clients/', blank=True, null=True, help_text="Client brand logo")
    website = models.URLField(blank=True, help_text="Client website URL")
    industry = models.CharField(max_length=100, blank=True, help_text="e.g. Real Estate Developer, Healthcare, IT Park")
    description = models.TextField(blank=True, help_text="Brief partnership summary or elevator project scope")
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Client / Partner"
        verbose_name_plural = "Clients & Partners"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    """
    Client endorsements, feedback, and executive reviews.
    """
    RATING_CHOICES = [(i, f"{i} Stars") for i in range(1, 6)]

    client_name = models.CharField(max_length=120, help_text="Name of executive / reviewer")
    client_title = models.CharField(max_length=150, blank=True, help_text="e.g. Managing Director, Chief Engineer, Resident Society Secretary")
    company = models.CharField(max_length=150, blank=True, help_text="e.g. Skyline Developers, Apex Group")
    city = models.CharField(max_length=100, blank=True, help_text="e.g. Ahmedabad, Mumbai, Pune")
    elevator_type_installed = models.CharField(max_length=120, blank=True, help_text="e.g. Dual High-Speed MRL Passenger Lifts")
    rating = models.PositiveSmallIntegerField(default=5, choices=RATING_CHOICES, help_text="Rating out of 5 stars")
    quote = models.TextField(help_text="Client review or testimonial text")
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Client portrait or company representative")
    display_order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=True, help_text="Showcase on homepage carousel")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Client Testimonial"
        verbose_name_plural = "Client Testimonials"

    def __str__(self):
        return f"{self.client_name} - {self.company or self.city} ({self.rating}★)"

    @property
    def rating_range(self):
        return range(self.rating)

    @property
    def empty_rating_range(self):
        return range(5 - self.rating)
