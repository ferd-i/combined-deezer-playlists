#!/usr/bin/env python3
import time
from typing import Dict, Tuple

from flask import Flask, send_from_directory, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

DEEZER_API_BASE = "https://api.deezer.com"
CACHE_TTL_SECONDS = 120
_cache: Dict[Tuple[str, Tuple[Tuple[str, str], ...]], Dict[str, object]] = {}
_session = requests.Session()


def _cache_key(
        endpoint: str,
        params: Dict[str, str]) -> Tuple[str, Tuple[Tuple[str, str], ...]]:
    return (endpoint, tuple(sorted(params.items())))


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
        params = request.args.to_dict(flat=True)
        key = _cache_key(endpoint, params)
        now = time.time()

        cached = _cache.get(key)
        if cached and now - cached["ts"] < CACHE_TTL_SECONDS:
            headers = {'Content-Type': 'application/json', 'X-Cache': 'HIT'}
            return Response(cached["content"],
                            status=cached["status"],
                            headers=headers)

        response = _session.get(url, params=params, timeout=30)

        payload = response.content
        _cache[key] = {
            "content": payload,
            "status": response.status_code,
            "ts": now
        }

        return Response(payload,
                        status=response.status_code,
                        headers={
                            'Content-Type': 'application/json',
                            'X-Cache': 'MISS'
                        })
    except Exception as e:
        return Response(f'{{"error": "{str(e)}"}}',
                        status=500,
                        headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
