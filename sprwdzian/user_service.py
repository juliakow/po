
class UserService:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self):
        return self.users

    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        raise UserNotFoundException()

    def create_user(self, user_data):
        user = {
            'id': self.next_id,
            'firstName': user_data['firstName'],
            'lastName': user_data['lastName'],
            'age': 2024 - user_data['birthYear'],  
            'group': user_data['group']
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def update_user(self, user_id, user_data):
        for user in self.users:
            if user['id'] == user_id:
                user.update(user_data)
                user['age'] = 2024 - user['birthYear']
                return user
        raise UserNotFoundException()

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user['id'] == user_id:
                del self.users[i]
                return
        raise UserNotFoundException()

class UserNotFoundException(Exception):
    pass
