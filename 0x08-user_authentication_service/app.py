#!/usr/bin/env python3
"""
App module
"""
from flask import Flask, escape, request, jsonify
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
