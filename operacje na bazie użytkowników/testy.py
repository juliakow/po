import unittest
from app import app, find_user_by_id, get_next_user_id, create_user, update_user, create_or_update_user, delete_user

class YourAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.users = []

    def test_find_user_by_id(self):
        user1 = {"id": 1, "name": "John", "lastname": "Doe"}
        user2 = {"id": 2, "name": "Jane", "lastname": "Smith"}
        self.users = [user1, user2]


        found_user = find_user_by_id(1)
        self.assertEqual(found_user, user1)


        non_existent_user = find_user_by_id(3)
        self.assertIsNone(non_existent_user)

    def test_get_next_user_id(self):
        
        next_id_empty_list = get_next_user_id()
        self.assertEqual(next_id_empty_list, 1)

        
        user1 = {"id": 1, "name": "John", "lastname": "Doe"}
        user2 = {"id": 2, "name": "Jane", "lastname": "Smith"}
        self.users = [user1, user2]

       
        next_id_non_empty_list = get_next_user_id()
        self.assertEqual(next_id_non_empty_list, 3)

    def test_create_user(self):
      
        response = self.app.post('/users', json={"name": "Alice", "lastname": "Johnson"})

       
        self.assertEqual(response.status_code, 201)

        
        created_user_id = response.json['id']
        created_user = find_user_by_id(created_user_id)
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user['name'], "Alice")
        self.assertEqual(created_user['lastname'], "Johnson")

    def test_update_user(self):
       
        user = {"id": 1, "name": "John", "lastname": "Doe"}
        self.users = [user]

        
        response = self.app.patch('/users/1', json={"name": "UpdatedName"})

        self.assertEqual(response.status_code, 204)

      
        updated_user = find_user_by_id(1)
        self.assertEqual(updated_user['name'], "UpdatedName")

    def test_create_or_update_user(self):
        
        response = self.app.put('/users/1', json={"name": "Bob", "lastname": "Smith"})

        
        self.assertEqual(response.status_code, 204)

       
        created_or_updated_user = find_user_by_id(1)
        self.assertIsNotNone(created_or_updated_user)
        self.assertEqual(created_or_updated_user['name'], "Bob")
        self.assertEqual(created_or_updated_user['lastname'], "Smith")

    def test_delete_user(self):
        
        user = {"id": 1, "name": "John", "lastname": "Doe"}
        self.users = [user]

       
        response = self.app.delete('/users/1')

        
        self.assertEqual(response.status_code, 204)

        
        deleted_user = find_user_by_id(1)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
