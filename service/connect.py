import psycopg2


class Connect:

    def __init__(self):
        config = dict(
            dbname="sistema_reserva_hotel",
            user="postgres", password="1532",
            host="localhost", port="5432"
        )
        self._connection = psycopg2.connect(**config)

    def create_tables(self):

        cursor = self._connection.cursor()
        from modules.hospede.dao import DAOHospede
        cursor.execute(DAOHospede().create_table())

        from modules.hotel.dao import DAOHotel
        cursor.execute(DAOHotel().create_table())

        from modules.quarto.dao import DAOQuarto
        cursor.execute(DAOQuarto().create_table())

        from modules.reserva.dao import DAOReserva
        cursor.execute(DAOReserva().create_table())

        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection

    def init_database(self, version='v1'):
        if version == 'v1':
            self.create_tables()
        if version == 'v2':
            self.update_database()

    def update_database(self):
        pass