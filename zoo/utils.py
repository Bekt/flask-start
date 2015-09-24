from datetime import datetime
from flask.json import JSONEncoder


class JsonEncoder(JSONEncoder):
    """Custom JSON encoder for types that aren't handled by default.

    See: `flask.json.JsonEncoder`.
    """

    def default(self, obj):
        if hasattr(obj, 'to_json') and hasattr(obj.to_json, '__call__'):
            return obj.to_json()
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, int) and obj >= (1 << 31):
            return str(obj)
        return JSONEncoder.default(self, obj)
