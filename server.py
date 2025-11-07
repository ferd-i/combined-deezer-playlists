#!/usr/bin/env python3
from flask import Flask, send_from_directory, jsonify, request
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
        
        response = requests.get(url, params=params, timeout=10)
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
