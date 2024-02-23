
from flask import Flask, request, jsonify
from user_service import UserService, UserNotFoundException

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(user), 200
    except UserNotFoundException:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    new_user = user_service.create_user(user_data)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.json
    try:
        updated_user = user_service.update_user(user_id, user_data)
        return jsonify(updated_user), 200
    except UserNotFoundException:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return '', 204
    except UserNotFoundException:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
