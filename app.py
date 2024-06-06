# app.py

from flask import Flask, render_template
import requests
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# app.py

#import requests

@app.route('/api/live-scores')
def get_live_scores():
    response = requests.get('https://api.soccer.com/live-scores')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch live scores'}, 500

# app.py

#from flask import request

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

