from modules.quarto.sql import SQLQuarto
from modules.quarto.modelo import Quarto

class DAOQuarto(SQLQuarto):
    def __init__(self):
        from service.connect import Connect
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Quarto(**i) for i in results]
        return results