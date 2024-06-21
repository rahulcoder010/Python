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