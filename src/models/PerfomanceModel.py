from . import db
from marshmallow import fields, Schema


class PerformanceModel(db.Model):
    """
    flask-sqlalchemy db object to store the performance data
    """

    __tablename__ = 'performances'

    def __init__(self, data: dict):
        self.reuters_id = data.get('reuters_id')
        self.L1M = data.get('L1M')
        self.L1Y = data.get('L1Y')
        self.YTD = data.get('YTD')
        self.since_inception = data.get('since_inception')

    iden = db.Column(db.Integer, primary_key=True)
    reuters_id = db.Column(db.String, nullable=False)
    L1M = db.Column(db.Numeric)
    L1Y = db.Column(db.Numeric)
    YTD = db.Column(db.Numeric)
    since_inception = db.Column(db.Numeric)

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
        return PerformanceModel.query.limit(limit).all()

    @staticmethod
    def get(iden: int):
        return PerformanceModel.query.get(iden)


class PerformanceSchema(Schema):

    """
    marshmallow Performance Schema
    """

    iden = fields.Int(dump_only=True)
    reuters_id = fields.Str(required=True)
    L1M = fields.Number(required=True)
    L1Y = fields.Number(required=True)
    YTD = fields.Number(required=True)
    since_inception = fields.Number(required=True)
