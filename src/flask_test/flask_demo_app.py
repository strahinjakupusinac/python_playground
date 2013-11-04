# -*- coding: utf-8 -*-
'''
Created on Oct 31, 2013

@author: Strahinja
'''
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

names = []

@app.route("/names", methods=["GET"])
def getNames():
    return jsonify({"names":names})


@app.route("/names", methods=["PUT"])
def addName():
    names.append(request.json)
    return jsonify({"result":"ok"})


@app.route("/forward", methods=["POST"])
def forward():
    if not request.json:
        abort(400)
    return jsonify(request.json)
    
if __name__ == "__main__":
    app.run(debug=True)
    
