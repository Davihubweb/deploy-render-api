from db import db


class Formulario(db.Model):
    __tablename__ = 'formularios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.String(300), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'mensagem': self.mensagem
        }