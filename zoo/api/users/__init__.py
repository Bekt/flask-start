import flask as f
from flask_login import login_required

from zoo.backend import UserService

from .forms import SignupForm
from ..helpers import service_factory


bp = f.Blueprint('users', __name__, url_prefix='/users/')


@bp.route('me')
def me():
    """."""
    users = service_factory(UserService)
    return users.me()


@bp.route('signup', methods=['POST'])
def signup():
    """"."""
    form = SignupForm()
    if not form.validate_on_submit():
        raise ValueError(form.errors)
    users = service_factory(UserService)
    return users.create(**form.data)
