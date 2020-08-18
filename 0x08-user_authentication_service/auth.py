#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> str:
    """
    4. Hash password
    """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """ return a string representation of a new UUID
    """
    return str(uuid.uuid4())


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
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ Valid login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(bytes(password, "ascii"),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ The method should find the user corresponding to the email,
            generate a new UUID and store it in the database as the user’s
            session_id, then return the session ID.
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ It takes a single session_id string argument and returns a string
        or None. If the session ID is None or no user is found, return None.
        Otherwise return the corresponding user.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
