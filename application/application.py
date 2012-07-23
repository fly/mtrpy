from flask import Flask, request
from pbs import mtr

app = Flask(__name__)

@app.route('/')
def displayMTR():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = mtr("-r","-w",clientIP).stdout
    return "<pre>" + reportMTR + "</pre>"

if __name__ == '__main__':
    app.run()
