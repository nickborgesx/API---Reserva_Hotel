from flask import Flask

from modules.hospede.controller import hospede_controller
from modules.hotel.controller import hotel_controller
from modules.quarto.controller import quarto_controller
from modules.reserva.controller import reserva_controller


from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(hospede_controller)
app.register_blueprint(hotel_controller)
app.register_blueprint(quarto_controller)
app.register_blueprint(reserva_controller)

Connect().init_database('v1')
app.run(debug=True)