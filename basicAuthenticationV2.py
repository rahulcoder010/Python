from flask import Flask
from flask_httpauth import HTTPBasicAuth
from models import Usuarios

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verificacao(login, senha):
    print('Validando usuario')
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

@app.route('/api/v2/login')
@auth.login_required
def logar():
    return 'Usuário logado.'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()