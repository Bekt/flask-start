"""Main WSGI module.

To run:
   python runserver.py
-or-
   gunicorn runserver:app -b 0.0.0.0:5000
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from zoo import (webapp, api)

DEBUG = True

www_app = webapp.create_app(debug=DEBUG)
api_app = api.create_app(debug=DEBUG)

# Combine multiple applications.
app = DispatcherMiddleware(www_app, {
    '/api/v0': api_app
})

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app,
               use_reloader=True, use_debugger=DEBUG)
