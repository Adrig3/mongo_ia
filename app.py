from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# 🔴 CAMBIA usuario, password y cluster
app.config["MONGO_URI"] = (
    "mongodb+srv://gabriel:1234@proyectoia.ubbwsgi.mongodb.net/main"
    "?retryWrites=true&w=majority"
)

mongo = PyMongo(app)


@app.route("/")
def seleccion_ia():
    return render_template("index.html")


@app.route('/save', methods=['POST'])
def save_result():
    """Recibe JSON { ia: <str>, text: <str> } y lo inserta en la colección 'main' de la BD 'main'.
    Devuelve JSON con el id insertado.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'No JSON body provided'}), 400

    ia = data.get('ia')
    text = data.get('text')
    prompt = data.get('prompt')
    # Requerir que se haya seleccionado una IA y que el prompt del usuario no esté vacío
    if not ia:
        return jsonify({'error': 'Missing ia field'}), 400
    if not prompt or not str(prompt).strip():
        return jsonify({'error': 'Missing prompt field'}), 400

    doc = {
        'ia': ia,
        'text': text,
    }
    # guardar también el prompt del usuario si viene en la petición
    if prompt is not None:
        doc['prompt'] = prompt

    try:
        res = mongo.db.main.insert_one(doc)
    except Exception as e:
        return jsonify({'error': 'DB insert failed', 'detail': str(e)}), 500

    return jsonify({'id': str(res.inserted_id)})



if __name__ == "__main__":
    app.run(debug=True)