import psycopg2


class Model:

    def __init__(self, id) -> None:
        self.id = id
        
    # create a connection
    def connect():
        conn = psycopg2.connect("dbname=mini_social_ddd user=postgres password=qazwsx")
        cursor = conn.cursor()
        return conn, cursor