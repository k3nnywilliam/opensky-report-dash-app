import os

# Dash app configuration settings
class Config:
    DEBUG = False  # Set to True for development, False for production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    # Database configuration if your app uses a database
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'

    # Other settings specific to your app
    # ...
