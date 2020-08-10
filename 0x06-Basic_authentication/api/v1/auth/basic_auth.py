#!/usr/bin/env python3
"""
Auth module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header for a
            Basic Authentication
        """
        if authorization_header is None or \
           type(authorization_header) is not str or \
           authorization_header[:6] != 'Basic ':
            return None
        else:
            return authorization_header[6:]
