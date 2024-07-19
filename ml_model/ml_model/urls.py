# myapp/urls.py

from django.urls import path, include


urlpatterns = [
    path('api/', include('myapp.urls')),  # Include myapp-specific URLs
    # path('ml/', include('ml_model.urls')),  # Include ml_model-specific URLs
    # Add other paths specific to myapp
]
