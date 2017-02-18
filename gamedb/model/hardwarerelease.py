from gamedb import db


class HardwareRelease(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    hardware_id = db.Column(db.Integer, db.ForeignKey("hardware.id"))
    release_id = db.Column(db.Integer, db.ForeignKey("release.id"))
