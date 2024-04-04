from flask import Flask, render_template
from routes.blueprints.catRoutes import catRoutes

app = Flask(__name__)
app.register_blueprint(catRoutes, url_prefix ="/cats")

@app.route("/")
def test():
    return "<h1>main test</h1>"

if __name__ == "__main__":
    app.run(debug=True)