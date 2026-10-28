from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import (
    create_user,
    login,
    get_user_by_id,
    update_user,
    delete_user
)

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users/', methods=['POST'])
def users_post():
    return create_user(request.json)


@user_routes.route('/users/login', methods=['POST'])
def users_login():
    return login(request.json)


@user_routes.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def user_get(user_id):
    return get_user_by_id(user_id)


@user_routes.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def user_put(user_id):
    return update_user(user_id, request.json)


@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def user_delete(user_id):
    return delete_user(user_id)