from datetime import datetime
from .models import SiteSettings


def site_context(request):
    """
    Supplies global corporate metadata, contact channels, branding,
    and year info to all templates without hardcoding.
    """
    try:
        settings_obj = SiteSettings.get_settings()
    except Exception:
        settings_obj = None

    return {
        'site_settings': settings_obj,
        'current_year': datetime.now().year,
    }
