from gamedb import db


class Software(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    developer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    developer = db.relationship("Company")

    def __repr__(self):
        return "<Software {name}>".format(name=self.name)
