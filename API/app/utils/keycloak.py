from functools import wraps
from flask import request, jsonify
import jwt

def authenticate(roles=[]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if auth_header:
                token = auth_header.split(" ")[1]
                decoded_token = jwt.decode(token, options={"verify_signature": False})
                print(decoded_token)
                if not any(role in decoded_token['realm_access']['roles'] for role in roles):
                    return jsonify(
                        {
                            "message": "Unauthorized"
                        }
                    ), 401
                
                return f(*args, **kwargs)
        return decorated_function
    return decorator