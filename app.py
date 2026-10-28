import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from db import db
from routes.user_routes import user_routes
from routes.formulario_routes import formulario_routes
from routes.aluno_routes import aluno_routes

app = Flask(__name__)

# Render fornece a porta e pode fornecer a chave secreta pelas variáveis de ambiente.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///projeto.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'chave-local-apenas-para-testes')
app.json.ensure_ascii = False

db.init_app(app)
JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(formulario_routes)
app.register_blueprint(aluno_routes)

# Importa os modelos para que o SQLAlchemy conheça as tabelas.
from models.user_models import User
from models.formulario_models import Formulario
from models.aluno_models import Aluno

with app.app_context():
    db.create_all()

@app.get('/')
def home():
    return jsonify({'mensagem': 'API online e funcionando.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
