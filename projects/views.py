from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Project


def project_list(request):
    """
    Project portfolio with multi-parameter filtering by city, project type, elevator type, and keyword search.
    """
    projects = Project.objects.filter(active=True).order_by('display_order', '-completion_date', '-created_at')

    # Distinct filter options for UI dropdowns
    available_cities = Project.objects.filter(active=True).values_list('city', flat=True).distinct().order_by('city')
    available_project_types = Project.objects.filter(active=True).values_list('project_type', flat=True).distinct().order_by('project_type')
    available_elevator_types = Project.objects.filter(active=True).values_list('elevator_type', flat=True).distinct().order_by('elevator_type')

    # Selected query parameters
    selected_city = request.GET.get('city', '').strip()
    selected_project_type = request.GET.get('project_type', '').strip()
    selected_elevator_type = request.GET.get('elevator_type', '').strip()
    search_query = request.GET.get('q', '').strip()

    if selected_city:
        projects = projects.filter(city__iexact=selected_city)
    if selected_project_type:
        projects = projects.filter(project_type__iexact=selected_project_type)
    if selected_elevator_type:
        projects = projects.filter(elevator_type__iexact=selected_elevator_type)
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(client_name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    context = {
        'projects': projects,
        'available_cities': available_cities,
        'available_project_types': available_project_types,
        'available_elevator_types': available_elevator_types,
        'selected_city': selected_city,
        'selected_project_type': selected_project_type,
        'selected_elevator_type': selected_elevator_type,
        'search_query': search_query,
        'total_count': projects.count(),
        'has_filters': bool(selected_city or selected_project_type or selected_elevator_type or search_query),
    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, slug):
    """
    In-depth case study of a completed elevator installation.
    """
    project = get_object_or_404(
        Project.objects.prefetch_related('images'),
        slug=slug,
        active=True
    )
    related_projects = Project.objects.filter(
        active=True
    ).filter(
        Q(project_type=project.project_type) | Q(city=project.city)
    ).exclude(id=project.id).order_by('display_order', '-completion_date')[:3]

    context = {
        'project': project,
        'images': project.images.all(),
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)
