# -*- coding: utf-8 -*-
'''
Created on Oct 31, 2013

@author: Strahinja
'''
from functools import wraps
from flask import Flask, jsonify, request, abort, Response, make_response

app = Flask(__name__)

names = []

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'admin'

def authenticate():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 401)
#     return jsonify({'bla':'bla'}, status=401)
#     """Sends a 401 response that enables basic auth"""
#     return Response(
#     'Could not verify your access level for that URL.\n'
#     'You have to login with proper credentials', 401,
#     {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
  
@app.route("/names", methods=["GET"])
def getNames():
    return jsonify({"names":names})


@app.route("/names", methods=["PUT"])
@requires_auth
def addName():
    names.append(request.json)
    return jsonify({"result":"ok"})


@app.route("/forward", methods=["POST"])
@requires_auth
def forward():
    if not request.json:
        abort(400)
    return jsonify(request.json)
    
if __name__ == "__main__":
    app.run(debug=True)
    
