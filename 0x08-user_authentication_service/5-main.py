#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User
from auth import _hash_password, Auth

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()
auth = Auth()

email = 'test@test.com'
hashed_password = "hashedPwd"

try:
    auth.register_user(email=email, password=hashed_password)
    print(my_db.find_user_by(email=email))
    print("User registered")
except ValueError:
    print("Error")

try:
    auth.register_user(email=email, password=hashed_password)
    print("User registered")
except ValueError:
    print("Error")