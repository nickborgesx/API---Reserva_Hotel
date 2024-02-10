from flask import Blueprint, request, jsonify
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



@reserva_controller.route(f'/{module_name}/', methods=['GET'])
def get_all_reserva():
    return get_reservas()


@reserva_controller.route(f'/{module_name}/<id>/', methods=['GET'])
def get_reserva_by_id(id: int):
    print('id', id)
    return []
