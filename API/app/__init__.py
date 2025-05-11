from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .config import Config
from app.utils.db import init_db

def create_app(config: Config = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    init_db(db_uri=app.config["SQLALCHEMY_DATABASE_URI"], tables=app.config["TABLES"])
    
    from .routes.blog import blog_bp
    
    app.register_blueprint(blueprint=blog_bp, url_prefix="/api/blogs")
    
    return app