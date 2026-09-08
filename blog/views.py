from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from .models import BlogCategory, BlogPost


def blog_list(request):
    """
    Blog archive with category filter, search query, and pagination.
    """
    posts = BlogPost.objects.filter(active=True).select_related('category')
    categories = BlogCategory.objects.filter(active=True).order_by('display_order')

    search_query = request.GET.get('q', '').strip()
    selected_category_slug = request.GET.get('category', '').strip()
    selected_category = None

    if selected_category_slug:
        selected_category = get_object_or_404(BlogCategory, slug=selected_category_slug, active=True)
        posts = posts.filter(category=selected_category)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(summary__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )

    # Optional featured hero article (shown only when no active filter/search and on page 1)
    page_number = request.GET.get('page', 1)
    featured_post = None
    if not search_query and not selected_category_slug and str(page_number) in ('1', ''):
        featured_post = posts.filter(featured=True).first()

    # Pagination: 6 posts per page
    paginator = Paginator(posts, 6)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'featured_post': featured_post,
        'total_count': paginator.count,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_category(request, slug):
    """
    Category-specific blog archive.
    """
    category = get_object_or_404(BlogCategory, slug=slug, active=True)
    posts = BlogPost.objects.filter(category=category, active=True).select_related('category')
    categories = BlogCategory.objects.filter(active=True).order_by('display_order')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'category': category,
        'selected_category': category,
        'categories': categories,
        'total_count': paginator.count,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """
    In-depth article reader with views increment, sidebar categories, and related articles.
    """
    post = get_object_or_404(BlogPost.objects.select_related('category'), slug=slug, active=True)

    # Increment view counter atomic
    BlogPost.objects.filter(pk=post.pk).update(views_count=F('views_count') + 1)
    post.refresh_from_db(fields=['views_count'])

    related_posts = BlogPost.objects.filter(
        category=post.category,
        active=True
    ).exclude(pk=post.pk).order_by('-published_date')[:3]

    recent_posts = BlogPost.objects.filter(
        active=True
    ).exclude(pk=post.pk).order_by('-published_date')[:4]

    categories = BlogCategory.objects.filter(active=True).order_by('display_order')

    context = {
        'post': post,
        'related_posts': related_posts,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/blog_detail.html', context)
