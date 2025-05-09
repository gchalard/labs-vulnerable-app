from flask import Blueprint, request, jsonify
from app.models import Blog
from app.extensions import db
from app.utils.keycloak import authenticate
from app.utils.db import get_author

blog_bp = Blueprint('blog', __name__)

def author_getter(blog_id: int): 
    return Blog.query.filter_by(id=blog_id).first().author_id

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
    
@blog_bp.route('/', methods=['POST'])
@authenticate(roles=["admin", "user"])
def create_blog():
    data = request.get_json()
    blog = Blog(**data)
    db.session.add(blog)
    db.session.commit()
    
    return jsonify(
        {
            "id": blog.id,
            "title": blog.title,
            "author": get_author(blog.author_id)
        }
    ), 201
    
@blog_bp.route('/<int:blog_id>', methods=['GET'])
def get_blog(blog_id: int):
    blog = Blog.query.filter_by(id=blog_id).first()
    if not blog:
        return jsonify({"message": "Blog not found"}, 404)
    
    return jsonify(
        {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "author": get_author(blog.author_id)
        }
    ), 200
    
@blog_bp.route('/<int:blog_id>', methods=['DELETE'])
@authenticate(roles=["admin"], author_getter=get_author)
def delete_blog(blog_id: int):
    blog = Blog.query.filter_by(id=blog_id).first()
    db.session.delete(blog)
    db.session.commit()
    
    return jsonify(
        {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "author": get_author(blog.author_id)
        }
    ),  200
    
@blog_bp.route('/<int:blog_id>', methods=['PUT'])
@authenticate(roles=["admin"], author_getter=author_getter)
def update_blog(blog_id: int):
    data = request.get_json()
    blog = Blog.query.filter_by(id=blog_id).first()
    blog.title = data["title"]
    blog.content = data["content"]
    db.session.commit()
    
    return jsonify(
        {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "author": get_author(blog.author_id)
        }
    ), 200