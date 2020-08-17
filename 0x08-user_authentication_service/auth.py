#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from user import User
from db import DB


def _hash_password(password: str) -> str:
    """
    4. Hash password
    """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Init
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user
        """
        results = self._db._session.query(User).filter_by(email=email)

        if results.count() > 0:
            raise ValueError("User {} already exists".format(email))

        hashed_password = _hash_password(password)
        user = self._db.add_user(email=email, hashed_password=hashed_password)

        return user
