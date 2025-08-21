from flask import redirect, url_for, render_template
from flask import Blueprint

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/', methods=['GET'])
def index():
    return redirect(url_for('portfolio.home'))


@portfolio.route('/home')
def home():
    # return render_template(welcome.html)
    return render_template('index.html')


@portfolio.route('/about')
def about():
    return "about"


@portfolio.route('/project')
def project():
    return "project"
