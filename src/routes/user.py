from flask import Blueprint, jsonify, request
from models import User

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@bpUser.route('/users/favorites', methods=['GET'])
def all_favorites_of_a_user():
    users = User.query.get(1)
    users = list(map(lambda user: user.favorites(), users))
    return jsonify(users), 200

