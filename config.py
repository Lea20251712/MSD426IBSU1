import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///warrigal_park.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False