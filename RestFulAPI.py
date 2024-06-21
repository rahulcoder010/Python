from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

# MOCK lista desenvolvedores
devs = []

class Desenvolvedor(Resource):
    def get(self, id):
        desenvolvedor = list(filter(lambda dev: dev['id'] == id, devs))
        if desenvolvedor:
            return desenvolvedor[0]
        else:
            mensagem = f'Desenvolvedor de id {str(id)} não encontrado'
            response = {'status': 'erro', 'mensagem': mensagem}
            return response

    def put(self, id):
        desenvolvedor = list(filter(lambda dev: dev['id'] == id, devs))
        if desenvolvedor:
            desenvolvedor_atualizado = json.loads(request.data)
            desenvolvedor_atualizado['id'] = id
            index = devs.index(desenvolvedor[0])
            devs[index] = desenvolvedor_atualizado

            assert desenvolvedor_atualizado in devs
            assert desenvolvedor[0] not in devs

            return desenvolvedor_atualizado
        else:
            mensagem = f'Desenvolvedor de id {str(id)} não encontrado'
            response = {'status': 'erro', 'mensagem': mensagem}
            return response

    def delete(self, id):
        desenvolvedor = list(filter(lambda dev: dev['id'] == id, devs))
        if desenvolvedor:
            devs.remove(desenvolvedor[0])

            assert desenvolvedor[0] not in devs

            return desenvolvedor[0]
        else:
            mensagem = f'Desenvolvedor de id {str(id)} não encontrado'
            response = {'status': 'erro', 'mensagem': mensagem}
            return response

class Desenvolvedores(Resource):
    def get(self):
        return devs

    def post(self):
        dev = json.loads(request.data)
        id = 0 if len(devs) == 0 else devs[-1]['id']+1
        dev['id'] = id
        devs.append(dev)
        return devs[-1]


api.add_resource(Desenvolvedor, '/api/restful/dev/<int:id>')
api.add_resource(Desenvolvedores, '/api/restful/dev')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()