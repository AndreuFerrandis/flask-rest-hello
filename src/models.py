from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, nullable=True)
    people_id = db.Column(db.Integer,  nullable=True)
    

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            # do not serialize the password, its a security breach
        }
    
    @classmethod
    def delete_favorite(cls, favorite_id):
        favorite = cls.query.get(favorite_id)
        if favorite is None:
            return jsonify({"message": "Favorite not found"}), 404
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite removed successfully"}), 200