# API Flask — Deploy no Render

## Configuração no Render
- Runtime: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

A rota `/` confirma que a API está online. As rotas de usuários, formulários e alunos podem ser testadas via Postman.

Para produção, configure `JWT_SECRET_KEY` como variável de ambiente no Render. O SQLite é adequado para demonstração, mas o armazenamento local do serviço gratuito pode não persistir após reinicializações/deploys.
