import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
