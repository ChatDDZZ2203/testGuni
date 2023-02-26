from flask import Flask, request
import os

app = Flask(__name__)

@app.before_request
def test():
    a = int(os.getenv("NUM"))
    if request.method == 'HEAD':
        a = 227
    b = 1
    return f"{a + b}"

