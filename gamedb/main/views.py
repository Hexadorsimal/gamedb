from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..model import User


@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            session['known'] = True
        else:
            session['known'] = False
            user = User(name=form.name.data)
            db.session.add(user)
            db.session.commit()

        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for(".index"))
    else:
        return render_template("index.html",
                               form=form,
                               name=session.get("name"),
                               known=session.get("known"),
                               current_time=datetime.utcnow())


@main.route("/users/<name>")
def user(name):
    return render_template("user.html", name=name)
