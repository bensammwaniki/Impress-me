from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    # inititalizing application
    app = Flask(__name__)

 
    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)


    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app