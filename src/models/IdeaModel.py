from enum import Enum
from datetime import datetime

from marshmallow import fields, Schema
from marshmallow_enum import EnumField

from . import db


class Position(Enum):
    BUY = 'buy'
    SELL = 'sell'
    HOLD = 'hold'


class IdeaModel(db.Model):
    """
    flask-sqlalchemy db object to store the ideas in the db

    :iden: internal identifier of idea
    :reuters_id: is our unique identifier (not ticker)
    :author: ID - will be taken from nodejs user object. It looks like 5cf049669faa622b7486dbe2

    """

    __tablename__ = 'ideas'

    def __init__(self, data: dict):
        self.reuters_id = data.get('reuters_id')
        self.company = data.get('company')
        self.author = data.get('author')
        self.market = data.get('market')
        self.position = data.get('position')
        self.thesis = data.get('thesis')
        self.metadata_ = data.get('metadata_')

    iden = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
    reuters_id = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    market = db.Column(db.String, nullable=False)
    position = db.Column(db.Enum, nullable=False)
    thesis = db.Column(db.String, nullable=False)
    metadata_ = db.Column(db.String, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data: dict):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all(limit: int):
        return IdeaModel.query.limit(limit).all()

    @staticmethod
    def get(iden: int):
        return IdeaModel.query.get(iden)


class IdeaSchema(Schema):
    """
    Idea Schema (marshmallow)

    """

    iden = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    reuters_id = fields.Str(required=True)
    company = fields.Str(required=True)
    author = fields.Str(required=True)
    market = fields.Str(required=True)
    position = EnumField(Position, by_value=True)
    thesis = fields.Str(required=True)
    metadata_ = fields.Str(required=True)
