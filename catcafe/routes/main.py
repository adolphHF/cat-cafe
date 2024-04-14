from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

from blueprints.application_routes import application_routes
from blueprints.cat_routes import cat_routes
from blueprints.user_routes import user_routes

#remember access via user_routes.user_routes
app.register_blueprint(user_routes, url_prefix = "/user")
app.register_blueprint(cat_routes, url_prefix = "/cat")
app.register_blueprint(application_routes, url_prefix = "/application")


@app.route("/")
def mainHome():
    return "Hello World main Home"

if __name__ == '__main__':
    app.run(debug=True)