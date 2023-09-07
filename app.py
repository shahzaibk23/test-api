from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/api/response', methods=['POST'])
def get_response():
    response = ["success", "failed"]
    return jsonify({"status": random.choice(response)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
