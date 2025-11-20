from flask import Flask, jsonify
import numpy as np
from datetime import datetime

app = Flask(__name__)

def generar_datos():
    return {
        "timestamp": datetime.now().isoformat(),
        "te": float(np.random.normal(20,2,1)),
        "hr": float(np.random.normal(70,2,1)),
        "pa": float(np.random.normal(900,10,1)),
        "p01": float(np.random.normal(10,2,1)),
        "p25": float(np.random.normal(30,2,1)),
        "p10": float(np.random.normal(100,10,1)),
        "h03": float(np.random.normal(1000,10,1)),
        "h05": float(np.random.normal(1000,10,1)),
        "h1": float(np.random.normal(1000,10,1)),
        "h25": float(np.random.normal(1000,10,1)),
        "h5": float(np.random.normal(1000,10,1)),
        "h10": float(np.random.normal(1000,10,1)),
    }

@app.route("/datos", methods=["POST"])
def datos():
    return jsonify(generar_datos())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
