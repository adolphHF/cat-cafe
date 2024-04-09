from flask import Blueprint
#here we should import the queries from repository
import back.repository.cat.repository.py

catRoutes = Blueprint("catRoutes", __name__, template_folder="blueprints")

@catRoutes.route("/")
def home():
    return "<h1>Cat Routes Home</h1>"