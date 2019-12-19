from flask import Blueprint,render_template
bp = Blueprint('peanut',__name__)

@bp.route('/')
def homepage():
    return render_template('home_page.html')


@bp.route('/pageinfo')
def pageinfo():
    return render_template('home_page.html')