from modules.quarto.sql import SQLQuarto
from modules.quarto.modelo import Quarto

class DAOQuarto(SQLQuarto):
    def __init__(self):
        from service.connect import Connect
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def criar(self, quarto: Quarto):
        query = self._INSERT
        cursor = self.connection.cursor()
        cursor.execute(query, (
            quarto.numero,
            quarto.capacidade,
            quarto.disponivel,
            quarto.hotel_id
        ))
        self.connection.commit()
        return quarto

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Quarto(**i) for i in results]
        return results

    def get_by_id(self, id):
        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            quarto_dict = dict(zip(cols, result))
            return Quarto(**quarto_dict)
        else:
            return None

    def quarto_existente(self, numero, hotel_id):
        query = self._SELECT_CREATE_VERIFIC
        cursor = self.connection.cursor()
        cursor.execute(query, (numero, hotel_id))
        return cursor.fetchone() is not None

    def update_quarto(self, quarto: Quarto):
        query = self._UPDATE_QUARTO
        cursor = self.connection.cursor()
        cursor.execute(query, (
            quarto.numero,
            quarto.capacidade,
            quarto.disponivel,
            quarto.hotel_id,
            quarto.id
        ))
        self.connection.commit()

    def delete_quarto_by_id(self, id):
        query = self._DELETE_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        self.connection.commit()

    def get_quartos_by_hotel(self, hotel_id):
        query = self._SELECT_QUARTOS_BY_HOTEL
        with self.connection.cursor() as cursor:
            cursor.execute(query, (hotel_id,))
            results = cursor.fetchall()
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Quarto(**i) for i in results]
            return results
