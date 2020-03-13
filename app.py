from flask import Flask,jsonify,request
from flask_dotenv import DotEnv
from controllers.dashboard import blueprint as dashboard_blueprint
from extentions.extentions import db,migrate
from config import Config
app = Flask(__name__)

def create_app(config_class=Config):
    app.config.from_object(config_class)
    # configure_config(app)
    configure_blueprints(app)
    configure_db(app)
    print(app.config.get("SQLALCHEMY_DATABASE_URI"))
    return app


def configure_blueprints(app):
    app.register_blueprint(dashboard_blueprint)

    return None

def configure_db(app):
    db.init_app(app)
    migrate.init_app(app,db)
    
# def configure_config(app):
#     # app.config.from_object(config_class)
#     env = DotEnv()
#     from helpers.path_helpers import config_path
#     config_path=config_path(app)
#     print(config_path)
#     env.init_app(app,env_file=config_path,verbose_mode=True)
#     return None
import models
create_app()

if __name__ == '__main__':
    app.run(debug=app.config.get("APP_DEBUG", True))