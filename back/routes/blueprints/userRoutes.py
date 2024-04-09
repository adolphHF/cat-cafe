from flask import Blueprint

userRoutes = Blueprint("userRoutes", __name__, template_folder= "blueprints")

@userRoutes.route("/")
def home():
    return "<h1>User Routes Home</h1>"

@userRoutes.route("/admin")
def createAdmin():
    return "<h1>Admin route"