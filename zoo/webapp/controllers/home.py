import flask as f

from ..helpers import render

bp = f.Blueprint('home', __name__, url_prefix='/')


@bp.route('')
def index():
    return render('home/index.html', {'ip': f.request.remote_addr})
