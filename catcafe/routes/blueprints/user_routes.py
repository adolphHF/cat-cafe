import sys
# setting path
sys.path.append('./catcafe')

from flask import Blueprint, g, jsonify
from flask import request
from database.connectionPool import ConnectionPool
from repository.user_repository import UserRepository

user_routes = Blueprint("user_routes", __name__)

@user_routes.before_request
def before_request():
    g.db = ConnectionPool.getConnection()

@user_routes.teardown_request
def teardown_request(exception = None):
    if hasattr(g, 'db'):
        ConnectionPool.releaseConnection(g.db)

@user_routes.route("/")
def userHome():
    return "<h1>User Home</h1>"

@user_routes.route("/validate", methods = ["POST"])
def validateUser():
    try:
        password = request.form['password']
        email = request.form['email']

        conn = g.db.connection
        cursor = conn.cursor()

        user = UserRepository.getUser(email, password, cursor)

        if user:
            return jsonify({"message": "user validated successfully"}), 200
        #TODO invoke the repository to do the query and then check if the data received via post is the same that in db
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        cursor.close()