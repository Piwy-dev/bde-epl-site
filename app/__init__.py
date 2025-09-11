import os
from .config import DevelopmentConfig, ProductionConfig
from flask import Flask, render_template, g, current_app, redirect, request

def create_app(test_config=None):
    """
    Create and configure the app.
    """
    app = Flask(__name__, instance_relative_config=True)
    
    config_name = os.environ.get('APP_CONFIG', 'development')
    if config_name == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

   # create the pages
    @app.route("/")
    def index():
        print(request.accept_languages)
        return redirect('/home')
    
    @app.route("/home")
    def home():
        return render_template('/home.html')
    
    @app.route("/members")
    def members():
        return render_template('/members.html')
    
    @app.route("/Contact")
    def contact():
        return render_template('/contact.html')

    return app
