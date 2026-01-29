from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# 🔴 CAMBIA usuario, password y cluster
app.config["MONGO_URI"] = (
    "mongodb+srv://gabriel:1234@proyectoia.ubbwsgi.mongodb.net/main"
    "?retryWrites=true&w=majority"
)

mongo = PyMongo(app)


@app.route("/")
def test_connection():
    # insertar algo
    result = mongo.db.main.insert_one({
        "mensaje": "Hola MongoDB Atlas 🚀"
    })

    # leer lo insertado
    doc = mongo.db.main.find_one(
        {"_id": result.inserted_id}
    )

    # convertir ObjectId a string
    doc["_id"] = str(doc["_id"])

    return jsonify({
        "status": "OK",
        "documento": doc
    })


if __name__ == "__main__":
    app.run(debug=True)