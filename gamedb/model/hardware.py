from gamedb import db


class Hardware(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    manufacturer = db.relationship("Company")

    def __repr__(self):
        return "<Hardware {name}>".format(name=self.name)
