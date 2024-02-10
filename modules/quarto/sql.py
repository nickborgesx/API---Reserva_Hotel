class SQLQuarto:
    _TABLE_NAME = 'quarto'
    _COL_ID = 'id'
    _COL_NUMERO = 'numero'
    _COL_CAPACIDADE = 'capacidade'
    _COL_DISPONIVEL = 'disponivel'
    _COL_HOTEL_ID = 'hotel_id'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (' \
                    f'{_COL_ID} SERIAL PRIMARY KEY, ' \
                    f'{_COL_NUMERO} VARCHAR(255), ' \
                    f'{_COL_CAPACIDADE} VARCHAR(255), ' \
                    f'{_COL_DISPONIVEL} BOOLEAN NOT NULL, ' \
                    f'{_COL_HOTEL_ID} INT REFERENCES hotel ({_COL_ID}) ' \
                    f');'

    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
