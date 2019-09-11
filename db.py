from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = "admin"
password = "Summer2019"
db = f"mysql://{user}:{password}ideas-collector.csiaqjz2well.us-east-2.rds.amazonaws.com:3306@/ideas-collector"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()
