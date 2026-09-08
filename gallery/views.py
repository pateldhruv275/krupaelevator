from django.shortcuts import render
from .models import GalleryCategory, GalleryImage


def gallery_list(request):
    """
    Renders the responsive photo gallery with category filtering and interactive lightbox.
    """
    categories = GalleryCategory.objects.all().order_by('display_order', 'name')
    images = GalleryImage.objects.filter(active=True).select_related('category').order_by('display_order', '-created_at')

    selected_category_slug = request.GET.get('category', '').strip()
    selected_category = None
    if selected_category_slug:
        selected_category = categories.filter(slug=selected_category_slug).first()
        if selected_category:
            images = images.filter(category=selected_category)

    context = {
        'categories': categories,
        'images': images,
        'selected_category': selected_category,
        'selected_category_slug': selected_category_slug,
        'total_count': images.count(),
    }
    return render(request, 'gallery/gallery_list.html', context)
