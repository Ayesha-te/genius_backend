from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def service_list(request):
    mock_services = [
        {"name": "MOT Test", "price": 50},
        {"name": "Oil Change", "price": 40},
        {"name": "Brake Inspection", "price": 60},
        {"name": "Tyre Replacement", "price": 80},
        {"name": "Battery Check", "price": 35}
    ]
    return Response(mock_services)
