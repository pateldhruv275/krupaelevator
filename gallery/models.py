from django.db import models


class GalleryCategory(models.Model):
    """
    Categorization for photo gallery (e.g. 'Cabin Interiors', 'Panoramic Lifts', 'Industrial Installations').
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110, unique=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name

    @property
    def image_count(self):
        return self.images.filter(active=True).count()


class GalleryImage(models.Model):
    """
    High-resolution elevator photographs rendered in masonry grid with lightbox.
    """
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=150, help_text="Title / Caption for image")
    image = models.ImageField(upload_to='gallery/', help_text="Photograph")
    description = models.TextField(blank=True, help_text="Context or technical details for lightbox popup")
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"{self.title} ({self.category.name})"
