from flask import Flask,render_template,request,url_for,redirect,session,escape
from flask_bootstrap import Bootstrap
import blueprint_peanut
import peanut_form

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(blueprint_peanut.bp)
app.secret_key = 'dfddddafdfasfasdfs'

#404处理
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

#500处理
@app.errorhandler(500)
def servererror(e):
    return render_template('500.html'),500

 
@app.route('/',methods=['GET','POST'])
def homepage():
    form = peanut_form.MyFrom()
    if request.method == "GET":
        # todo   basedate
        return render_template('home_page.html')
    else:
        if form.validate_on_submit():
            url_args = request.form['title']
            print('url_args------>',url_args)
            return redirect(url_for('pageinfo_',name=url_args))
            # return render_template('home_info.html',url_args = url_args,form=form)




@app.route('/pageinfo/<name>',methods=["GET","POST"])
def pageinfo_(name):
    # todo   basedate
    return render_template('home_info.html',name=name)
#



@app.route('/terrace/<name>')
def wawj(name):
        #todo
    return render_template('terraces.html')


@app.route('/region/<name>')
def regions(name):
    # todo
    return render_template('regions_info.html',name=name)


@app.route('/houseinfo/<name>')
def houseinfo(name):
    #todo
    return render_template('house_info.html')




if __name__ == '__main__':
    app.run(debug=True)
