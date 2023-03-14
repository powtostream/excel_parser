import sqlite3


class DbConnector(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def execute(self, sql_script):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute(sql_script)
            connection.commit()
            cursor.close()
            print("Successfully executed")

        except sqlite3.Error as error:
            print("Database error", error)

        finally:
            if (connection):
                connection.close()
                print("Connection closed")

    def insert_values(self, values):
        sql_script = "INSERT INTO qliq_qoil (company_name, 'date', " \
                     "calc_type, qliq, qoil) VALUES (?,?,?,?,?) "
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.executemany(sql_script, values)
            connection.commit()
            cursor.close()
            print("Successfully executed")

        except sqlite3.Error as error:
            print("Database error", error)

        finally:
            if (connection):
                connection.close()
                print("Connection closed")
