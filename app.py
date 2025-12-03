# app.py
from flask import Flask
from api.spotify import generate_badge  # Ajusta según tu función real

app = Flask(__name__)

@app.route("/api/spotify")
def spotify():
    return generate_badge()
