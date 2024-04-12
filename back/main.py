from flask import Flask, render_template
from routes.blueprints.catRoutes import catRoutes
from routes.blueprints.userRoutes import userRoutes

app = Flask(__name__)
app.register_blueprint(catRoutes, url_prefix ="/cats")
app.register_blueprint(userRoutes, url_prefix ="/user")

@app.route("/")
def test():
    return "<h1>main test</h1>"

if __name__ == "__main__":
    app.run(debug=True)