from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    movies = db.relationship('movie', backref='author', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.username}')"
    
movie_list = db.Table('movie_list',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('list_id', db.Integer, db.ForeignKey('movielist.id'), primary_key=True)
)

class movielist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    movies = db.relationship('movie', secondary=movie_list, backref='lists', lazy=True)

    def __repr__(self):
        return f"List('{self.name}')"

class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posterURL = db.Column(db.String(200))
    tmdbID = db.Column(db.Integer)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}')"