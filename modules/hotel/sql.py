class SQLHotel:
    _TABLE_NAME = 'hotel'
    _COL_ID = 'id'
    _COL_NOME = 'nome'
    _COL_RUA = 'rua'
    _COL_BAIRRO = 'bairro'
    _COL_CIDADE = 'cidade'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (' \
                    f'{_COL_ID} SERIAL PRIMARY KEY, ' \
                    f'{_COL_NOME} VARCHAR(255), ' \
                    f'{_COL_RUA} VARCHAR(255), ' \
                    f'{_COL_BAIRRO} VARCHAR(255), ' \
                    f'{_COL_CIDADE} VARCHAR(255) ' \
                    f');'

    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f'SELECT * from {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _INSERT = f'INSERT INTO {_TABLE_NAME}({_COL_NOME}, {_COL_RUA}, {_COL_BAIRRO}, {_COL_CIDADE}) VALUES (%s, %s, %s, %s);'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _UPDATE_HOTEL = f'UPDATE {_TABLE_NAME} SET {_COL_NOME} = %s, {_COL_RUA} = %s, {_COL_BAIRRO} = %s, {_COL_CIDADE} = %s WHERE {_COL_ID} = %s'
