"""Core module.

Common "global" instances are defined here.
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# No app instance passed!
db = SQLAlchemy()

login = LoginManager()

