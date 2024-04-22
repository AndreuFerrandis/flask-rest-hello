"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cambiar la URL de la base de datos según sea necesario
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define los modelos Planet, People y Favorite
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Agrega más campos según sea necesario

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Agrega más campos según sea necesario

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)

    # Define las relaciones entre Favorite y User, Planet, People
    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    planet = db.relationship('Planet', backref=db.backref('favorites', lazy=True))
    people = db.relationship('People', backref=db.backref('favorites', lazy=True))

# Implementa los endpoints GET
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Asume que el usuario actual se obtiene de alguna manera, por ejemplo, desde el token de autenticación
    current_user = User.query.first()

    user_favorites = Favorite.query.filter_by(user_id=current_user.id).all()
    return jsonify([favorite.serialize() for favorite in user_favorites]), 200

# Implementa los endpoints POST y DELETE
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_planet_favorite(planet_id):
    # Asume que el usuario actual se obtiene de alguna manera, por ejemplo, desde el token de autenticación
    current_user = User.query.first()

    new_favorite = Favorite(user_id=current_user.id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": "Planet added to favorites successfully"}), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_people_favorite(people_id):
    # Asume que el usuario actual se obtiene de alguna manera, por ejemplo, desde el token de autenticación
    current_user = User.query.first()

    new_favorite = Favorite(user_id=current_user.id, people_id=people_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": "People added to favorites successfully"}), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(planet_id):
    # Asume que el usuario actual se obtiene de alguna manera, por ejemplo, desde el token de autenticación
    current_user = User.query.first()

    favorite_to_delete = Favorite.query.filter_by(user_id=current_user.id, planet_id=planet_id).first()
    if favorite_to_delete:
        db.session.delete(favorite_to_delete)
        db.session.commit()
        return jsonify({"message": "Planet removed from favorites successfully"}), 200
    else:
        return jsonify({"message": "Planet is not in favorites"}), 404

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_people_favorite(people_id):
    # Asume que el usuario actual se obtiene de alguna manera, por ejemplo, desde el token de autenticación
    current_user = User.query.first()

    favorite_to_delete = Favorite.query.filter_by(user_id=current_user.id, people_id=people_id).first()
    if favorite_to_delete:
        db.session.delete(favorite_to_delete)
        db.session.commit()
        return jsonify({"message": "People removed from favorites successfully"}), 200
    else:
        return jsonify({"message": "People is not in favorites"}), 404

if __name__ == '__main__':
    app.run(debug=True)