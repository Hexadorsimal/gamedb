from flask import render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from gamedb import app, db
from gamedb.model import User


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
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
        return redirect(url_for("index"))
    else:
        return render_template("index.html", form=form, name=session.get("name"), known=session.get("known"))
