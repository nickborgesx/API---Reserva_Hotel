from modules.hospede.sql import SQLHospede
from modules.quarto.sql import SQLQuarto


class SQLReserva:
    _TABLE_NAME = 'reserva'
    _COL_ID = 'id'
    _COL_ENTRADA = 'entrada'
    _COL_SAIDA = 'saida'
    _COL_VALOR = 'valor'
    _COL_QUARTO_ID = 'quarto_id'
    _COL_HOSPEDE_ID = 'hospede_id'
    _REFERENCES_QUARTO = f'{SQLQuarto._TABLE_NAME}({SQLQuarto._COL_ID})'
    _REFERENCES_HOSPEDE = f'{SQLHospede._TABLE_NAME}({SQLHospede._COL_ID})'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_ENTRADA} date not null, ' \
                    f'{_COL_SAIDA} date not null, ' \
                    f'{_COL_VALOR} decimal(10, 2) not null, ' \
                    f'{_COL_QUARTO_ID} int REFERENCES {_REFERENCES_QUARTO}, ' \
                    f'{_COL_HOSPEDE_ID} int REFERENCES {_REFERENCES_HOSPEDE} ' \
                    f');'

    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"