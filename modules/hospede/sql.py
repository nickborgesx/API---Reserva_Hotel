class SQLHospede:
    _TABLE_NAME = 'hospede'
    _COL_ID = 'id'
    _COL_NOME = 'nome'
    _COL_EMAIL = 'email'
    _COL_CPF = 'cpf'
    _COL_TELEFONE = 'telefone'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}' \
                    f'(id serial primary key, ' \
                    f'{_COL_NOME} varchar(255), ' \
                    f'{_COL_EMAIL} varchar(255), ' \
                    f'{_COL_CPF} varchar(255), ' \
                    f'{_COL_TELEFONE} varchar(255) ' \
                    f');'

    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f'SELECT * from {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _SELECT_BY_CPF = f'SELECT * from {_TABLE_NAME} WHERE {_COL_CPF} = %s'
    _SELECT_BY_TELEFONE = f'SELECT * from {_TABLE_NAME} WHERE {_COL_TELEFONE} = %s'
    _SELECT_ID_BY_CPF = f'SELECT {_COL_ID} from {_TABLE_NAME} where {_COL_CPF} = %s'
    _SELECT_BY_EMAIL = f'SELECT * from {_TABLE_NAME} where {_COL_EMAIL} = %s'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_ID} = %s'
    _DELETE_BY_CPF = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_CPF} = %s'
    _INSERT = f'INSERT INTO {_TABLE_NAME}({_COL_NOME}, {_COL_EMAIL}, {_COL_CPF}, {_COL_TELEFONE}) VALUES (%s, %s, %s, %s);'
    _UPDATE_HOSPEDE = f'UPDATE {_TABLE_NAME} SET {_COL_NOME} = %s, {_COL_EMAIL} = %s, {_COL_TELEFONE} = %s WHERE {_COL_CPF} = %s'
    _SELECT_VE_TELEFONE =f'SELECT cpf FROM hospede WHERE telefone = %s AND cpf != %s'