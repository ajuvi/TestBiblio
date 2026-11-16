
import mysql.connector


class DB:

    # Configuració
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_USER = "root"
    DB_PASSWORD = "toor"
    DB_NAME = "db_biblio"

    def __init__(self, transaccio=False):
        self.conn = None
        self.transaccio = transaccio
        self.connectar()

    # --------------------------------------------------
    # CONNEXIÓ
    # --------------------------------------------------

    def connectar(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host=self.DB_HOST,
                port=self.DB_PORT,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME
            )

        return self.conn

    def tancar(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

        self.conn = None

    # --------------------------------------------------
    # TRANSACCIONS
    # --------------------------------------------------

    def start_transaction(self):
        self.conn.start_transaction()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    # --------------------------------------------------
    # CONSULTES SELECT
    # --------------------------------------------------

    def execute_query(self, sql, params=None):
        cursor = None

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, params or ())
            return cursor.fetchall()

        except mysql.connector.Error as error:
            print(f"Error executant la consulta: {error}")
            raise

        finally:
            if cursor:
                cursor.close()

    # --------------------------------------------------
    # INSERT, UPDATE, DELETE
    # --------------------------------------------------

    def execute_update(self, sql, params=None):
        cursor = None

        try:
            if not self.transaccio:
                self.start_transaction()

            cursor = self.conn.cursor()
            cursor.execute(sql, params or ())

            files_afectades = cursor.rowcount

            if not self.transaccio:
                self.commit()

            return files_afectades

        except mysql.connector.Error:
            if not self.transaccio:
                self.rollback()
            raise

        finally:
            if cursor:
                cursor.close()
