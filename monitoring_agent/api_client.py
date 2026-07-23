import requests
from config import SERVER_URL


def post(endpoint, data):
    try:
        response = requests.post(
            f"{SERVER_URL}/api/{endpoint}",
            json=data,
            timeout=5
        )

        if response.status_code == 200:
            print(f"✅ {endpoint} sent successfully")
        else:
            print(f"❌ {endpoint} failed")
            print(response.text)

    except Exception as e:
        print("API Error:", e)