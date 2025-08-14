# src/app/__init__.py
import os
from dotenv import load_dotenv
from flask import Flask
from config import DevConfig, ProdConfig, TestConfig

# Création de l'app
app = Flask(__name__)

# Chargement des configs
load_dotenv()
env = os.getenv("FLASK_ENV")
if env == "development":
    app.config.from_object(DevConfig)
elif env == "production":
    app.config.from_object(ProdConfig)
elif env == "test":
    app.config.from_object(TestConfig)

# Import du Blueprint après la création de l'app
from src.app.routes.roures import portfolio
app.register_blueprint(portfolio)
