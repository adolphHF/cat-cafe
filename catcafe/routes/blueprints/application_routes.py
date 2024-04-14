import sys
# setting path
sys.path.append('./catcafe')

from flask import Blueprint, g, jsonify
from flask import request
from database.connectionPool import ConnectionPool
from repository.application_repository import ApplicationRepository

application_routes = Blueprint("application_blueprint", __name__)

@application_routes.before_request
def before_request():
    g.db = ConnectionPool.getConnection()

@application_routes.teardown_request
def teardown_request(exception = None):
    if hasattr(g, 'db'):
        ConnectionPool.releaseConnection(g.db)

@application_routes.route("/")
def applicationHome():
    return "<h1>Application Home</h1>"

@application_routes.route("/create", methods=["POST"])
def createApplication():
    try:
        cat_id = request.form['cat_id']
        applicant_name = request.form['applicant_name']
        applicant_phone = request.form['applicant_phone']
        applicant_email = request.form['applicant_email']
        applicant_age = request.form['applicant_age']
        applicant_address = request.form['applicant_address']

        print("cat_id: "+cat_id+" applicant_name: "+applicant_name+" applicant_phone: "+applicant_phone+" applicant_email: "+applicant_email+" applicant_age: "+applicant_age+" applicant_address: "+applicant_address)
        return jsonify({"message": "application created succesfully"}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500
    
@application_routes.route("/get/all")
def getApplications():
    try:
        return jsonify({"message": "all cats"}), 200
    except Exception as e:
        return jsonify({ "error":str(e) }),500

#In case we need to get only one application
#@application_routes.route("/get")

@application_routes.route("/update/status", methods = ["POST"])
def updateStatus():
    try:
        return jsonify({"message":"updated application status"}), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@application_routes.route("/delete", methods = ["POST"])
def deleteApplication():
    try:
        return  jsonify({"message":"deleted cat"}),200
    except Exception as e:
        return jsonify({'error':str(e)}),500