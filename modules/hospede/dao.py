from modules.hospede.sql import SQLHospede
from modules.hospede.modelo import Hospede

class DAOHospede(SQLHospede):

    def __init__(self):
        from service.connect import Connect
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def criar(self, hospede: Hospede):
        erros = []
        if not self.get_by_cpf(hospede.cpf):
            query = self._INSERT
            cursor = self.connection.cursor()
            cursor.execute(query, (
                hospede.nome,
                hospede.email,
                hospede.cpf,
                hospede.telefone
            ))
            self.connection.commit()
            return hospede
        else:
            erros.append(f'Hospede com CPF {hospede.cpf} ja cadastrado')

    def delete_hospede_by_id(self, id):
        query = self._DELETE_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, id)
        self.connection.commit()

    def delete_hospede_by_cpf(self, cpf):
        query = self._DELETE_BY_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        self.connection.commit()

    def update(self, cpf, novo_hospede_dados):
        hospede_existente = self.get_by_cpf(cpf)
        if not hospede_existente:
            raise ValueError(f'Hospede com CPF {cpf} não encontrado')

        nome = novo_hospede_dados.get('nome')
        if nome is None:
            raise ValueError('A chave "nome" é necessária no JSON enviado para a atualização do hospede.')

        email = novo_hospede_dados.get('email')
        if email and self.email_exists_for_other_hospede(cpf, email):
            raise ValueError(f'O email {email} ja esta sendo utilizado por outro hospede.')

        telefone = novo_hospede_dados.get('telefone')
        if telefone and self.telefone_exists_for_other_hospede(cpf, telefone):
            raise ValueError(f'O telefone {telefone} ja esta sendo utilizado por outro hospede.')

        query = """
            UPDATE hospede
            SET nome = %(nome)s, email = %(email)s, telefone = %(telefone)s
            WHERE cpf = %(cpf)s
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, {
                'nome': nome,
                'email': email,
                'cpf': cpf,
                'telefone': telefone
            })
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise ValueError(f'Erro ao atualizar hospede: {str(e)}')

        return novo_hospede_dados

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Hospede(**i) for i in results]
        return results

    def get_by_id(self, id):
        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            hospede_dict = dict(zip(cols, result))
            return Hospede(**hospede_dict)
        else:
            return None

    def get_by_cpf(self, cpf):
        query = self._SELECT_BY_CPF
        cursor = self.connection.cursor()
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            hospede_dict = dict(zip(cols, result))
            return Hospede(**hospede_dict)
        else:
            return None

    def get_by_email(self, email):
        query = self._SELECT_BY_EMAIL
        cursor = self.connection.cursor()
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            hospede_dict = dict(zip(cols, result))
            return Hospede(**hospede_dict)
        else:
            return None

    def get_by_telefone(self, telefone):
        query = self._SELECT_BY_TELEFONE
        cursor = self.connection.cursor()
        cursor.execute(query, (telefone,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            hospede_dict = dict(zip(cols, result))
            return Hospede(**hospede_dict)
        else:
            return None

    def telefone_exists_for_other_hospede(self, cpf, telefone):
        query = "SELECT cpf FROM hospede WHERE telefone = %s AND cpf != %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (telefone, cpf))
        return cursor.fetchone() is not None

    def email_exists_for_other_hospede(self, cpf, email):
        query = "SELECT cpf FROM hospede WHERE email = %s AND cpf != %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (email, cpf))
        return cursor.fetchone() is not None