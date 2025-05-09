from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "postgresql://user:password@localhost:5432/db")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    
    TABLES = [
        {
            "name": "blog",
            "columns": [
                {"name": "id", "type": "serial", "constraints": "primary key"},
                {"name": "title", "type": "varchar(100)", "constraints": "not null"},
                {"name": "content", "type": "text", "constraints": "not null"},
                {"name": "author_id", "type": "varchar(36)", "constraints": "REFERENCES user_entity(id)"}
            ]
        },
        {
            "name": "comment",
            "columns": [
                {"name": "id", "type": "serial", "constraints": "primary key"},
                {"name": "content", "type": "text", "constraints": "not null"},
                {"name": "blog_id", "type": "int", "constraints": "not null"},
                {"name": "author_id", "type": "varchar(36)", "constraints": "REFERENCES user_entity(id)"}
            ]
        }
    ]
    

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLES = [
        {
            "name": "user_entity",
            "columns": [
                {"name": "id", "type": "varchar(36)", "constraints": "primary key"},
                {"name": "name", "type": "varchar(255)", "constraints": "not null"},
                {"name": "value", "type": "varchar(255)"},
                {"name": "user_id", "type": "varchar(36)", "constraints": "not null"},
                {"name": "long_value_hash", "type": "bytea"},
                {"name": "long_value_hash_lower_case", "type": "bytea"},
                {"name": "long_value", "type": "text"}
            ]
        },
        {
            "name": "blog",
            "columns": [
                {"name": "id", "type": "serial", "constraints": "primary key"},
                {"name": "title", "type": "varchar(100)", "constraints": "not null"},
                {"name": "content", "type": "text", "constraints": "not null"},
                {"name": "author_id", "type": "varchar(36)", "constraints": "REFERENCES user_entity(id)"}
            ]
        }
    ]