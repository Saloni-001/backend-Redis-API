from django.urls import path
from . import views

urlpatterns = [
    path('device/latest-info/<int:device_id>/', views.latest_info),
    path('device/location/<int:device_id>/', views.device_location),
    path('device/location-history/<int:device_id>/', views.location_history),
]
