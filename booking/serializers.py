from rest_framework import serializers
from .models import Booking, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer, _ = Customer.objects.get_or_create(**customer_data)
        return Booking.objects.create(customer=customer, **validated_data)
