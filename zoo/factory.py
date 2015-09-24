import flask as f

from .core import db, login
from .wrappers import MFlask, MRequest
from .utils import JsonEncoder


def flask_app(app_name, config_file=None, debug=False):
    """Creates a new bootstrapped Flask application."""
    app = MFlask(app_name)
    if config_file:
        app.config.from_object(config_file)
    app.debug = debug
    app.json_encoder = JsonEncoder
    app.request_class = MRequest
    db.init_app(app)
    login.init_app(app)
    return app
