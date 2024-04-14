import sys
# setting path
sys.path.append('./catcafe')

from flask import Blueprint, g, jsonify
from flask import request

from database.connectionPool import ConnectionPool
from repository.cat_repository import CatRepository

cat_routes = Blueprint("cat_routes", __name__)

@cat_routes.before_request
def before_request():
    g.db = ConnectionPool.getConnection()

@cat_routes.teardown_request
def teardown_request(exception = None):
    if hasattr(g, 'db'):
        ConnectionPool.releaseConnection(g.db)

@cat_routes.route("/")
def catHome():
    return "<h1>Cat Home</h1>"

@cat_routes.route("/create", methods = ["POST"])
def createCat():
    try:
        name = request.form['name']
        age = request.form['age']
        race = request.form['race']
        sex = request.form['sex']

        print("name: "+name+" age: "+age+" race "+race+ " sex: "+sex)

        return jsonify({"message": "cat created successfully"}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500
    #finally:
    #    cursor.close()

@cat_routes.route("/get/all")
def getAllCats():
    try:
        return jsonify({"message": "all cats"}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500

@cat_routes.route("/get/one", methods = ["POST"])
def getOneCat():
    try:
        return jsonify({"message": "one cat"}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500
    
@cat_routes.route("/update/cat", methods = ["POST"])
def updateCat():
    try:
        return jsonify({"message":"updated cat info"}), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500
    
@cat_routes.route("/update/adopted", methods = ["POST"])
def updateIsAdopted():
    try:
        return jsonify({"message":"updated cat is adopted"}), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@cat_routes.route("/delete", methods = ["POST"])
def deleteCat():
    try:
        return  jsonify({"message":"deleted cat"}),200
    except Exception as e:
        return jsonify({'error':str(e)}),500