from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.formulario_controller import (
    create_formulario,
    get_formulario_by_id,
    update_formulario,
    delete_formulario
)

formulario_routes = Blueprint('formulario_routes', __name__)


@formulario_routes.route('/formularios/', methods=['POST'])
@jwt_required()
def formulario_post():
    return create_formulario(request.json)


@formulario_routes.route('/formularios/<int:formulario_id>', methods=['GET'])
@jwt_required()
def formulario_get(formulario_id):
    return get_formulario_by_id(formulario_id)


@formulario_routes.route('/formularios/<int:formulario_id>', methods=['PUT'])
@jwt_required()
def formulario_put(formulario_id):
    return update_formulario(formulario_id, request.json)


@formulario_routes.route('/formularios/<int:formulario_id>', methods=['DELETE'])
@jwt_required()
def formulario_delete(formulario_id):
    return delete_formulario(formulario_id)