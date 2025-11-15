import json
import paho.mqtt.client as mqtt
import requests

# -------------------------------------------------
# Configuración MQTT
# -------------------------------------------------
BROKER = "localhost"
PORT = 1883
TOPIC = "sensores"

USERNAME = "usuario"      # <-- reemplaza por tu usuario real
PASSWORD = "clave123"     # <-- reemplaza por tu clave real

# -------------------------------------------------
# Configuración Node-RED
# -------------------------------------------------
NODE_RED_URL = "http://localhost:1880/sensores_mqtt"  
# Recomiendo usar otro endpoint para diferenciar del POST normal

# -------------------------------------------------
# Callback cuando se conecta al broker
# -------------------------------------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado al broker MQTT")
        client.subscribe(TOPIC)
        print(f"📡 Suscrito al tópico: {TOPIC}")
    else:
        print("❌ Error al conectar. Código:", rc)

# -------------------------------------------------
# Callback cuando llega un mensaje MQTT
# -------------------------------------------------
def on_message(client, userdata, msg):
    print("\n📥 Mensaje recibido desde MQTT:")
    print("Tópico:", msg.topic)

    try:
        # Convertir mensaje JSON
        payload = json.loads(msg.payload.decode())
        print("JSON recibido:", payload)

        # Enviar a Node-RED
        print("\n➡ Enviando a Node-RED...")
        r = requests.post(NODE_RED_URL, json=payload)
        print("Response:", r.status_code, r.text)

    except Exception as e:
        print("❌ Error procesando mensaje:", e)

# -------------------------------------------------
# Main
# -------------------------------------------------
def start_subscriber():
    client = mqtt.Client()

    # Autenticación obligatoria
    client.username_pw_set(USERNAME, PASSWORD)

    # Asignar callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Conexión al broker
    client.connect(BROKER, PORT, keepalive=60)

    print("👂 Escuchando mensajes MQTT...\n")

    # Loop infinito
    client.loop_forever()

if __name__ == "__main__":
    start_subscriber()
