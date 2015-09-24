import flask as f

from zoo import factory
from . import users


def create_app():
    """Creates an API application."""
    app = factory.flask_app(__name__)

    for bp in [users.bp, ]:
        app.register_blueprint(bp)

    app.before_request(attach_before_request(app))
    app.errorhandler(Exception)(attach_errorhandler)
    return app


def attach_before_request(app):
    def before_request(*args, **kwargs):
        """Asserts the request is a JSON request."""
        if f.request.method in ('POST', 'PUT') and not f.request.is_json:
            f.abort(405, description='Please send a JSON request.')
    return before_request


def attach_errorhandler(error, _type=None):
    return f.jsonify(
        status_code=error.code,
        message=error.description,
        details=str(error),
        _type=(_type or error.__class__.name)
    ), error.code
