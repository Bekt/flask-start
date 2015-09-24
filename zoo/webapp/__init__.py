from zoo import factory

from .controllers import home


def create_app():
    """Creates a new wwww application."""
    app = factory.flask_app(__name__, 'zoo.configs')
    _setup_jinja(app)

    for bp in [home.bp]:
        app.register_blueprint(bp)

    return app


def _setup_jinja(app):
    params = dict(app.jinja_options)
    params.update({
        'trim_blocks': True,
        'lstrip_blocks': True
    })
    app.jinja_options = params
