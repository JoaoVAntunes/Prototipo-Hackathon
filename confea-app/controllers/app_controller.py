from flask import Flask, redirect, render_template, request
import requests

# Importação dos BLUEPRINTS

def create_app():
    app = Flask(__name__,
        template_folder="./views/",
        static_folder="./static/",
        root_path="./")

# Blueprints --------------------------------------------------------------------------------------

    @app.route('/')
    def index():

        url = "https://hackathon.teste.confea.org.br/Profissionais/2022483600"

        data = requests.get(url=url)

        data = data.json()
        print(data)

        return render_template("index.html")

    return app
