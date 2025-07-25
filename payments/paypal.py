import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_paypal_access_token():
    url = f"{os.getenv('PAYPAL_API_BASE')}/v1/oauth2/token"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_CLIENT_SECRET"))
    )
    return response.json().get("access_token")

def create_paypal_order(amount, service_name, email):
    token = get_paypal_access_token()
    url = f"{os.getenv('PAYPAL_API_BASE')}/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": str(amount)
            },
            "description": f"Payment for {service_name} by {email}"
        }],
        "application_context": {
            "return_url": "https://yourdomain.com/success",
            "cancel_url": "https://yourdomain.com/cancel"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
