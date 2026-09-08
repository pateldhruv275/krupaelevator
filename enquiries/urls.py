from django.urls import path
from . import views

app_name = 'enquiries'

urlpatterns = [
    path('quote/', views.quote_request_view, name='quote_request'),
    path('request-a-quote/', views.quote_request_view, name='request_a_quote'),
    path('contact/', views.contact_view, name='contact'),
]

