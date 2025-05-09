from flask import Blueprint, request, jsonify
from app.models import Blog
from app.extensions import db
from app.utils.keycloak import authenticate
from app.utils.db import get_author

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/', methods=['GET'])
def get_blogs():
    blogs = Blog.query.with_entities(Blog.id, Blog.title, Blog.author_id).all()
    
    return jsonify(
        [
            {
                "id": blog.id,
                "title": blog.title,
                "author": get_author(blog.author_id)
            } for blog in blogs
        ]
    )