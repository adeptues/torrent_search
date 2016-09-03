#!/bin/python

# Flask server to aggregate search torrents sites so they can be
# searched on a phone without infecting it with horrible malware and
# addverts. Will also support upload to synalogy nas download center

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/search")
def search():
    search_text = request.args.get('searchText')
    # for each site make search request
    # dispatch to aproriate parser
    # aggegate results into single list
    #return list
    return search_text

if __name__ == "__main__":
    app.run()
