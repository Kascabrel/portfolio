import os
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()
if os.getenv("FLASK_ENV") == "development":
    app.config.from_object('DevConfig')
elif os.getenv("FLASK_ENV") == "production":
    app.config.from_object('ProdConfig')
elif os.getenv("FLASK_ENV") == "test":
    app.config.from_object('TestConfig')

