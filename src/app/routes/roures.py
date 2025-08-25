from flask import redirect, url_for, render_template, request, flash
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
    return redirect( url_for("portfolio.home") + "#about")


@portfolio.route('/projects')
def projects():
    return render_template("project.html")


@portfolio.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Ici tu peux envoyer un email ou stocker le message en DB
        print(f"New message from {name} ({email}): {message}")

        flash("Thank you for your message! I will get back to you soon.", "success")
        return redirect(url_for("portfolio.contact"))

    return render_template("contact.html")


@portfolio.route('/skills')
def skills():
    return render_template("skills.html")


@portfolio.route('/experience')
def experience():
    return render_template("experience.html")
