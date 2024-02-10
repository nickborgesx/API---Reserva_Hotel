from flask import Blueprint, request, jsonify
from modules.hotel.dao import DAOHotel

hotel_controller = Blueprint('hotel_controller', __name__)
dao_hotel = DAOHotel()
module_name = 'hotel'


def get_hotels():
    hotels = dao_hotel.get_all()
    results = [hotel.__dict__ for hotel in hotels]
    response = jsonify(results)
    response.status_code = 200
    return response



@hotel_controller.route(f'/{module_name}/', methods=['GET'])
def get_all_hospede():
    return get_hotels()


@hotel_controller.route(f'/{module_name}/<id>/', methods=['GET'])
def get_hotel_by_id(id: int):
    print('id', id)
    return []
