from flask import Blueprint, request
from controllers.aluno_controller import (
    get_alunos,
    get_aluno_by_id,
    create_aluno,
    update_aluno,
    delete_aluno,
)

aluno_routes = Blueprint('aluno_routes', __name__)

@aluno_routes.route('/alunos', methods=['GET'])
def alunos_get():
    return get_alunos()

@aluno_routes.route('/alunos/<int:aluno_id>', methods=['GET'])
def aluno_get_by_id_route(aluno_id):
    return get_aluno_by_id(aluno_id)

@aluno_routes.route('/alunos', methods=['POST'])
def alunos_post():
    return create_aluno(request.get_json())

@aluno_routes.route('/alunos/<int:aluno_id>', methods=['PUT'])
def aluno_put(aluno_id):
    return update_aluno(aluno_id, request.get_json())

@aluno_routes.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def aluno_delete(aluno_id):
    return delete_aluno(aluno_id)
