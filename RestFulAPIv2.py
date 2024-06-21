from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import Desenvolvedores


app = Flask(__name__)
api = Api(app)

# MOCK lista desenvolvedores
devs = []

class DesenvolvedorResource(Resource):
    def get(self, id):
        try:
            desenvolvedor = Desenvolvedores.query.filter_by(id=id).first()
            response = {
                "nome": desenvolvedor.nome,
                "id": desenvolvedor.id
            }
        except:
            mensagem = f'Desenvolvedor de id {str(id)} não encontrado'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        try:
            desenvolvedor = Desenvolvedores.query.filter_by(id=id).first()
            dados = request.json

            if 'nome' in dados:
                desenvolvedor.nome = dados['nome']

            desenvolvedor.save()

            response = {
                "nome": desenvolvedor.nome,
                "id": desenvolvedor.id
            }
        except:
            mensagem = f'Desenvolvedor de id {str(id)} não atualizado'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response


    def delete(self, id):
        try:
            desenvolvedor = Desenvolvedores.query.filter_by(id=id).first()
            desenvolvedor.delete()
            mensagem = f'Desenvolvedor de id {id} excluído com sucesso'
            response = {'status': 'sucesso', 'mensagem': mensagem}
        except:
            response = {'status':'erro'}
        return response

class DesenvolvedoresResource(Resource):
    def get(self):
        try:
            desenvolvedores = Desenvolvedores.query.all()
            response = [
                {
                    "id": d.id,
                    "nome": d.nome
                 } for d in desenvolvedores
            ]
        except:
            response = {'Nenhum desenvolvedor encontrado'}

        return response

    def post(self):
        try:
            dados = request.json
            desenvolvedor = Desenvolvedores(nome=dados['nome'])
            desenvolvedor.save()

            response = {
                "id": desenvolvedor.id,
                "nome": desenvolvedor.nome
            }
        except:
            response = {'status': 'erro'}
        return response

api.add_resource(DesenvolvedorResource, '/api/restful/v2/dev/<int:id>')
api.add_resource(DesenvolvedoresResource, '/api/restful/v2/dev')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()