#!/bin/python

# Flask server to aggregate search torrents sites so they can be
# searched on a phone without infecting it with horrible malware and
# addverts. Will also support upload to synalogy nas download center

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
