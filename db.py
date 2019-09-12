from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

user = "admin"
password = "Summer2019"
db = f"mysql://{user}:{password}ideas-collector.csiaqjz2well.us-east-2.rds.amazonaws.com:3306@/ideas-collector"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db
db = SQLAlchemy(app)

"""
This file creates all of the classes for the SQL-Alchemy ORM.
For each class, SQL-Alchemy will create a DB table to store data.
:reuters_id: is our unique identifier (not ticker)
:iden: is our internal identifier
"""

class Idea(db.Model):
    # flask-sqlalchemy db object to store the ideas in the db
    #TODO add linkage between the author and the author
    iden = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    reuters_id = db.Column(db.String, nullable=False)
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
    # flask-sqlalchemy db object to store the performance data
    iden = db.Column(db.Integer, primary_key=True)
    reuters_id = db.Column(db.String, nullable=False)
    L1M = db.Column(db.Numeric)
    L1Y = db.Column(db.Numeric)
    YTD = db.Column(db.Numeric)
    since_inception = db.Column(db.Numeric)

#TODO add ds2 pricing table schema
#TODO add a table with company name, ticker, RIC (i.e mapping table) for search
