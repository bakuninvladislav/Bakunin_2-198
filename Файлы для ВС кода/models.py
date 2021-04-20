import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Cats(db.Model):
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    price = db.Column(db.Integer)