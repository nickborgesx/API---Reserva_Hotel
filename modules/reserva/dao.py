from modules.reserva.sql import SQLReserva
from modules.reserva.modelo import Reserva

class DAOReserva(SQLReserva):
    _COL_ID = SQLReserva._COL_ID

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
        results = [Reserva(**i) for i in results]
        return results

    def criar(self, entrada, saida, valor, quarto_id, hospede_id, hotel_id):
        query = self._INSERT
        with self.connection.cursor() as cursor:
            cursor.execute(query, (entrada, saida, valor, quarto_id, hospede_id, hotel_id))
        self.connection.commit()

    def get_by_id(self, id):
        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            cols = [desc[0] for desc in cursor.description]
            quarto_dict = dict(zip(cols, result))
            return Reserva(**quarto_dict)
        else:
            return None

    def update_reserva(self, entrada, saida, valor, quarto_id, hospede_id, hotel_id, reserva_id):
        query = self._UPDATE_RESERVA
        with self.connection.cursor() as cursor:
            cursor.execute(query, (entrada, saida, valor, quarto_id, hospede_id, hotel_id, reserva_id))
        self.connection.commit()

    def delete_by_id(self, reserva_id):
        query = self._DELETE_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (reserva_id,))
        self.connection.commit()

    def get_reservas_by_quarto(self, quarto_id):
        query = self._SELECT_BY_QUARTO_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (quarto_id,))
        result = cursor.fetchall()

        reservas = []
        for row in result:
            reserva = Reserva(
                id=row[0],
                entrada=row[1],
                saida=row[2],
                valor=row[3],
                quarto_id=row[4],
                hospede_id=row[5],
                hotel_id=row[6]
            )
            reservas.append(reserva)

        return reservas

    def check_date_conflict(self, quarto_id, entrada, saida, exclude_reserva_id=None):
        query = self._SELECT_CREATE_VERIFIC

        with self.connection.cursor() as cursor:
            if exclude_reserva_id:
                cursor.execute(query, (entrada, quarto_id))
                existing_reserva = cursor.fetchone()

                if existing_reserva and existing_reserva[0] == exclude_reserva_id:
                    return False
                else:
                    cursor.execute(query, (entrada, quarto_id))
            else:
                cursor.execute(query, (entrada, quarto_id))

            result = cursor.fetchone()
            return result is not None

    def get_reservas_by_hotel(self, hotel_id):
        query = self._SELECT_HOTEL_ID
        with self.connection.cursor() as cursor:
            cursor.execute(query, (hotel_id,))
            results = cursor.fetchall()
            cols = [desc[0] for desc in cursor.description]
            results = [dict(zip(cols, i)) for i in results]
            results = [Reserva(**i) for i in results]
            return results

    def check_reserva_belongs_to_hotel(self, reserva_id, hotel_id):
        query = self._CHECK_RESERVA_BELONGS_TO_HOTEL
        with self.connection.cursor() as cursor:
            cursor.execute(query, (reserva_id, hotel_id))
            result = cursor.fetchone()
            return result[0] > 0