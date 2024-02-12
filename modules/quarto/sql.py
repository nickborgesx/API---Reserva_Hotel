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
    _SELECT_BY_ID = f'SELECT * from {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _INSERT = f'INSERT INTO {_TABLE_NAME}({_COL_NUMERO}, {_COL_CAPACIDADE}, {_COL_DISPONIVEL}, {_COL_HOTEL_ID}) VALUES (%s, %s, %s, %s);'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _UPDATE_QUARTO = f'UPDATE {_TABLE_NAME} SET {_COL_NUMERO} = %s, {_COL_CAPACIDADE} = %s, {_COL_DISPONIVEL} = %s, {_COL_HOTEL_ID} = %s WHERE {_COL_ID} = %s'
    _SELECT_CREATE_VERIFIC = f"SELECT * FROM {_TABLE_NAME} WHERE {_COL_NUMERO} = %s AND {_COL_HOTEL_ID} = %s"
