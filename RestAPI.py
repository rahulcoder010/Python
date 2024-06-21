from flask import Flask, jsonify, request
import json
#import requests

app = Flask(__name__)

# MOCK lista desenvolvedores
devs = []

@app.route('/api')
def mensagem():
    return 'API de desenvolvedores'

@app.route('/api/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id {str(id)} não encontrado'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dev = json.loads(request.data)
        dev['id'] = id
        devs[id] = dev
        return jsonify(dev)
    elif request.method == 'DELETE':
        devs.pop(id)
        mensagem = 'Registro excluído'
        response = {'status': 'sucesso', 'mensagem': mensagem}
        return jsonify(response)
    else:
        mensagem = 'Método http não suportado'
        response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

@app.route('/api/dev', methods=['GET', 'POST'])
def desenvolvedores():
    if request.method == 'GET':
        return jsonify(devs)
    elif request.method == 'POST':
        dev = json.loads(request.data)
        posicao = len(devs)
        dev['id'] = posicao
        devs.append(dev)
        return jsonify(devs[posicao])
    else:
        mensagem = 'Método http não suportado'
        response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
