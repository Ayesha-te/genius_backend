from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to Genius Backend API",
        "routes": {
            "booking": "/api/booking/",
            "users": "/api/users/",
            "support": "/api/support/",
            "services": "/api/services/",
            "payments": "/api/payments/",
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/booking/', include('booking.urls')),
    path('api/users/', include('users.urls')),
    path('api/support/', include('support.urls')),
    path('api/services/', include('services.urls')),
    path('api/payments/', include('payments.urls')),
    path('', api_root),
]
