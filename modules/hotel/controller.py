from flask import Blueprint, request, jsonify
from modules.hotel.dao import DAOHotel
from modules.hotel.modelo import Hotel

hotel_controller = Blueprint('hotel_controller', __name__)
dao_hotel = DAOHotel()
module_name = 'hotel'

def get_hoteis():
    hoteis = dao_hotel.get_all()
    results = [hotel.__dict__ for hotel in hoteis]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_hotel_by_id(id):
    hotel = dao_hotel.get_by_id(id)
    if hotel:
        response = jsonify(hotel.__dict__)
        response.status_code = 200
        return response
    else:
        response = jsonify('hotel nao encontrado - [ID]')
        response.status_code = 404
        return response

def criar_hotel():
    dados_hotel = request.get_json()
    erros = []

    if 'nome' not in dados_hotel or 'rua' not in dados_hotel or 'bairro' not in dados_hotel or 'cidade' not in dados_hotel:
        erros.append('Os campos nome, rua, bairro e cidade são obrigatórios.')

    if erros:
        response = jsonify({'error': ', '.join(erros)})
        response.status_code = 400  # Bad Request
        return response

    novo_hotel = Hotel(
        nome=dados_hotel['nome'],
        rua=dados_hotel['rua'],
        bairro=dados_hotel['bairro'],
        cidade=dados_hotel['cidade']
    )

    try:
        dao_hotel.criar(novo_hotel)
        response = jsonify({'message': 'Hotel criado com sucesso'})
        response.status_code = 201  # Created
    except Exception as e:
        print(f'Erro ao criar hotel: {str(e)}')
        response = jsonify({'error': f'Erro ao criar hotel: {str(e)}'})
        response.status_code = 500  # Internal Server Error

    return response
def delete_hotel(id):
    if not id:
        response = jsonify({"error": "ID errado ou nao fornecido!"})
        response.status_code = 400
        return response

    hotel_existente = dao_hotel.get_by_id(id)

    if not hotel_existente:
        response_data = f"Hotel com o ID {id} nao encontrado"
        response_status = 404
    else:
        try:
            dao_hotel.delete_hotel_by_id(id)
            response_data = "Hotel deletado!"
            response_status = 200
        except Exception as e:
            print(f'Erro ao deletar hotel: {str(e)}')
            response_data = f'Erro ao deletar hotel: {str(e)}'
            response_status = 500

    response = jsonify({"message": response_data})
    response.status_code = response_status
    return response


def update_hotel(id):
    dados_hotel = request.get_json()
    erros = []

    if 'nome' not in dados_hotel or 'rua' not in dados_hotel or 'bairro' not in dados_hotel or 'cidade' not in dados_hotel:
        erros.append('Os campos nome, rua, bairro e cidade são obrigatórios.')

    if erros:
        response = jsonify({'error': ', '.join(erros)})
        response.status_code = 400  # Bad Request
        return response

    hotel_existente = dao_hotel.get_by_id(id)

    if not hotel_existente:
        response = jsonify({f'Hotel com ID {id} não encontrado.'})
        response.status_code = 404
        return response

    hotel_atualizado = Hotel(
        nome=dados_hotel['nome'],
        rua=dados_hotel['rua'],
        bairro=dados_hotel['bairro'],
        cidade=dados_hotel['cidade'],
        id=id
    )

    try:
        dao_hotel.update_hotel(hotel_atualizado)
        response = jsonify({'menssage':'Hotel atualizado com sucesso'})
        response.status_code = 200
    except Exception as e:
        error_message = str(e)
        print(f'Erro ao atualizar hotel: {error_message}')
        response = jsonify({'error': f'Erro ao atualizar hotel: {error_message}'})
        response.status_code = 500

    return response

@hotel_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_all_hotel():
    if request.method == 'GET':
        return get_hoteis()
    elif request.method == 'POST':
        return criar_hotel()
    else:
        return jsonify({'message': 'Método não existente', 'status_code': 404})


@hotel_controller.route(f'/{module_name}/delete/<int:id>/', methods=['DELETE'])
def method_delete_hotel(id):
    return delete_hotel(id)

@hotel_controller.route(f'/{module_name}/id/<int:id>/', methods=['GET'])
def get_id(id):
    return get_hotel_by_id(id)

@hotel_controller.route(f'/{module_name}/update/<int:id>/', methods=['PUT'])
def put_update_hotel(id):
    return update_hotel(id)
