from django.urls import path
from services.views import service_list

urlpatterns = [
    path('', service_list),
]
