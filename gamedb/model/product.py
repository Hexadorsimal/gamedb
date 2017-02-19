from gamedb import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    developer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    developer = db.relationship("Company")
