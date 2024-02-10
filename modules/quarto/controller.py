from flask import Blueprint, request, jsonify
from modules.quarto.dao import DAOQuarto

quarto_controller = Blueprint('quarto_controller', __name__)
dao_quarto = DAOQuarto()
module_name = 'quarto'


def get_quartos():
    quartos = dao_quarto.get_all()
    results = [quarto.__dict__ for quarto in quartos]
    response = jsonify(results)
    response.status_code = 200
    return response



@quarto_controller.route(f'/{module_name}/', methods=['GET'])
def get_all_quarto():
    return get_quartos()


@quarto_controller.route(f'/{module_name}/<id>/', methods=['GET'])
def get_quarto_by_id(id: int):
    print('id', id)
    return []
