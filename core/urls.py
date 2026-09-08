from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('clients/', views.client_list, name='clients'),
]
