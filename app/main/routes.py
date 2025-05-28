from flask import render_template
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title='Home')

@bp.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html", title='About')
