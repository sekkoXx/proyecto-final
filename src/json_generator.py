import random
import json
from datetime import datetime

def generate_json():
    data = {
        "timestamp": datetime.now().isoformat(),
        "temperature": random.uniform(20.0, 30.0),
        "humidity": random.uniform(30.0, 70.0),
        "pressure": random.uniform(1000.0, 1020.0),
        "light": random.randint(0, 100)
    }
    return json.dumps(data)

if __name__ == "__main__":
    print(generate_json())
