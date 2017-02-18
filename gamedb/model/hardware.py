from gamedb import db


class Hardware(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    manufacturer = db.relationship("Company")

    def __repr__(self):
        return "<Hardware {name}>".format(name=self.name)
