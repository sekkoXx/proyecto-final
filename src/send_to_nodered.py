import requests
from json_generator import generate_json

NODE_RED_URL = "http://localhost:1880/sensores"

def post_to_nodered():
    data = generate_json()
    print("JSON generado:", data)

    try:
        response = requests.post(NODE_RED_URL, json=data)
        print("Status Code:", response.status_code)
        print("Respuesta de Node-RED:", response.text)

    except Exception as e:
        print("Error al enviar datos a Node-RED:", e)

if __name__ == "__main__":
    post_to_nodered()
