import requests
import jwt
import json

token_url = 'http://localhost:8080/realms/vuln-app/protocol/openid-connect/token'
data = {
    'client_id': 'vuln-app',
    'client_secret': '8kaE62lq3pxjmRYULuBVBiDfrLva6tGP',
    'username': 'user',
    'password': 'password',
    'grant_type': 'password'
}

response = requests.post(token_url, data=data)
# print(response.json())
token = response.json().get('access_token')
print(token)

decoded_token = jwt.decode(token, algorithms=['HS256', 'RS256'], options={"verify_signature": False})
print(json.dumps(decoded_token, indent=4))
