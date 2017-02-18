from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://gamer:password@localhost/gamedb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "hard to guess string"

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


import gamedb.views
import gamedb.hello
import gamedb.model.company
import gamedb.model.hardware
import gamedb.model.location
import gamedb.model.role
import gamedb.model.software
import gamedb.model.user
