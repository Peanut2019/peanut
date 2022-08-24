from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'dfddddafdfasfasdfs'


class BuildApp:

    def __init__(self):
        self.app = Flask(__name__)

    # def load_config(self):
    #     self.app.config.from_object()

    def register_exception_handler(self):
        @self.app.errorhandler(404)
        def handle_bad_request(error):
            return render_template('404.html'), 404

        @self.app.errorhandler(500)
        def handle_integrity_error(error):
            return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)