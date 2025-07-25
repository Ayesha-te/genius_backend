from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.booking_views import BookingViewSet
from .views.export_views import export_bookings_csv

router = DefaultRouter()
router.register(r'', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export-csv/', export_bookings_csv),
]
