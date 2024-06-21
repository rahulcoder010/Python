from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

USUARIOS_FIXOS = {
    "admin" : "pass"
}

@auth.verify_password
def verificacao(login, senha):
    print('Validando usuario')
    #print(USUARIOS_FIXOS.get(login) == senha)
    if not (login, senha):
        return False
    return USUARIOS_FIXOS.get(login) == senha

@app.route('/api/login')
@auth.login_required
def logar():
    return 'Usuário logado.'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()