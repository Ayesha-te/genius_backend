from rest_framework.decorators import api_view
from rest_framework.response import Response
from support.models import ContactMessage
# from django.core.mail import send_mail  ← temporarily disabled

@api_view(['POST'])
def contact_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    subject = request.data.get('subject')
    message = request.data.get('message')

    if not all([name, email, subject, message]):
        return Response({"error": "All fields are required"}, status=400)

    # Save the contact message to the database
    ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message
    )

    # Email sending is temporarily disabled
    # full_message = f"From: {name} <{email}>\n\n{message}"
    # send_mail(
    #     subject,
    #     full_message,
    #     'noreply@yourdomain.com',
    #     ['your@email.com'],
    #     fail_silently=False
    # )

    return Response({"message": "Message received successfully."})
