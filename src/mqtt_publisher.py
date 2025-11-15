import requests
from json_generator import generate_json

NODE_RED_URL = "http://localhost:1880/endpoint"  # Reemplaza con tu URL de NodeRed

def send_to_nodered():
    data = generate_json()
    response = requests.post(NODE_RED_URL, json=data)
    print("Response status:", response.status_code)

if __name__ == "__main__":
    send_to_nodered()
