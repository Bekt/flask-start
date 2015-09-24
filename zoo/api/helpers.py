import flask_login


def service_factory(cls, *args, **kwargs):
    """Factory for creating a backend service instance with current user."""
    return cls(*args, actor=flask_login.current_user, **kwargs)
