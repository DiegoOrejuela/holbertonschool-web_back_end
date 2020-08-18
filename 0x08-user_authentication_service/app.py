#!/usr/bin/env python3
"""
App module
"""
from flask import Flask, escape, request, jsonify, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome() -> str:
    """ Welcome
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ Register user
    """

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def log_in() -> str:
    """ Log in
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ Log out
    """
    session_id = request.cookies.get('session_id')

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("http://0.0.0.0:5000/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
