from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from project import app, db

app.config.from_object("config.BaseConfig")

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()


# python manage.py db init  -- init transitions
# python manage.py db migrate -- luo scriptan uusimpaan muutokseen
# python manage.py db upgrade / downgrade -- downgrade tiputtaa askeleen, upgrade nostaa uusimpaan