import numpy as np
from datetime import datetime

def generate_json():
    data = {
        "timestamp": datetime.now().isoformat(),

        # Variables principales
        "te": float(np.random.normal(20, 2, 1)),     # Temperatura
        "hr": float(np.random.normal(70, 2, 1)),     # Humedad
        "pa": float(np.random.normal(900, 10, 1)),   # Presión atmosférica

        # Material particulado (MP)
        "p01": float(np.random.normal(10, 2, 1)),    # PM 1.0
        "p25": float(np.random.normal(30, 2, 1)),    # PM 2.5
        "p10": float(np.random.normal(100, 10, 1)),  # PM 10

        # Histogramas
        "h03": float(np.random.normal(1000, 10, 1)),
        "h05": float(np.random.normal(1000, 10, 1)),
        "h1":  float(np.random.normal(1000, 10, 1)),
        "h25": float(np.random.normal(1000, 10, 1)),
        "h5":  float(np.random.normal(1000, 10, 1)),
        "h10": float(np.random.normal(1000, 10, 1)),
    }

    return data

if __name__ == "__main__":
    print(generate_json())
