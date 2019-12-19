from flask import Flask,render_template,request,url_for,redirect
import blueprint_peanut
import peanut_form

app = Flask(__name__)
# app.register_blueprint(blueprint_peanut.bp)

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method == "GET":
        return render_template('home_page.html')
    else:
        if request.method == "POST":
            url_args = request.form.get('seel_args')
            # print(url_args)
            return redirect(url_for(pageinfo,name = url_args))




@app.route('/pageinfo/<name>')
def pageinfo(name):
    print(name)
    return render_template('home_page.html')



if __name__ == '__main__':
    app.run()
