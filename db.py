from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = "admin"
password = "Summer2019"
db = f"mysql://{user}:{password}ideas-collector.csiaqjz2well.us-east-2.rds.amazonaws.com:3306@/ideas-collector"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db
db = SQLAlchemy(app)


class Idea(db.Model):
    # flask-sqlalchemy db object to store the ideas in the db
    iden = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.Date, nullable=False)
    barrid = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    market = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    thesis = db.Column(db.String, nullable=False)
    metadata = db.Column(db.String, nullable=False)


class User(db.Model):
    # flask-sqlalchemy db object to store the users
    iden = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    born = db.Column(db.Date, nullable=False)
    status = db.Column(db.String, nullable=False)


class Performance(db.Model):
    # flask-sqlalchemy db object to store the performance
    iden = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String, nullable=False)
    L1M = db.Column(db.Numeric)
    L1Y = db.Column(db.Numeric)
    YTD = db.Column(db.Numeric)
    since_inception = db.Column(db.Numeric)
