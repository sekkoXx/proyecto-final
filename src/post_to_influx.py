import time
import requests
from json_generator import generate_json

INFLUX_URL = "http://localhost:8086/write?db=estaciones"

def send_to_influx(estacion="estacion_1"):
    data = generate_json()

    timestamp = int(time.time() * 1e9)  # tiempo en nanosegundos

    line = (
        f"ambiental,estacion={estacion} "
        f"te={data['te']},"
        f"hr={data['hr']},"
        f"pa={data['pa']},"
        f"p01={data['p01']},"
        f"p25={data['p25']},"
        f"p10={data['p10']},"
        f"h03={data['h03']},"
        f"h05={data['h05']},"
        f"h1={data['h1']},"
        f"h25={data['h25']},"
        f"h5={data['h5']},"
        f"h10={data['h10']} "
        f"{timestamp}"
    )

    response = requests.post(INFLUX_URL, data=line)

    print("Data enviada:", line)
    print("Status:", response.status_code)


if __name__ == "__main__":
    print("Enviando datos continuamente a InfluxDB...")
    while True:
        send_to_influx()
        time.sleep(1)   # enviar cada 1 segundo (puedes cambiarlo)
