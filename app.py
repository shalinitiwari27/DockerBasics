from flask import Flask
import pandas as pd
import numpy as nm

app = Flask(__name__)

@app.route('/', methods = ['Get'])
def hello_world():
    return "Welcome All to the basics of Docker"
    
if __name__ == "__main__":
    app.run()
    