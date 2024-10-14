# db.py

import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Estabelece e retorna uma conexão com o banco de dados MySQL.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão.
    """
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1341',
            database='crud_python'
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida.")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
