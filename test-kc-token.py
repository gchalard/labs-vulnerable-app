import requests

token_url = 'http://localhost:8080/realms/vuln-app/protocol/openid-connect/token'
data = {
    'client_id': 'app',
    'client_secret': 'zXs4I2WTgnrxp9LehzOz2hctetImetED',
    'username': 'admin',
    'password': '-etu-',
    'grant_type': 'password'
}

response = requests.post(token_url, data=data)
# print(response.json())
token = response.json().get('access_token')
print(token)
