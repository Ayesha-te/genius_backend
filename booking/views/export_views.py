from rest_framework.decorators import api_view
from django.http import HttpResponse
import csv
from booking.models import Booking

@api_view(['GET'])
def export_bookings_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bookings.csv"'
    writer = csv.writer(response)
    writer.writerow(['Customer', 'Email', 'Phone', 'Service', 'Date', 'Time', 'Status'])

    for b in Booking.objects.all():
        writer.writerow([
            b.customer.name, b.customer.email, b.customer.phone,
            b.service, b.date, b.time, b.status
        ])
    return response
