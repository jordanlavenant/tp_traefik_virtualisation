import time
import redis
import json

from flask import Flask, request, Response, jsonify

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/kv/<string:i>/<string:k>', defaults={'v': None}, methods=['POST', 'GET', 'DELETE', 'PUT'])
@app.route('/kv/<string:i>/<string:k>/<string:v>', methods=['POST', 'PUT'])
def kv(i: str, k: str, v: str):
    """
    Key-Value Store avec Redis
    """
    status = 200
    method = request.method

    if v is None and method in ['POST', 'PUT']:
        return jsonify({'id': i, 'error': 'value parameter is required', 'method': method}), 400

    if v is not None and method in ['GET', 'DELETE']:
        return jsonify({'id': i, 'error': 'value parameter does not apply', 'method': method}), 400

    if method == 'GET':
        value = redis_client.get(k)
        if value is None:
            status = 404
        response = {'request_id': i, 'request_key': k, 'response_value': value, 'method': method}

    elif method in ['POST', 'PUT']:
        redis_client.set(k, v)
        response = {'request_id': i, 'request_key': k, 'request_value': v, 'method': method}

    elif method == 'DELETE':
        redis_client.delete(k)
        response = {'request_id': i, 'request_key': k, 'deleted': True, 'method': method}

    return jsonify(response), status


if __name__ == '__main__':
    while True:
        try:
            if redis_client.ping():
                break
        except redis.ConnectionError:
            time.sleep(5)

    app.run(debug=True, host="0.0.0.0", port=80)
