from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    planet = db.relationship('Planet', backref=db.backref('favorites_planets', lazy=True))
    people = db.relationship('People', backref=db.backref('favorites_people', lazy=True))