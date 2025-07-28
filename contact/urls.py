# contact/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='home'),  # shows homepage with contact form
]
