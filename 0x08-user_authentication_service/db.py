#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str):
        """ Add user to DB
        """
        from user import User

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user, _warn=False)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs: dict):
        """ 2. Find user by
        """
        from user import User
        from sqlalchemy.orm.exc import NoResultFound

        results = self._session.query(User).filter_by(**kwargs)

        return results.one()
