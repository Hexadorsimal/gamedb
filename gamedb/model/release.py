from gamedb import db


class Release(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    name = db.Column(db.String)

    territory_id = db.Column(db.Integer, db.ForeignKey("territory.id"))
    territory = db.relationship("Territory")

    publisher_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    publisher = db.relationship("Company")

    date = db.Column(db.Date())

    def __repr__(self):
        return "<Release {date}>".format(date=self.date)
