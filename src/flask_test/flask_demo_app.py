'''
Created on Oct 31, 2013

@author: Strahinja
'''
from flask import Flask, jsonify, request

app = Flask(__name__)

names = ["Laza", "Pera", "Mika", "Zika"]

@app.route("/names/", methods=['GET'])
def getNames():
    return jsonify({ 'tasks': names })


@app.route("/names/", methods=['PUT'])
def addName():
    names.append(request.json["name"])
    return jsonify({ 'result': "ok"})

if __name__ == "__main__":
    app.run()
    
