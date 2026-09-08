from .models import ProductCategory


def product_categories(request):
    """
    Exposes active product categories to all templates for the dynamic navigation dropdown.
    """
    try:
        categories = ProductCategory.objects.filter(active=True).order_by('display_order', 'name')
    except Exception:
        categories = []

    return {
        'navbar_categories': categories,
    }
