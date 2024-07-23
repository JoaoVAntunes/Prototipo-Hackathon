from flask import Blueprint, Flask, render_template, request, redirect, url_for
import requests
from models.db import db, instance

from models.profissional.profissional import Professional

# Importação dos BLUEPRINTS
from controllers.auth_controller import auth
from controllers.prof_controller import prof


def create_app():
    app = Flask(__name__,
        template_folder="./views/",
        static_folder="./static/",
        root_path="./")
    
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    # Blueprints --------------------------------------------------------------------------------------
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(prof, url_prefix='/')

    @app.route('/')
    def index():
        
        url = "https://hackathon.teste.confea.org.br/Profissionais/2022483600"

        data = requests.get(url=url)

        data = data.json()
        print(data) 

        professional = Professional.query.all()
        return render_template('index.html', professional=professional)


    return app


