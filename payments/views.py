import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from payments.paypal import get_paypal_access_token, create_paypal_order
import os

@csrf_exempt
def create_paypal_checkout(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        data = json.loads(request.body)
        service_name = data.get("service_name")
        email = data.get("email")
        amount = data.get("amount")

        if not all([service_name, email, amount]):
            return JsonResponse({"error": "Missing data"}, status=400)

        order = create_paypal_order(amount, service_name, email)
        approval_url = next(link["href"] for link in order["links"] if link["rel"] == "approve")

        return JsonResponse({"approval_url": approval_url})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def capture_paypal_order(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        data = json.loads(request.body)
        order_id = data.get("order_id")

        if not order_id:
            return JsonResponse({"error": "Missing order_id"}, status=400)

        access_token = get_paypal_access_token()

        response = requests.post(
            f"{os.getenv('PAYPAL_API_BASE')}/v2/checkout/orders/{order_id}/capture",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"
            }
        )

        capture_result = response.json()

        if response.status_code == 201:
            return JsonResponse({
                "status": "success",
                "order_id": order_id,
                "details": capture_result
            })
        else:
            return JsonResponse({"error": "Capture failed", "details": capture_result}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
