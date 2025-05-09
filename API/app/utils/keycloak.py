from functools import wraps
from flask import request, jsonify
import jwt
from typing import Callable

from app.extensions import db

Resource = db.Model

def authenticate(roles : list = [], author_getter : Callable = None):
    """
    Vulnerable implementation of a Decorator that checks if the user has the specified roles or user_id (author id) 
    to enforce RBAC based on JWT
    
    Args:
        roles (list[str]): A list of roles
        resource_id (int): The id of the resource
        resource (db.Model): The resource
    
    Returns:
        function: The decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if auth_header:
                token = auth_header.split(" ")[1]
                # print(token)
                decoded_token = jwt.decode(token, algorithms=['HS256', 'RS256'], options={"verify_signature": False})
                
                author_id = author_getter(*args, **kwargs) if author_getter else None
                                
                has_role = any(role in decoded_token['realm_access']['roles'] for role in roles)
                is_author = decoded_token['sub'] == author_id
                
                if not (has_role or is_author):
                    return jsonify(
                        {
                            "message": "Unauthorized",
                            "has_role": has_role,
                            "roles": decoded_token['realm_access']['roles'],
                            "is_author": is_author
                        }
                    ), 401
                else:
                    print("Authorized")
                
                return f(*args, **kwargs)
            else:
                print("ERROR: Missing Authorization header")
                return jsonify(
                    {
                        "message": "Missing Authorization header"
                    }
                ), 400
        return decorated_function
    return decorator