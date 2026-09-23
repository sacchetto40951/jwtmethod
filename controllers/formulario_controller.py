import json

from flask import make_response

from models.formulario_model import FormularioModel  


def _json_response(message, payload, status=200):
    response = make_response(
        json.dumps({
            'mensagem': message,
            'dados': payload  
        }, ensure_ascii=False, sort_keys=False),
        status
    )
    response.headers['Content-Type'] = 'application/json'
    return response


class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  

        formulario = FormularioModel.create_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500 

    @staticmethod
    def formulario_get():
        form = FormularioModel.query.all()
        return _json_response('Dados', [item.json() for item in form])