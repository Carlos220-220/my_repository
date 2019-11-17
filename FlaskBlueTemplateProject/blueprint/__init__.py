import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from blueprint.course import course
# from blueprint.user import user
#
# base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#
#
# app = Flask(__name__)
#
# app.config.from_object("settings.DebugConfig")
#
# db = SQLAlchemy(app)
#
# app.register_blueprint(course, url_prefix="/course/")
# app.register_blueprint(user, url_prefix="/user/")
#



# app惰性加载

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DebugConfig")

    db.init_app(app)

    from blueprint.course import course
    from blueprint.user import user
    app.register_blueprint(course, url_prefix="/course/")
    app.register_blueprint(user, url_prefix="/user/")

    return app