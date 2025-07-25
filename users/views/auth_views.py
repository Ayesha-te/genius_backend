from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    if not all([name, email, password]):
        return Response({'error': 'All fields are required.'}, status=400)

    if User.objects.filter(username=email).exists():
        return Response({'error': 'User already exists.'}, status=400)

    user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
    token = Token.objects.create(user=user)
    return Response({'token': token.key}, status=201)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'})
