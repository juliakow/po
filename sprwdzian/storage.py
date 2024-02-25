from app.models import User

users = {}

def add_user(user):
    users[user.id] = user

def get_user(user_id):
    return users.get(user_id)

def update_user(user_id, user):
    if user_id in users:
        users[user_id] = user
        return True
    return False

def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return True
    return False

def get_all_users():
    return list(users.values())
