import json
import time
import paho.mqtt.client as mqtt
from json_generator import generate_json

# Configuración del broker MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "sensores"

USERNAME = "usuario"      # <-- Cambiar por tu usuario real
PASSWORD = "clave123"     # <-- Cambiar por tu contraseña real

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT correctamente.")
    else:
        print("Error al conectar. Código:", rc)

def mqtt_publish():
    # Crear cliente MQTT
    client = mqtt.Client()

    # Credenciales para conexión segura
    client.username_pw_set(USERNAME, PASSWORD)

    # Callback de conexión
    client.on_connect = on_connect

    # Intentar conexión
    client.connect(BROKER, PORT, keepalive=60)

    # Iniciar loop de red en background
    client.loop_start()

    # Generar el JSON ambiental
    data = generate_json()
    print("JSON generado para publicar:", data)

    # Convertir a JSON string
    payload = json.dumps(data)

    # Publicar mensaje
    result = client.publish(TOPIC, payload)

    # Chequear si se envió correctamente
    status = result[0]
    if status == 0:
        print(f"Mensaje enviado al tópico `{TOPIC}`")
    else:
        print(f"Error al enviar mensaje al tópico `{TOPIC}`")

    # Esperar un momento y terminar
    time.sleep(1)
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    mqtt_publish()
