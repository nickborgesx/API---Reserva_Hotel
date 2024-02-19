from modules.hospede.sql import SQLHospede
from modules.hotel.sql import SQLHotel
from modules.quarto.sql import SQLQuarto


class SQLReserva:
    _TABLE_NAME = 'reserva'
    _COL_ID = 'id'
    _COL_ENTRADA = 'entrada'
    _COL_SAIDA = 'saida'
    _COL_VALOR = 'valor'
    _COL_QUARTO_ID = 'quarto_id'
    _COL_HOSPEDE_ID = 'hospede_id'
    _COL_HOTEL_ID = 'hotel_id'
    _REFERENCES_QUARTO = f'{SQLQuarto._TABLE_NAME}({SQLQuarto._COL_ID})'
    _REFERENCES_HOSPEDE = f'{SQLHospede._TABLE_NAME}({SQLHospede._COL_ID})'
    _REFERENCES_HOTEL = f'{SQLHotel._TABLE_NAME}({SQLHotel._COL_ID})'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_ENTRADA} date not null, ' \
                    f'{_COL_SAIDA} date not null, ' \
                    f'{_COL_VALOR} decimal(10, 2) not null, ' \
                    f'{_COL_QUARTO_ID} int REFERENCES {_REFERENCES_QUARTO}, ' \
                    f'{_COL_HOSPEDE_ID} int REFERENCES {_REFERENCES_HOSPEDE}, ' \
                    f'{_COL_HOTEL_ID} int REFERENCES {_REFERENCES_HOTEL} ' \
                    f');'

    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f'SELECT {_COL_ID}, {_COL_ENTRADA}, {_COL_SAIDA}, {_COL_VALOR}, {_COL_QUARTO_ID}, {_COL_HOSPEDE_ID}, {_COL_HOTEL_ID} FROM {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _INSERT = f'INSERT INTO {_TABLE_NAME}({_COL_ENTRADA}, {_COL_SAIDA}, {_COL_VALOR}, {_COL_QUARTO_ID}, {_COL_HOSPEDE_ID}, {_COL_HOTEL_ID}) VALUES (%s, %s, %s, %s, %s, %s);'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _UPDATE_RESERVA = f'UPDATE {_TABLE_NAME} SET {_COL_ENTRADA} = %s, {_COL_SAIDA} = %s, {_COL_VALOR} = %s, {_COL_QUARTO_ID} = %s, {_COL_HOSPEDE_ID} = %s, {_COL_HOTEL_ID} = %s WHERE {_COL_ID} = %s'
    _SELECT_CREATE_VERIFIC = f"SELECT * FROM {_TABLE_NAME} WHERE {_COL_ENTRADA} = %s AND {_COL_QUARTO_ID} = %s"
    _SELECT_BY_ENTRADA_QUARTO = f'SELECT * FROM {_TABLE_NAME} WHERE {_COL_ENTRADA} = %s AND {_COL_QUARTO_ID} = %s'
    _SELECT_BY_QUARTO_ID = f'SELECT * FROM {_TABLE_NAME} WHERE {_COL_QUARTO_ID} = %s'
    _SELECT_HOTEL_ID = f"SELECT * FROM reserva WHERE {_COL_HOTEL_ID} = %s"
    _SELECT_QUARTOS_BY_HOTEL = f"SELECT * FROM {SQLQuarto._TABLE_NAME} WHERE {SQLQuarto._COL_HOTEL_ID} = %s"
    _CHECK_RESERVA_BELONGS_TO_HOTEL = f"SELECT COUNT(*) FROM {_TABLE_NAME} WHERE {_COL_ID} = %s AND {_COL_HOTEL_ID} = %s"