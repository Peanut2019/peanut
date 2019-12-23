from flask import Blueprint,render_template
import peanut_form
bp = Blueprint('peanut',__name__)

@bp.route('/')
def homepage():
    form = peanut_form.MyFrom()
    return render_template('home_page.html',form = form)


@bp.route('/pageinfo')
def pageinfo():
    return render_template('home_page.html')