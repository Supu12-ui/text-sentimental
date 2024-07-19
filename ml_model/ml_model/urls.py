# myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('myapp.urls')),  # Include your API URLs
]
