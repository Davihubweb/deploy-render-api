from flask import jsonify
from models.formulario_models import Formulario
from db import db


def create_formulario(dados):
    novo = Formulario(
        nome=dados['nome'],
        email=dados['email'],
        mensagem=dados['mensagem']
    )
    db.session.add(novo)
    db.session.commit()

    return jsonify({'mensagem': 'Formulário cadastrado com sucesso.', 'dados': novo.json()}), 201


def get_formulario_by_id(formulario_id):
    formulario = Formulario.query.get(formulario_id)

    if not formulario:
        return jsonify({'mensagem': 'Formulário não encontrado.'}), 404

    return jsonify({'mensagem': 'Formulário encontrado.', 'dados': formulario.json()}), 200


def update_formulario(formulario_id, dados):
    formulario = Formulario.query.get(formulario_id)

    if not formulario:
        return jsonify({'mensagem': 'Formulário não encontrado.'}), 404

    formulario.nome = dados.get('nome', formulario.nome)
    formulario.email = dados.get('email', formulario.email)
    formulario.mensagem = dados.get('mensagem', formulario.mensagem)

    db.session.commit()

    return jsonify({'mensagem': 'Formulário atualizado com sucesso.', 'dados': formulario.json()}), 200


def delete_formulario(formulario_id):
    formulario = Formulario.query.get(formulario_id)

    if not formulario:
        return jsonify({'mensagem': 'Formulário não encontrado.'}), 404

    db.session.delete(formulario)
    db.session.commit()

    return jsonify({'mensagem': 'Formulário excluído com sucesso.'}), 200