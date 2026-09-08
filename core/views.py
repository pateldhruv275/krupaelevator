from django.shortcuts import render, get_object_or_404
from .models import HeroSlider, Statistic, Feature, ProcessStep, Industry, Service, Client, Testimonial


def home(request):
    """
    Renders the dynamic corporate homepage for Krupa Elevator.
    Retrieves all sections from the database.
    """
    hero_slides = HeroSlider.objects.filter(active=True).order_by('display_order', '-created_at')
    statistics = Statistic.objects.filter(active=True).order_by('display_order')
    features = Feature.objects.filter(active=True).order_by('display_order')
    process_steps = ProcessStep.objects.filter(active=True).order_by('step_number', 'display_order')
    industries = Industry.objects.filter(active=True).order_by('display_order')
    services = Service.objects.filter(active=True).order_by('display_order')
    clients = Client.objects.filter(active=True).order_by('display_order')
    testimonials = Testimonial.objects.filter(active=True, featured=True).order_by('display_order', '-created_at')

    # Try to import ProductCategory for product categories grid on homepage
    try:
        from products.models import ProductCategory
        product_categories = ProductCategory.objects.filter(active=True).order_by('display_order')
    except Exception:
        product_categories = []

    # Try to import Project for featured showcase on homepage if projects app is available
    try:
        from projects.models import Project
        featured_projects = Project.objects.filter(active=True, featured=True).order_by('display_order', '-completion_date')[:6]
    except Exception:
        featured_projects = []

    # Try to import BlogPost for latest articles on homepage if blog app is available
    try:
        from blog.models import BlogPost
        latest_posts = BlogPost.objects.filter(active=True).order_by('-published_date')[:3]
    except Exception:
        latest_posts = []

    technology_features = [
        {
            'badge': 'Drive Engineering',
            'title': 'PMSM Gearless Traction Machines',
            'icon': 'bi-cpu-fill',
            'description': 'Permanent Magnet Synchronous Motors delivering up to 40% energy savings, zero gearbox friction, and ultra-quiet sound levels under 48 dB.',
            'specs': ['40% Power Reduction', 'No Oil Maintenance', 'Compact MRL Layout'],
        },
        {
            'badge': 'Motion Control',
            'title': 'Regenerative V3F Variable Frequency Drives',
            'icon': 'bi-lightning-charge-fill',
            'description': 'Closed-loop 32-bit vector inverters producing imperceptible S-curve acceleration and returning recovered kinetic power back to building power.',
            'specs': ['Jerk-Free S-Curve Profile', 'Power Factor > 0.95', 'Harmonics Suppression'],
        },
        {
            'badge': 'Intelligent Dispatch',
            'title': 'Microprocessor Group Collective Control',
            'icon': 'bi-diagram-3-fill',
            'description': 'Smart dispatching algorithms minimizing wait times during peak morning and evening traffic across multi-car commercial lift banks.',
            'specs': ['Duplex / Triplex Grouping', 'Real-Time Load Sensing', 'Peak-Hour Traffic Mode'],
        },
        {
            'badge': 'Blackout Safety',
            'title': 'Automatic Rescue Device (ARD)',
            'icon': 'bi-battery-charging',
            'description': 'Automatic battery takeover during municipal power cuts, slowly gliding the car to the nearest landing and unlocking doors safely.',
            'specs': ['SMF Battery Backup', 'Sub-30s Rescue Action', 'Fail-Safe Brake Locks'],
        },
        {
            'badge': 'Optical Safety',
            'title': '128-Beam Infrared Multi-Ray Curtains',
            'icon': 'bi-shield-shaded',
            'description': 'Dense optical curtain matrix scanning the entrance from sill to header, detecting obstructions instantaneously without physical touch.',
            'specs': ['128 Optical Beams', 'Zero Contact Safety', 'Full Height Coverage'],
        },
        {
            'badge': 'Structural Alignment',
            'title': 'Laser-Guided Hoistway Plumb Precision',
            'icon': 'bi-crosshair2',
            'description': 'Laser-guided rail alignment ensuring guide rail straightness within ±0.5 mm tolerances for whisper-quiet travel at speeds up to 2.5 m/s.',
            'specs': ['±0.5 mm Tolerance', 'Acoustics Under 50 dB', 'IS 14665 & EN-81 Norms'],
        },
    ]

    context = {
        'hero_slides': hero_slides,
        'statistics': statistics,
        'features': features,
        'process_steps': process_steps,
        'industries': industries,
        'services': services,
        'clients': clients,
        'testimonials': testimonials,
        'product_categories': product_categories,
        'technology_features': technology_features,
        'featured_projects': featured_projects,
        'latest_posts': latest_posts,
    }
    return render(request, 'pages/home.html', context)


def service_list(request):
    """
    Displays the full catalog of engineering, installation, and AMC services.
    """
    services = Service.objects.filter(active=True).order_by('display_order', 'id')
    return render(request, 'core/service_list.html', {'services': services})


def service_detail(request, slug):
    """
    Detailed scope of work, methodology, and engineering specifications for a service.
    """
    service = get_object_or_404(Service, slug=slug, active=True)
    all_services = Service.objects.filter(active=True).exclude(id=service.id).order_by('display_order')
    return render(request, 'core/service_detail.html', {
        'service': service,
        'features_list': service.get_features_list(),
        'all_services': all_services,
    })


def client_list(request):
    """
    Corporate clients, developers, and institutional partner portfolio.
    """
    clients = Client.objects.filter(active=True).order_by('display_order', 'name')
    return render(request, 'core/client_list.html', {'clients': clients})

