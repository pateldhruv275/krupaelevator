"""
URL Configuration for Krupa Elevator Corporate Website.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('careers/', include('careers.urls', namespace='careers')),
    path('', include('enquiries.urls', namespace='enquiries')),
    path('', include('core.urls', namespace='core')),
]

# Serve media and static files in development & test
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path
from django.views.static import serve

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR / 'static'}),
]

# Custom Admin Site Header & Titles
admin.site.site_header = "Krupa Elevator Administration"
admin.site.site_title = "Krupa Elevator Portal"
admin.site.index_title = "Corporate Portal Management"
