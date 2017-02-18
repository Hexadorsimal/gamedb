from gamedb import db


class Release(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    territory_id = db.Column(db.Integer, db.ForeignKey("territory.id"))
    territory = db.relationship("Territory")

    date = db.Column(db.Date())

    def __repr__(self):
        return "<Release {date}>".format(date=self.date)
