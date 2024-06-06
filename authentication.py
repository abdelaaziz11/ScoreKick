# app.py

from flask import request
from app import app

# Predefined list of usernames and passwords
USERS = {'user1': 'password1', 'user2': 'password2'}

@app.route('/api/login', methods=['POST'])
def login():
    auth_data = request.json
    username = auth_data.get('username')
    password = auth_data.get('password')
    
    if username in USERS and USERS[username] == password:
        return {'message': 'Login successful'}
    else:
        return {'error': 'Invalid username or password'}, 401
