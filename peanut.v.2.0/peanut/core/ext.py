from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
api = Api()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()
bootstrap = Bootstrap()
