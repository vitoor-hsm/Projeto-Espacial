from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db.init_app(app)
api = Api(app)
from APP.CONTROLLER.default import MissaoApi
api.add_resource(MissaoApi, "/missoes")

from APP.CONTROLLER import default


