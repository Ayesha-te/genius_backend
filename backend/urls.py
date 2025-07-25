from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # your API routes
    path('admin/', admin.site.urls),
    path('api/booking/', include('booking.urls')),
    path('api/users/', include('users.urls')),
    path('api/support/', include('support.urls')),
    path('api/services/', include('services.urls')),
    path('api/payments/', include('payments.urls')),

    # DRF Browsable API Root
    path('api/docs/', include_docs_urls(title='Genius Backend API')),
]
