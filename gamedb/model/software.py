from gamedb import db


class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    developer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    developer = db.relationship("Company")
    publisher_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    publisher = db.relationship("Company")

    def __repr__(self):
        return "<Software {name}>".format(name=self.name)
