from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell

from gamedb import app, db
from gamedb.model import Role, User


def _make_context():
    return dict(app=app, db=db, User=User, Role=Role)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=2600))
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
