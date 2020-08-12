#!/usr/bin/env python3
""" Module of Session Auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - Dictionary representation of the User authenticated
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user_not_found_error = {"error": "no user found for this email"}
    try:
        users = User.search({'email': email})
    except KeyError:
        return jsonify(user_not_found_error), 404

    if len(users) == 0:
        return jsonify(user_not_found_error), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 404

    # Create session
    from api.v1.app import auth

    session_id = auth.create_session(user_id=user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
