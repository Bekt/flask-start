import flask as f


class MFlask(f.Flask):
    """Custom Flask application."""

    def make_response(self, obj):
        """Return a JSON response if `obj` has a `to_json` method.

        See: `flask.Flask`.
        """
        if hasattr(obj, 'to_json') and hasattr(obj.to_json, '__call__'):
            return f.jsonify(data=obj)
        return f.Flask.make_response(self, obj)


class MRequest(f.Request):
    """Custom request object that extends the default Flask request.

    See: `flask.Request`.
    """

    @property
    def is_json(self):
        """See `Request.is_json` in Flask 1.0."""
        mt = self.mimetype
        if mt == 'application/json':
            return True
        if mt.startswith('application/') and mt.endswith('+json'):
            return True
        return False
