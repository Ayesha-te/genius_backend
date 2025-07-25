import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from payments.paypal import get_paypal_access_token, create_paypal_order

# Will use sandbox by default, good for both localhost & Render
PAYPAL_API_BASE = config('PAYPAL_API_BASE', default='https://api-m.sandbox.paypal.com')


@csrf_exempt
def create_paypal_checkout(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        # Try to parse JSON body
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            # Fallback: parse as form data (for browser form submission)
            data = request.POST

        service_name = data.get("service_name")
        email = data.get("email")
        amount = data.get("amount")

        if not all([service_name, email, amount]):
            return JsonResponse({"error": "Missing data"}, status=400)

        order = create_paypal_order(amount, service_name, email)
        approval_url = next(link["href"] for link in order["links"] if link["rel"] == "approve")

        return JsonResponse({"approval_url": approval_url})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def capture_paypal_order(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        order_id = data.get("order_id")
        if not order_id:
            return JsonResponse({"error": "Missing order_id"}, status=400)

        access_token = get_paypal_access_token()

        response = requests.post(
            f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"
            }
        )

        result = response.json()

        if response.status_code in [200, 201]:
            return JsonResponse({
                "status": "success",
                "order_id": order_id,
                "details": result
            })
        else:
            return JsonResponse({
                "error": "Capture failed",
                "paypal_response": result
            }, status=response.status_code)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
