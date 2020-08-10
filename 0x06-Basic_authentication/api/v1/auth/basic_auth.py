#!/usr/bin/env python3
"""
Auth module for the API
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Returns the decoded value of a Base64
            string base64_authorization_header
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) is not str:
            return None

        try:
            base64_authorization_header = base64.b64decode(
                                            base64_authorization_header
                                          )
        except binascii.Error:
            return None

        return base64_authorization_header.decode('utf-8')

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or \
           type(decoded_base64_authorization_header) is not str or \
           ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            user_credentials = decoded_base64_authorization_header.split(':')
            return user_credentials[0], user_credentials[1]
