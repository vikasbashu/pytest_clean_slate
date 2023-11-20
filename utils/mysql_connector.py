import mysql.connector
from mysql.connector import Error
import pandas as pd


class Connection:
    connection = None

    def __init__(self, host_name=None, user_name=None, password=None, database=None, auth_plugin=None):
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=password,
                database=database,
                auth_plugin=auth_plugin
            )
        except Error as e:
            print(f"Error: {e}")
        else:
            print("Connection established")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except Error as e:
            print(f"Error: {e}")
        else:
            print("Query is executed successfully")

    @staticmethod
    def display_in_panda_table(output, headers):
        return pd.DataFrame(output, columns=headers)

    @classmethod
    def commit(cls):
        cls.connection.commit()
