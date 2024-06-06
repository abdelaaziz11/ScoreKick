# app.py

import requests
from app import app

@app.route('/api/live-scores')
def get_live_scores():
    response = requests.get('https://api.soccer.com/live-scores')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch live scores'}, 500
