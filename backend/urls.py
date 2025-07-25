from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  # <-- Add this import

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "Welcome to Genius Backend API"})),  # <-- Add this line
    path('admin/', admin.site.urls),
    path('api/booking/', include('booking.urls')),
    path('api/users/', include('users.urls')),
    path('api/support/', include('support.urls')),
    path('api/services/', include('services.urls')),
    path('api/payments/', include('payments.urls')),
]
