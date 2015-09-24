from zoo.core import db


class JsonSerializer(object):

    __json_hidden__ = None
    __json_public__ = None
    # SQLAlchemy specific. Probably belongs elsewhere.
    __orm_props__ = {'query', 'metadata'}

    def to_json(self):
        """Returns a dict of serializable JSON properties."""
        public = self.json_public()
        hidden = self.json_hidden()
        rv = {k: getattr(self, k) for k in public
              if k not in hidden and k not in self.__orm_props__}
        print(rv)
        return rv

    def json_public(self):
        """JSON serializable properties."""
        if self.__json_public__:
            return self.__json_public__
        props = {p.key for p in self.__mapper__.iterate_properties}
        props = set()
        for k in dir(self):
            if k.startswith('_') or hasattr(getattr(self, k), '__call__'):
                continue
            props.add(k)
        return props


    def json_hidden(self):
        """Properties hidden for JSON serialization."""
        return self.__json_public__ or {}


class BaseModel(db.Model, JsonSerializer):
    """Base SQLAlchemy model."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())


class BaseService(object):

    def __init__(self, actor=None):
        self.actor = actor

    def assert_authorized(self):
        assert self.actor is not None, 'Not logged in.'
