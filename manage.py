#!/usr/bin/env python
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell

from gamedb import create_app, db
from gamedb.model import Role, User


app = create_app(os.getenv("FLASK_CONFIG") or "default")


def _make_context():
    return dict(app=app, db=db, User=User, Role=Role)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=2600))
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()
