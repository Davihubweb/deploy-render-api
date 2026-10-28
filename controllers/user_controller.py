from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_models import User
from db import db


def create_user(dados):
    if User.query.filter_by(email=dados['email']).first():
        return jsonify({'mensagem': 'Este email já está cadastrado.'}), 400

    novo_user = User(
        nome=dados['nome'],
        email=dados['email'],
        senha=generate_password_hash(dados['senha'])
    )
    db.session.add(novo_user)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário cadastrado com sucesso.', 'dados': novo_user.json()}), 201


def login(dados):
    user = User.query.filter_by(email=dados['email']).first()

    if not user or not check_password_hash(user.senha, dados['senha']):
        return jsonify({'mensagem': 'Email ou senha inválidos.'}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({'mensagem': 'Login realizado com sucesso.', 'access_token': token}), 200


def get_user_by_id(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'mensagem': 'Usuário não encontrado.'}), 404

    return jsonify({'mensagem': 'Usuário encontrado.', 'dados': user.json()}), 200


def update_user(user_id, dados):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'mensagem': 'Usuário não encontrado.'}), 404

    user.nome = dados.get('nome', user.nome)
    user.email = dados.get('email', user.email)

    if 'senha' in dados:
        user.senha = generate_password_hash(dados['senha'])

    db.session.commit()

    return jsonify({'mensagem': 'Usuário atualizado com sucesso.', 'dados': user.json()}), 200


def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'mensagem': 'Usuário não encontrado.'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário excluído com sucesso.'}), 200