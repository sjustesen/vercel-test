import os
from dotenv import load_dotenv
from flask import Flask
from convex import ConvexClient

load_dotenv(".env.local")
load_dotenv()

client = ConvexClient(os.getenv("CONVEX_URL"))


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
