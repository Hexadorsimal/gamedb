from gamedb import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String(), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role")

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User {user}>".format(user=self.username)
