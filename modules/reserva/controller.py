from flask import Blueprint, request, jsonify

from modules.hospede.controller import dao_hospede
from modules.quarto.controller import dao_quarto
from modules.reserva.dao import DAOReserva

reserva_controller = Blueprint('reserva_controller', __name__)
dao_reserva = DAOReserva()
module_name = 'reserva'


def get_reservas():
    reservas = dao_reserva.get_all()
    results = [reserva.__dict__ for reserva in reservas]
    response = jsonify(results)
    response.status_code = 200
    return response

def get_reserva_by_id(reserva_id):
    reserva = dao_reserva.get_by_id(reserva_id)
    if reserva:
        response = jsonify(reserva.__dict__)
        response.status_code = 200
        return response
    else:
        response = jsonify(f'Reserva com ID {reserva_id} não encontrada.')
        response.status_code = 404
        return response

def criar_reserva():
    data = request.get_json()
    entrada = data.get('entrada')
    saida = data.get('saida')
    valor = data.get('valor')
    quarto_id = data.get('quarto_id')
    hospede_id = data.get('hospede_id')
    hotel_id = data.get('hotel_id')

    if not entrada or not saida or not valor or not quarto_id or not hospede_id or not hotel_id:
        response = jsonify({"message": "Todos os campos são obrigatórios!"})
        response.status_code = 400
        return response

    if not dao_quarto.get_by_id(quarto_id) or not dao_hospede.get_by_id(hospede_id):
        response = jsonify({"message": "Quarto ou hóspede não encontrado!"})
        response.status_code = 404
        return response

    if dao_reserva.check_date_conflict(quarto_id, entrada, saida):
        response = jsonify({"message": "Conflito de datas! Já existe uma reserva para este quarto no mesmo período."})
        response.status_code = 409
        return response

    dao_reserva.criar(entrada, saida, valor, quarto_id, hospede_id, hotel_id)

    response = jsonify({"message": "Reserva criada com sucesso!"})
    response.status_code = 201
    return response

def delete_reserva(id):
    if not id:
        response = jsonify({"ID não fornecido!"})
        response.status_code = 400
        return response
    dao_reserva.delete_by_id(id)
    response = jsonify({"message": "Reserva deletada!"})
    response.status_code = 200
    return response

import logging

def put_update_reserva(hotel_id, id):
    data = request.get_json()
    entrada = data.get('entrada')
    saida = data.get('saida')
    valor = data.get('valor')
    quarto_id = data.get('quarto_id')
    hospede_id = data.get('hospede_id')

    if not entrada or not saida or not valor or not quarto_id or not hospede_id or not hotel_id:
        response = jsonify({"message": "Todos os campos são obrigatórios!"})
        response.status_code = 400
        return response

    existing_reserva = dao_reserva.get_by_id(id)

    if not existing_reserva:
        logging.error(f"Reserva com ID {id} não encontrada.")
        response = jsonify({"message": f"Reserva com ID {id} não encontrada."})
        response.status_code = 404
        return response

    if not dao_quarto.get_by_id(quarto_id) or not dao_hospede.get_by_id(hospede_id):
        logging.error("Quarto ou hóspede não encontrado!")
        response = jsonify({"message": "Quarto ou hóspede não encontrado!"})
        response.status_code = 404
        return response

    if (
        existing_reserva.entrada == entrada
        and existing_reserva.saida == saida
        and existing_reserva.valor == valor
        and existing_reserva.quarto_id == quarto_id
        and existing_reserva.hospede_id == hospede_id
    ):
        logging.info("A reserva é a mesma, nenhum dado foi alterado.")
        response = jsonify({"message": "A reserva é a mesma, nenhum dado foi alterado."})
        response.status_code = 200
        return response

    if dao_reserva.check_date_conflict(quarto_id, entrada, saida, id):
        logging.error("Conflito de datas! Já existe uma reserva para este quarto no mesmo período.")
        response = jsonify({"message": "Conflito de datas! Já existe uma reserva para este quarto no mesmo período."})
        response.status_code = 409
        return response

    dao_reserva.update_reserva(entrada, saida, valor, quarto_id, hospede_id, hotel_id, id)

    logging.info("Reserva atualizada com sucesso!")
    response = jsonify({"message": "Reserva atualizada com sucesso!"})
    response.status_code = 200
    return response

def get_reservas_by_hotel(hotel_id):
    quartos_do_hotel = dao_quarto.get_quartos_by_hotel(hotel_id)
    reservas_do_hotel = []
    for quarto in quartos_do_hotel:
        reservas_do_quarto = dao_reserva.get_reservas_by_quarto(quarto.id)
        reservas_do_hotel.extend(reservas_do_quarto)
    results = [reserva.__dict__ for reserva in reservas_do_hotel]
    response = jsonify(results)
    response.status_code = 200
    return response

@reserva_controller.route(f'/{module_name}/', methods=['GET'])
def get_all_reserva():
    if request.method == 'GET':
        return get_reservas()
    else:
        return jsonify({'message': 'Método não existente', 'status_code': 404})

@reserva_controller.route(f'/{module_name}/create/', methods=['POST'])
def c_reserva():
    return criar_reserva()

@reserva_controller.route(f'/{module_name}/delete/<int:id>/', methods=['DELETE'])
def method_delete_reserva(id):
    return delete_reserva(id)

@reserva_controller.route(f'/{module_name}/<int:id>/', methods=['GET'])
def get_id(id):
    return get_reserva_by_id(id)

@reserva_controller.route(f'/{module_name}/update/<int:hotel_id>/<int:id>/', methods=['PUT'])
def update_reserva(hotel_id, id):
    return put_update_reserva(hotel_id, id)

@reserva_controller.route(f'/{module_name}/hotel/<int:hotel_id>/', methods=['GET'])
def get_all_hotel_reserva(hotel_id):
    return get_reservas_by_hotel(hotel_id)
