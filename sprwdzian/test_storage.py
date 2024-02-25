import pytest
from app.storage import add_user, get_user, update_user, delete_user, get_all_users
from app.models import User

def test_add_user():
    user = User(1, "John", "Doe",  1990, "user")
    add_user(user)
    assert get_user(1) == user

def test_update_user():
    user = User(1, "John", "Doe",  1990, "user")
    add_user(user)
    user.first_name = "Jane"
    update_user(1, user)
    assert get_user(1).first_name == "Jane"

def test_delete_user():
    user = User(1, "John", "Doe",  1990, "user")
    add_user(user)
    delete_user(1)
    assert get_user(1) is None
