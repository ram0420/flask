# app.py로 명시해줘야 함. 안그럼 나중에 내가 따로 해줘야 한다구..
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
