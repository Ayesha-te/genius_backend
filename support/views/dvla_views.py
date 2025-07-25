from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from decouple import config

DVLA_API_URL = config('DVLA_API_URL')
DVLA_API_KEY = config('DVLA_API_KEY')

@api_view(['POST'])
def check_vehicle_view(request):
    # Accept both snake_case and camelCase from frontend
    reg_number = request.data.get('registrationNumber') or request.data.get('registration_number')
    
    if not reg_number or not reg_number.strip():
        return Response({'error': 'Registration number is required.'}, status=400)

    headers = {
        'x-api-key': DVLA_API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        'registrationNumber': reg_number.strip().upper()  # DVLA prefers uppercase
    }

    try:
        response = requests.post(DVLA_API_URL, json=payload, headers=headers)
        return Response(response.json(), status=response.status_code)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
