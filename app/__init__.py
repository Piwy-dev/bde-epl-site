import os
from flask import Flask, render_template, g, current_app, redirect, request

def create_app(test_config=None):
    """
    Create and configure the app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

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
    
    @app.route("/membres")
    def membres():
        return render_template('/membres.html')
    
    @app.route("/privacy")
    def privacy():
        return render_template('/privacy.html')
    
    @app.route("/terms")
    def terms():
        return render_template('/terms.html')
    
    @app.route("/suppression-request")
    def suppression_request():
        return render_template('/suppression-request.html')

    return app
