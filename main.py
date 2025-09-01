import os
import requests
import time
import hmac
import hashlib

API_KEY = os.getenv("MEXC_API_KEY")
API_SECRET = os.getenv("MEXC_API_SECRET")

base_url = "https://api.mexc.com"

def sign_request(query_string: str) -> str:
    return hmac.new(
        API_SECRET.encode("utf-8"),
        query_string.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

def get_account_info():
    timestamp = str(int(time.time() * 1000))
    query = f"timestamp={timestamp}&recvWindow=5000"
    signature = sign_request(query)
    url = f"{base_url}/api/v3/account?{query}&signature={signature}"
    headers = {"X-MEXC-APIKEY": API_KEY}
    resp = requests.get(url, headers=headers)
    print("Status:", resp.status_code)
    print("Response:", resp.text)

if __name__ == "__main__":
    get_account_info()

