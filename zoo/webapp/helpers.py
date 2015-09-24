import flask as f
import flask_login

def render(template, context={}):
    """Wrapper around `flask.render`.

    Passes flash messages (`flashes`) and current user (`user`)
    onto the template context.
    """
    context['flashes'] = f.get_flashed_messages(with_categories=True)
    context['user'] = flask_login.current_user
    return f.render_template(template, **context)
