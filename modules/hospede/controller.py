from flask import Blueprint, request, jsonify
from modules.hospede.dao import DAOHospede

hospede_controller = Blueprint('hospede_controller', __name__)
dao_hospede = DAOHospede()
module_name = 'hospede'

def get_hospedes():
    hospedes = dao_hospede.get_all()
    results = [hospede.__dict__ for hospede in hospedes]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_hospede_by_id(id):
    hospede = dao_hospede.get_by_id(id)
    if hospede:
        response = jsonify(hospede.__dict__)
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'Hospede nao encontrado - [ID]'})
        response.status_code = 404
        return response

def get_hospede_by_cpf(cpf):
    hospede = dao_hospede.get_by_cpf(cpf)
    if hospede:
        response = jsonify(hospede.__dict__)
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'Hospede nao encontrado - [CPF]'})
        response.status_code = 404
        return response

def criar_hospede():
    hospedes = request.get_json()
    erros = []

    if isinstance(hospedes, dict):
        hospedes = [hospedes]

    for data in hospedes:
        cpf = data.get('cpf', '').strip()
        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()
        telefone = data.get('telefone', '').strip()

        if not cpf:
            erros.append('CPF nao fornecido para o hospede ou formato invalido')
            continue

        if dao_hospede.get_by_cpf(cpf):
            erros.append(f'Hospede com CPF {cpf} ja cadastrado')

        if not nome:
            erros.append('Nome não fornecido para o hospede ou formato invalido')

        if not email:
            erros.append('E-mail nao fornecido para o hospede ou formato invalido')
        elif dao_hospede.get_by_email(email):
            erros.append(f'Hospede com e-mail {email} ja cadastrado')

        if not telefone:
            erros.append('Telefone nao fornecido para o hospede ou formato invalido')
        elif dao_hospede.get_by_telefone(telefone):
            erros.append(f'Hospede com telefone {telefone} já cadastrado')

    if erros:
        response = jsonify({'errors': erros})
        response.status_code = 400
        return response

    response = jsonify({"message": "Hospede Criado!"})
    response.status_code = 201
    return response

def update_hospede(cpf):
    novo_hospede_dados = request.get_json()

    hospede_existente = dao_hospede.get_by_cpf(cpf)
    if not hospede_existente:
        print(f'Hospede com CPF {cpf} não encontrado')
        response = jsonify({'error': f'Hospede com CPF {cpf} não encontrado'})
        response.status_code = 404
        return response

    try:
        hospede_atualizado = dao_hospede.update(cpf, novo_hospede_dados)
        print(f'Hospede atualizado com sucesso: {hospede_atualizado}')
        response = jsonify({'message': 'Hospede atualizado com sucesso', 'hospede': hospede_atualizado})
        response.status_code = 200
    except ValueError as ve:
        print(f'Erro ao atualizar hospede: {str(ve)}')
        response = jsonify({'error': str(ve)})
        response.status_code = 400  # Bad Request
    except Exception as e:
        print(f'Erro ao atualizar hospede: {str(e)}')
        response = jsonify({'error': f'Erro ao atualizar hospede: {str(e)}'})
        response.status_code = 500

    return response

def delete_hospede(cpf):
    if not cpf:
        response = jsonify({"error": "CPF errado ou nao fornecido!"})
        response.status_code = 400
        return response

    if dao_hospede.delete_hospede_by_cpf(cpf):
        response = jsonify({"message": "Hospede deletado!"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"error": "Hospede nao encontrado"})
        response.status_code = 404
        return response

@hospede_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_all_hospede():
    if request.method == 'GET':
        return get_hospedes()
    elif request.method == 'POST':
        return criar_hospede()
    else:
        return jsonify({'message': 'Método não existente', 'status_code': 404})

@hospede_controller.route(f'/{module_name}/delete/<string:cpf>/', methods=['DELETE'])
def method_delete_hospede(cpf):
    if request.method == 'DELETE':
        return delete_hospede(cpf)

@hospede_controller.route(f'/{module_name}/id/<int:id>/', methods=['GET'])
def get_hospede_id(id):
    return get_hospede_by_id(id)

@hospede_controller.route(f'/{module_name}/cpf/<string:cpf>/', methods=['GET'])
def get_hospede_cpf(cpf):
    return get_hospede_by_cpf(cpf)

@hospede_controller.route(f'/{module_name}/update/<cpf>/', methods=['PUT'])
def put_update_hospede(cpf):
    return update_hospede(cpf)
