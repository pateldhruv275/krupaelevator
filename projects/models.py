from django.db import models
from django.urls import reverse


class Project(models.Model):
    """
    Completed or ongoing elevator engineering case studies & projects.
    """
    PROJECT_TYPE_CHOICES = [
        ('Residential', 'Residential High-Rise & Villas'),
        ('Commercial', 'Commercial & Corporate Towers'),
        ('Healthcare', 'Hospitals & Healthcare Facilities'),
        ('Hospitality', 'Hotels & Luxury Resorts'),
        ('Industrial', 'Industrial Plants & Warehouses'),
        ('Infrastructure', 'Infrastructure & Public Sector'),
    ]

    ELEVATOR_TYPE_CHOICES = [
        ('Passenger Elevator', 'Passenger Elevator'),
        ('MRL Elevator', 'Machine Room-Less (MRL) Elevator'),
        ('Hospital Stretcher Elevator', 'Hospital Stretcher Elevator'),
        ('Freight / Goods Elevator', 'Freight / Goods Elevator'),
        ('Panoramic Glass Elevator', 'Panoramic Glass Elevator'),
        ('Hydraulic Elevator', 'Hydraulic Elevator'),
        ('Home / Villa Elevator', 'Home / Villa Elevator'),
        ('Escalator', 'Commercial Escalator'),
    ]

    title = models.CharField(max_length=180, help_text="Project title, e.g. 'Skyline Heights Twin Towers'")
    slug = models.SlugField(max_length=190, unique=True, help_text="SEO slug")
    client_name = models.CharField(max_length=150, blank=True, help_text="Client or Developer name")
    location = models.CharField(max_length=200, help_text="Locality/Address, e.g. 'SG Highway, Bodakdev'")
    city = models.CharField(max_length=100, db_index=True, help_text="e.g. Ahmedabad, Surat, Vadodara, Mumbai")
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES, db_index=True)
    elevator_type = models.CharField(max_length=60, choices=ELEVATOR_TYPE_CHOICES, db_index=True)
    number_of_elevators = models.PositiveIntegerField(default=1, help_text="Total number of lift units installed")
    description = models.TextField(help_text="Project case study narrative, technical challenges, and solutions delivered")
    featured_image = models.ImageField(upload_to='projects/featured/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True, help_text="Commissioning / handover date")

    featured = models.BooleanField(default=False, help_text="Showcase on homepage")
    active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-completion_date', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.title} - {self.city}"

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})


class ProjectImage(models.Model):
    """
    Project installation photography, shaft erection photos, and cabin interiors.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Photo for {self.project.title} ({self.caption or self.id})"
