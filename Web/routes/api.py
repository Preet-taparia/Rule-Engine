from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

@api.route('/logs', methods=['POST'])
def receive_logs():
    log_data = request.json
    print("Received log:", log_data)
    return jsonify({"message": "Log received"}), 200

@api.route('/rules', methods=['GET'])
def get_rules():
    # Mock data for rules
    security_rules = [
        {"id": 1, "description": "Block traffic from suspicious IPs", "status": "active"},
        # Add more rules as needed
    ]
    return jsonify(security_rules), 200
