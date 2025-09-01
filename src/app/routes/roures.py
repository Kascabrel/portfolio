from flask import redirect, url_for, render_template, request, flash, session
from flask import Blueprint

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/', methods=['GET'])
def index():
    return redirect(url_for('portfolio.home'))


@portfolio.route('/home')
def home():
    return render_template('index.html', current_page='home')


@portfolio.route('/about')
def about():
    return render_template("about.html", current_page='about')


@portfolio.route('/projects')
def projects():
    return render_template("project.html", current_page='projects')


@portfolio.route('/skills')
def skills():
    return render_template("skills.html", current_page='skills')


@portfolio.route('/experience')
def experience():
    return render_template("experience.html", current_page='experience')


@portfolio.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # send an email or store the message into the database
        print(f"New message from {name} ({email}): {message}")

        flash("Thank you for your message! I will get back to you soon.", "success")
        session['current_page'] = 'contacts'
        return redirect(url_for("portfolio.contact"))

    return render_template("contact.html", current_page="contact ")
