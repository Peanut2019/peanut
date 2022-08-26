from flask import Flask
from flask import render_template
from peanut.core.ext import bootstrap, db, api, migrate, jwt, cors


# template_folder改为本地templates所在文件位置
# app = Flask(__name__, template_folder=r'D:\PycharmProjects\Peanut\peanut\peanut.v.2.0\peanut\templates')
# bootstrap = Bootstrap(app)
#
# app.secret_key = 'dfddddafdfasfasdfs'


class BuildApp:

    def __init__(self):
        self.app = Flask(__name__)

    def load_config(self):
        self.app.config.from_object()

    def load_ext(self):
        db.init_app(self.app)
        api.init_app(self.app)
        migrate.init_app(self.app)
        jwt.init_app(self.app)
        cors.init_app(self.app)
        bootstrap.init_app(self.app)

    def register_exception_handler(self):
        @self.app.errorhandler(404)
        def handle_bad_request(error):
            return render_template('404.html'), 404

        @self.app.errorhandler(500)
        def handle_integrity_error(error):
            return render_template('500.html'), 500

    def get_app(self):
        return self.app
