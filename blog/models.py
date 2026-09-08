from django.db import models
from django.urls import reverse
from django.utils import timezone


class BlogCategory(models.Model):
    """
    Category classification for elevator engineering articles, regulatory guides, and industry news.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    @property
    def post_count(self):
        return self.posts.filter(active=True).count()


class BlogPost(models.Model):
    """
    Technical thought leadership, IS/EN safety compliance updates, and elevator maintenance guides.
    """
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=220, help_text="Headline for article")
    slug = models.SlugField(max_length=240, unique=True, help_text="SEO URL slug")
    author = models.CharField(max_length=100, default="Krupa Engineering Team")
    summary = models.TextField(help_text="Short lead-in summary (2-3 sentences) for index cards")
    content = models.TextField(help_text="Full article narrative, technical breakdown, and engineering insights")
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    reading_time = models.PositiveIntegerField(default=4, help_text="Estimated minutes to read")
    views_count = models.PositiveIntegerField(default=0, help_text="Pageview counter")
    published_date = models.DateTimeField(default=timezone.now, db_index=True)
    featured = models.BooleanField(default=False, help_text="Highlight as featured hero story")
    active = models.BooleanField(default=True)

    # SEO
    meta_title = models.CharField(max_length=220, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
