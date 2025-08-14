from flask import redirect, url_for
from flask import Blueprint

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/', methods=['GET'])
def index():
    return redirect(url_for('portfolio.home'))


@portfolio.route('/home')
def home():
    # return render_template(welcome.html)
    return "home"


@portfolio.route('/about')
def about():
    return "about"


@portfolio.route('/project')
def project():
    return "project"
