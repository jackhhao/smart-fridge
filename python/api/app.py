from pymongo.errors import DuplicateKeyError
from flask_pymongo import PyMongo
from flask import Flask, request, url_for, jsonify
from flask import Flask, jsonify, request
from utils import config

# creating a Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = config["MONGO_URI"]
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404

@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=f"Duplicate key error."), 400

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num**2})

# driver function
if __name__ == '__main__':
    app.run(debug=True)