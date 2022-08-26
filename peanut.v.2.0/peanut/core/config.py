import os


class Config:
    template_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                   'peanut/templates')

    SECRET_KEY = r"\x1c\x15\xe2lT\x1a^DM-B\x9e\xbdIP\x1e\x91\xad\xe8[\x87V(Z"

    DB_CONFIG = {
        'username': 'root',
        'password': 'root',
        'database': 'peanut',
        'port': '3306',
        'datatype': 'mysql+mysqlconnector',
        'host': '127.0.0.1:3306'
    }
    SQLALCHEMY_DATABASE_URI = str(
        DB_CONFIG["datatype"] + '://' + DB_CONFIG['username'] + ':' + DB_CONFIG['password'] + '@' + DB_CONFIG[
            'host'] + '/' + DB_CONFIG['database'])

    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()
