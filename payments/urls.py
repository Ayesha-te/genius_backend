from django.urls import path
from payments.views import create_paypal_checkout, capture_paypal_order

urlpatterns = [
    path('create-checkout/', create_paypal_checkout),
    path('capture-order/', capture_paypal_order),
]
