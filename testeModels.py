from models import Desenvolvedores, Usuarios

def insere_desenvolvedor():
    desenvolvedor = Desenvolvedores(nome='Developer')
    print(desenvolvedor)
    desenvolvedor.save()

def consulta_desenvolvedor():
    desenvolvedores = Desenvolvedores.query.all()
    print(desenvolvedores)

def altera_desenvolvedor():
    desenvolvedor = Desenvolvedores.query.filter_by(nome='Developer').first()
    desenvolvedor.nome='Dev'
    desenvolvedor.save()

def exclui_desenvolvedor():
    desenvolvedor = Desenvolvedores.query.filter_by(nome='Developer').first()
    desenvolvedor.delete()

def insere_usuario():
    usuario = Usuarios(login='Admin', senha='pass')
    print(usuario)
    usuario.save()

def consulta_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    #deleteall
    insere_desenvolvedor()
    consulta_desenvolvedor()
    altera_desenvolvedor()
    consulta_desenvolvedor()
    exclui_desenvolvedor()
    consulta_desenvolvedor()

    #Usuario
    insere_usuario()
    consulta_usuario()

# Flask - Rest and Restful API
## Routes RestAPI:
- /api
- /api/dev/<id>
- /api/dev

## RestFulAPI:
- /api/restful/dev/<id>
- /api/restful/dev

## RestFulAPIv2:
- /api/restful/v2/dev/<id>
- /api/restful/v2/dev

## basicAuthentication:
- /api/login

## basicAuthenticationV2:
- /api/v2/login

## References
Digital Innovation One - Desenvolvendo Rest APIs Com Python e Flask: https://web.dio.me/course/desenvolvimento-avancado-de-rest-api-com-flask/learning/f2b22f12-5b79-4e9a-80a8-c916e387c423