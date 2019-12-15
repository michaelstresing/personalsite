from flask import Flask
from .config import ProductionConfig, DevelopmentConfig

app = Flask(__name__, instance_relative_config=False)

def create_app():

    # Construct the core application.
    app.config.from_object(ProductionConfig)
    
    with app.app_context():

        # Imports
        from . import routes
        
        return app