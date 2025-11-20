import json
import time
import paho.mqtt.client as mqtt
from json_generator import generate_json

BROKER = "localhost"
PORT = 1883
TOPIC = "sensores"

USERNAME = "estudiante"   # el mismo del mosquitto_passwd
PASSWORD = "papa123"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT correctamente.")
    else:
        print("Error al conectar. Código:", rc)

def mqtt_publish():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect

    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()

    data = generate_json()
    payload = json.dumps(data)

    print("JSON generado para publicar:", payload)

    result = client.publish(TOPIC, payload)
    status = result[0]

    if status == 0:
        print(f"Mensaje enviado al tópico `{TOPIC}`")
    else:
        print(f"Error al enviar mensaje al tópico `{TOPIC}`")

    time.sleep(1)
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    mqtt_publish()
