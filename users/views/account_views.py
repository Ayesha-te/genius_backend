from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    current_password = request.data.get("current_password")
    new_password = request.data.get("new_password")

    if not user.check_password(current_password):
        return Response({"error": "Current password is incorrect."}, status=400)

    user.set_password(new_password)
    user.save()
    return Response({"message": "Password changed successfully."})

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if not email:
        return Response({"error": "Email is required"}, status=400)

    try:
        user = User.objects.get(email=email)
        temp_password = User.objects.make_random_password()
        user.set_password(temp_password)
        user.save()

        send_mail(
            'Password Reset',
            f'Your temporary password is: {temp_password}',
            'your@email.com',
            [email],
            fail_silently=False,
        )

        return Response({"message": "Temporary password sent to your email."})
    except User.DoesNotExist:
        return Response({"error": "User with this email does not exist."}, status=404)
