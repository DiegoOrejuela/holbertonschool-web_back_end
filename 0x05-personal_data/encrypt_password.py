#!/usr/bin/env python3
"""
5. Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ function that expects one string argument and returns
    a salted, hashed password, which is a byte string"""
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())
