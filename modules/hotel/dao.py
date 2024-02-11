from modules.hotel.sql import SQLHotel
from modules.hotel.modelo import Hotel

class DAOHotel(SQLHotel):
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
        results = [Hotel(**i) for i in results]
        return results

    def criar(self, hotel: Hotel):
        query = self._INSERT
        cursor = self.connection.cursor()
        cursor.execute(query, (
            hotel.nome,
            hotel.rua,
            hotel.bairro,
            hotel.cidade
        ))
        self.connection.commit()
        return hotel

    def delete_hotel_by_id(self, id):
        query = self._DELETE_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        self.connection.commit()


    def get_by_id(self, id):
        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            hotel_dict = dict(zip(cols, result))
            return Hotel(**hotel_dict)
        else:
            return None

    def update_hotel(self, hotel: Hotel):
        query = self._UPDATE_HOTEL
        cursor = self.connection.cursor()
        cursor.execute(query, (
            hotel.nome,
            hotel.rua,
            hotel.bairro,
            hotel.cidade,
            hotel.id
        ))
        self.connection.commit()
