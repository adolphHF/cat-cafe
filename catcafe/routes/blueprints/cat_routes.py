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
    return "Cat Home"

@cat_routes.route("/create", methods = ["POST"])
def createCat():
    try:
        name = request.form['name']
        age = request.form['age']
        race = request.form['race']
        sex = request.form['sex']
        data = {
            "name": name,
            "age": age,
            "race": race,
            "sex": sex
        }
        conn = g.db
        cursor = conn.cursor()

        CatRepository.create(data, conn, cursor)

        return jsonify({"message": "cat created successfully"}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500
    finally:
        cursor.close()

@cat_routes.route("/get/all")
def getAllCats():
    try:
        conn = g.db
        cursor = conn.cursor()
        cats = CatRepository.getAll(conn,cursor)
        return cats, 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500

@cat_routes.route("/get/one", methods = ["POST"])
def getOneCat():
    try:
        conn = g.db
        cursor = conn.cursor()
        #TODO preguntarle a luisen si el id me lo pasa por el path o como un elemento
        catId = request.form["id"]
        cat = CatRepository.getOne(catId, cursor)
        return jsonify({"cat": cat}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500
    
@cat_routes.route("/update/catdata", methods = ["POST"])
def updateCat():
    try:
        name = request.form['name']
        age = request.form['age']
        race = request.form['race']
        sex = request.form['sex']
        catId = request.form['id']
        data = {
            "name": name,
            "age": age,
            "race": race,
            "sex": sex
        }
        conn = g.db
        cursor = conn.cursor()

        CatRepository.update(data, catId, conn, cursor)

        return jsonify({"message":"cat updated succesfully"}), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500
    
@cat_routes.route("/update/adopted", methods = ["POST"])
def updateIsAdopted():
    try:
        conn = g.db
        cursor = conn.cursor()
        isAdopted = request.form['adopted']
        catId = request.form['id']

        CatRepository.updateAdopted(isAdopted,catId, conn, cursor)
        return jsonify({"message":"cat is adopted updated succesfully"}), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@cat_routes.route("/delete", methods = ["POST"])
def deleteCat():
    try:
        conn = g.db
        cursor = conn.cursor()
        catId = request.form['id']
        CatRepository.delete(catId, conn, cursor)
        return  jsonify({"message":"deleted cat"}),200
    except Exception as e:
        return jsonify({'error':str(e)}),500