from django.urls import path, include
from django.contrib import admin

# Serializers define the API representation.

urlpatterns = [
    path("", include("api.urls")),
    path("admin/", admin.site.urls)
]
