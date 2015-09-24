"""Manager module via Flask-Script.

To run: python manage.py [<command>, shell, runserver]
"""

from flask_script import Manager

from zoo import webapp
from zoo.core import db


manager = Manager(webapp.create_app())


@manager.command
def hello():
    print('Hello.')


@manager.command
def create_db():
    """Creates all defined ORM tables."""
    db.create_all()


@manager.command
def seed():
    """Seeds the database."""
    pass

if __name__ == '__main__':
    manager.run()
