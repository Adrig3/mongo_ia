# imports
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# bbdd
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20))
    autor = db.Column(db.String(20))
    genero = db.Column(db.String(10))
    fecha_publicacion = db.Column(db.String(20))

    def __repr__(self):
        return f'Libro {self.titulo}'

# endpoint de testing
@app.route('/prueba')
def prueba():
    return render_template("prueba.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)