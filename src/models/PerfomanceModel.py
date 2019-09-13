from . import db


class PerformanceModel(db.Model):
    """

    flask-sqlalchemy db object to store the performance data
    """

    __tablename__ = 'performances'

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
    def get_all():
        return PerformanceModel.query.all()

    @staticmethod
    def get(iden: str):
        return PerformanceModel.query.get(iden)
