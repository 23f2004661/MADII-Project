from flask import Flask
from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import User
from application.security import jwt
from flask_cors import CORS

def create_app():
    app=Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    CORS(app)
    jwt.init_app(app)
    app.app_context().push()
    return app


app=create_app()

from application.controllers import *

if __name__ == '__main__':
    # db.create_all()
    # admin=User(username='admin',password='1939',pincode='0000',fullname='Administrator',role='admin')
    # user=User(username='Tarang1712',password='1939',pincode='223355',fullname='Tarang j')
    # db.session.add_all([admin,user])
    # db.session.commit()
    app.run()