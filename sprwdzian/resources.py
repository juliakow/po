from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from app.models import User
from app.storage import add_user, get_user, update_user, delete_user, get_all_users

app = Flask(__name__)
api = Api(app)

class UserList(Resource):
    def get(self):
        return jsonify([user.__dict__ for user in get_all_users()])

    def post(self):
        data = request.get_json()
        user = User(data['id'], data['firstName'], data['lastName'], data['birthYear'], data['group'])
        add_user(user)
        return jsonify(user.__dict__),  201

class UserItem(Resource):
    def get(self, user_id):
        user = get_user(user_id)
        if user:
            return jsonify(user.__dict__)
        return jsonify({"error": "User not found"}),  404

    def patch(self, user_id):
        data = request.get_json()
        user = get_user(user_id)
        if user:
            user.first_name = data.get('firstName', user.first_name)
            user.last_name = data.get('lastName', user.last_name)
            user.birth_year = data.get('birthYear', user.birth_year)
            user.group = data.get('group', user.group)
            update_user(user_id, user)
            return jsonify(user.__dict__)
        return jsonify({"error": "User not found"}),  404

    def delete(self, user_id):
        if delete_user(user_id):
            return jsonify({"message": "User deleted"}),  200
        return jsonify({"error": "User not found"}),  404

api.add_resource(UserList, '/users')
api.add_resource(UserItem, '/users/<int:user_id>')
