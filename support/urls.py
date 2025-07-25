from django.urls import path
from support.views.contact_views import contact_view
from support.views.dvla_views import check_vehicle_view

urlpatterns = [
    path('contact/', contact_view),
   
     path('dvla/check-vehicle/', check_vehicle_view),
]
