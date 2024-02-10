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