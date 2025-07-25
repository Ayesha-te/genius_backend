from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/booking/', include('booking.urls')),
    path('api/users/', include('users.urls')),
    path('api/support/', include('support.urls')),
    path('api/services/', include('services.urls')),
    path('api/payments/', include('payments.urls')),
]
