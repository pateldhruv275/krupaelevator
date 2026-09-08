from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import ProductCategory, Product


def product_list(request):
    """
    Renders the complete product catalog.
    Supports filtering by category and search queries.
    """
    categories = ProductCategory.objects.filter(active=True).order_by('display_order', 'name')
    products = Product.objects.filter(active=True).select_related('category').order_by('display_order', '-created_at')

    selected_category_slug = request.GET.get('category', '').strip()
    selected_category = None
    if selected_category_slug:
        selected_category = categories.filter(slug=selected_category_slug).first()
        if selected_category:
            products = products.filter(category=selected_category)

    search_query = request.GET.get('q', '').strip()
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(features__icontains=search_query) |
            Q(machine_type__icontains=search_query) |
            Q(application__icontains=search_query)
        )

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'selected_category_slug': selected_category_slug,
        'search_query': search_query,
        'total_count': products.count(),
    }
    return render(request, 'products/product_list.html', context)


def category_detail(request, slug):
    """
    Displays landing showcase for a specific elevator category.
    """
    category = get_object_or_404(ProductCategory, slug=slug, active=True)
    products = category.products.filter(active=True).order_by('display_order', '-created_at')
    all_categories = ProductCategory.objects.filter(active=True).exclude(id=category.id).order_by('display_order', 'name')

    context = {
        'category': category,
        'products': products,
        'all_categories': all_categories,
    }
    return render(request, 'products/category_detail.html', context)


def product_detail(request, category_slug, slug):
    """
    Comprehensive product specification sheet, gallery, and brochure download.
    """
    product = get_object_or_404(
        Product.objects.select_related('category').prefetch_related('images'),
        slug=slug,
        category__slug=category_slug,
        active=True
    )
    related_products = Product.objects.filter(
        category=product.category, 
        active=True
    ).exclude(id=product.id).order_by('display_order', '-created_at')[:3]

    context = {
        'product': product,
        'category': product.category,
        'images': product.images.all(),
        'features_list': product.get_features_list(),
        'finishes_list': product.get_finishes_list(),
        'specs_list': product.get_specs_list(),
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


def product_detail_direct(request, slug):
    """
    Resolves /products/<slug>/ flexibly:
    If the slug matches a Category, renders the category landing page.
    If the slug matches a Product, renders the product detail page.
    """
    # Check if category
    cat = ProductCategory.objects.filter(slug=slug, active=True).first()
    if cat:
        return category_detail(request, slug)

    # Check if product
    prod = Product.objects.filter(slug=slug, active=True).select_related('category').first()
    if prod:
        return redirect('products:detail', category_slug=prod.category.slug, slug=prod.slug)

    return get_object_or_404(Product, slug=slug, active=True)
