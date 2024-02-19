from flask import Blueprint, request, jsonify
from modules.quarto.dao import DAOQuarto
from modules.quarto.modelo import Quarto

quarto_controller = Blueprint('quarto_controller', __name__)
dao_quarto = DAOQuarto()
module_name = 'quarto'


def get_quartos():
    quartos = dao_quarto.get_all()
    results = [quarto.__dict__ for quarto in quartos]
    response = jsonify(results)
    response.status_code = 200
    return response


def get_quartos_by_hotel_id(hotel_id):
    quartos = dao_quarto.get_quartos_by_hotel(hotel_id)

    if quartos:
        results = [quarto.__dict__ for quarto in quartos]
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        response = jsonify(f'Nenhum quarto encontrado para o hotel com ID {hotel_id}')
        response.status_code = 404
        return response

def criar_quarto():
    dados_quarto = request.get_json()
    erros = []

    if 'numero' not in dados_quarto or 'capacidade' not in dados_quarto or 'disponivel' not in dados_quarto or 'hotel_id' not in dados_quarto:
        erros.append('Os campos numero, capacidade, disponivel e hotel_id são obrigatórios.')

    if erros:
        response = jsonify({'error': ', '.join(erros)})
        response.status_code = 400  # Bad Request
        return response

    numero_quarto = dados_quarto['numero']
    hotel_id = dados_quarto['hotel_id']

    if dao_quarto.quarto_existente(numero_quarto, hotel_id):
        response = jsonify({'error': 'Quarto já existente para este hotel'})
        response.status_code = 409  # Conflict
        return response

    novo_quarto = Quarto(
        numero=numero_quarto,
        capacidade=dados_quarto['capacidade'],
        disponivel=dados_quarto['disponivel'],
        hotel_id=hotel_id
    )

    try:
        dao_quarto.criar(novo_quarto)
        response = jsonify({'message': 'Quarto criado com sucesso'})
        response.status_code = 201  # Created
    except Exception as e:
        print(f'Erro ao criar quarto: {str(e)}')
        response = jsonify({'error': f'Erro ao criar quarto: {str(e)}'})
        response.status_code = 500  # Internal Server Error

    return response

def delete_quarto(hotel_id, id):
    if not hotel_id or not id:
        response = jsonify({"error": "ID ou hotel_id incorreto ou não fornecido!"})
        response.status_code = 400
        return response

    quarto_existente = dao_quarto.get_by_id(id)

    if not quarto_existente or quarto_existente.hotel_id != hotel_id:
        response_data = f"Quarto com o ID {id} não encontrado para o hotel com ID {hotel_id}"
        response_status = 404
    else:
        try:
            dao_quarto.delete_quarto_by_id(id)
            response_data = "Quarto deletado!"
            response_status = 200
        except Exception as e:
            print(f'Erro ao deletar quarto: {str(e)}')
            response_data = f'Erro ao deletar quarto: {str(e)}'
            response_status = 500

    response = jsonify({"message": response_data})
    response.status_code = response_status
    return response

def update_quarto(hotel_id, id):
    dados_quarto = request.get_json()
    erros = []

    if 'numero' not in dados_quarto or 'capacidade' not in dados_quarto or 'disponivel' not in dados_quarto:
        erros.append('Os campos numero, capacidade e disponivel são obrigatórios.')

    if erros:
        response = jsonify({'error': ', '.join(erros)})
        response.status_code = 400  # Bad Request
        return response

    quarto_existente = dao_quarto.get_by_id(id)

    if not quarto_existente or quarto_existente.hotel_id != hotel_id:
        response = jsonify({f'Quarto com ID {id} não encontrado para o hotel com ID {hotel_id}.'})
        response.status_code = 404  # Not Found
        return response

    for key, value in dados_quarto.items():
        if isinstance(value, set):
            dados_quarto[key] = list(value)

    quarto_atualizado = Quarto(
        numero=dados_quarto['numero'],
        capacidade=dados_quarto['capacidade'],
        disponivel=dados_quarto['disponivel'],
        hotel_id=hotel_id,
        id=id
    )

    try:
        dao_quarto.update_quarto(quarto_atualizado)
        response = jsonify({'message': 'Quarto atualizado com sucesso'})
        response.status_code = 200  # OK
    except Exception as e:
        print(f'Erro ao atualizar quarto: {str(e)}')
        response = jsonify({'error': f'Erro ao atualizar quarto: {str(e)}'})
        response.status_code = 500  # Internal Server Error

    return response


@quarto_controller.route(f'/{module_name}/', methods=['GET'])
def get_all_quarto():
    if request.method == 'GET':
        return get_quartos()
    else:
        return jsonify({'message': 'Método não existente', 'status_code': 404})

@quarto_controller.route(f'/{module_name}/create/', methods=['POST'])
def create_quarto():
    return criar_quarto()

@quarto_controller.route(f'/{module_name}/delete/<int:hotel_id>/<int:id>/', methods=['DELETE'])
def method_delete_quarto(hotel_id, id):
    return delete_quarto(hotel_id, id)

@quarto_controller.route(f'/{module_name}/hotel/<int:hotel_id>/', methods=['GET'])
def get_quartos_by_hotel_id_route(hotel_id):
    return get_quartos_by_hotel_id(hotel_id)

@quarto_controller.route(f'/{module_name}/update/<int:hotel_id>/<int:id>/', methods=['PUT'])
def put_update_quarto(hotel_id, id):
    return update_quarto(hotel_id, id)

@quarto_controller.route(f'/{module_name}/disponiveis/<string:disponivel>/', methods=['GET'])
def get_quartos_disponiveis(disponivel):
    if request.method == 'GET':
        if disponivel.lower() == 'true':
            quartos = [quarto.__dict__ for quarto in dao_quarto.get_all() if quarto.disponivel]
        elif disponivel.lower() == 'false':
            quartos = [quarto.__dict__ for quarto in dao_quarto.get_all() if not quarto.disponivel]
        else:
            response = jsonify({'error': 'Valor inválido para o parâmetro "disponivel" (deve ser "true" ou "false")'})
            response.status_code = 400  # Bad Request
            return response

        response = jsonify(quartos)
        response.status_code = 200
        return response
    else:
        return jsonify({'message': 'Método não existente', 'status_code': 404})
