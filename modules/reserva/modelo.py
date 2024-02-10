from modules.hospede.modelo import Hospede
from modules.quarto.modelo import Quarto
class Reserva:
    def __init__(self, entrada, saida, valor, quarto_id : Quarto, hospede_id : Hospede, id=None):
        self.entrada = entrada
        self.saida = saida
        self.valor = valor
        self.quarto_id = quarto_id
        self.hospede_id = hospede_id
        self.id = id