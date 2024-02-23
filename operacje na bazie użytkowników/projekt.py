from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

def find_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

def get_next_user_id():
    if not users:
        return 1
    return max(user['id'] for user in users) + 1

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'lastname' not in data:
        return jsonify({"error": "Name and lastname are required"}), 400
    
    user_id = get_next_user_id()
    new_user = {"id": user_id, "name": data['name'], "lastname": data['lastname']}
    users.append(new_user)
    
    return jsonify({"id": user_id}), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data or not any(key in data for key in ['name', 'lastname']):
        return jsonify({"error": "Invalid request body"}), 400
    
    if 'name' in data:
        user['name'] = data['name']
    if 'lastname' in data:
        user['lastname'] = data['lastname']
    
    return '', 204

@app.route('/users/<int:user_id>', methods=['PUT'])
def create_or_update_user(user_id):
    user = find_user_by_id(user_id)
    data = request.get_json()
    
    if user:
        user['name'] = data.get('name', user['name'])
        user['lastname'] = data.get('lastname', user['lastname'])
    else:
        new_user = {"id": user_id, "name": data['name'], "lastname": data['lastname']}
        users.append(new_user)
    
    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users.remove(user)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
