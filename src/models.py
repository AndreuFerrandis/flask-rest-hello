from flask_sqlalchemy import SQLAlchemy

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    planet_name = db.Column(db.Integer, db.ForeignKey('planet.name'), nullable=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    people_name = db.Column(db.Integer, db.ForeignKey('people.name'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "planet_name": self.planet_name,
            "people_id": self.people_id,
            "people_name": self.people_name,
            # do not serialize the password, its a security breach
        }
    
    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    planet = db.relationship('Planet', backref=db.backref('favorites_planets', lazy=True))
    people = db.relationship('People', backref=db.backref('favorites_people', lazy=True))