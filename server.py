#!/usr/bin/env python3
from flask import Flask, send_from_directory, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

DEEZER_API_BASE = "https://api.deezer.com"

@app.route('/')
def index():
    response = send_from_directory('.', 'index.html')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/api/deezer/<path:endpoint>')
def proxy_deezer(endpoint):
    try:
        url = f"{DEEZER_API_BASE}/{endpoint}"
        params = request.args.to_dict()
        
        response = requests.get(url, params=params, timeout=120)
        
        return Response(
            response.content,
            status=response.status_code,
            headers={'Content-Type': 'application/json'}
        )
    except Exception as e:
        return Response(
            f'{{"error": "{str(e)}"}}',
            status=500,
            headers={'Content-Type': 'application/json'}
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
