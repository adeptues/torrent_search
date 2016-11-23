#!/bin/python

# Flask server to aggregate search torrents sites so they can be
# searched on a phone without infecting it with horrible malware and
# addverts. Will also support upload to synalogy nas download center

#TODO Make a properfactory loader class and such 
from flask import Flask
from flask import request
import requests
import json
from parser import NyaaParser, PirateParser
import config
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/search")
def search():
    search_text = request.args.get('searchText')
    site = request.args.get('site')
    print "searching for "+search_text+" with site "+str(site)
    results = do_search(search_text,site)
    output = []
    for r in results:
        output.append(r.__dict__)
    return json.dumps(output)

def search_factory(site):
    if site == 'nyaa':
        return search_nyaa
    if site == 'pirate':
        return search_pirate
    return None

def do_search(search_text,site_search):
    sites = ['pirate','nyaa']
    #TODO Do proper config externalisations
    # if site search then search that site only
    # otherwise
    if site_search is None or len(site_search) == 0:
        results = []
        for site in sites:
            # factory time
            fn = search_factory(site)
            site_results = fn(search_text)
            print str(len(site_results))+" from "+site
            results = site_results+results
        print str(len(results))+" from "+str(len(sites))+" sites"
        return results
    else:
        fn = search_factory(site_search)
        results = fn(search_text)
        print str(len(results))+" from "+site_search
        return results
            
def search_nyaa(search_text):
    url = config.NYAA+'/?page=search&cats=0_0&filter=0&term='+search_text
    r = requests.get(url)
    html = r.text
    parser = NyaaParser(html)
    entries = parser.parse()
    print "nyaa search"
    return entries

def search_pirate(search_text):
    print "pirate search"
    url = config.PIRATE_BAY+'/s/?q='+search_text+'&page=0&orderby=99'
    r = requests.get(url)
    html = r.text
    parser = PirateParser(html)
    entries = parser.parse()
    return entries


if __name__ == "__main__":
    app.run()
