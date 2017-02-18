from gamedb import db


class SoftwareRelease(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    software_id = db.Column(db.Integer, db.ForeignKey("software.id"))
    release_id = db.Column(db.Integer, db.ForeignKey("release.id"))
