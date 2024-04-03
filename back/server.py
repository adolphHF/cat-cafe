from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from back.crud.crud import getCat
#back.crud.crud and getCat must be replaced with back.repository.filename https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

app = Flask(__name__)
CORS(app)

@app.route("/api/cats")
def getCats():
    cats = "cats data"
    return cats

@app.route("/api/cats", methods = ['POST'])
def createCat():
    if request.method == "POST":

        return jsonify({"response": "Gato creado exitosamente"})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)