# crud.py

from db import get_connection
from models import Venda
from mysql.connector import Error

def criar_venda(venda: Venda):
    conexao = get_connection()
    if conexao is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        with conexao.cursor() as cursor:
            sql = "INSERT INTO vendas (nome_produto, valor_produto) VALUES (%s, %s)"
            valores = (venda.nome_produto, venda.valor_produto)
            cursor.execute(sql, valores)
            conexao.commit()
            print(f"Venda '{venda.nome_produto}' inserida com sucesso com ID {cursor.lastrowid}.")
    except Error as e:
        print(f"Erro ao inserir venda: {e}")
    finally:
        conexao.close()

def ler_vendas():
    conexao = get_connection()
    if conexao is None:
        print("Não foi possível conectar ao banco de dados.")
        return []

    vendas = []
    try:
        with conexao.cursor() as cursor:
            sql = "SELECT id_venda, nome_produto, valor_produto FROM vendas"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for row in resultados:
                venda = Venda(id_venda=row[0], nome_produto=row[1], valor_produto=row[2])
                vendas.append(venda)
    except Error as e:
        print(f"Erro ao ler vendas: {e}")
    finally:
        conexao.close()
    
    return vendas

def atualizar_venda(venda: Venda):
    if venda.id_venda is None:
        print("ID da venda é necessário para atualização.")
        return

    conexao = get_connection()
    if conexao is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        with conexao.cursor() as cursor:
            sql = "UPDATE vendas SET nome_produto = %s, valor_produto = %s WHERE id_venda = %s"
            valores = (venda.nome_produto, venda.valor_produto, venda.id_venda)
            cursor.execute(sql, valores)
            conexao.commit()
            if cursor.rowcount:
                print(f"Venda ID {venda.id_venda} atualizada com sucesso.")
            else:
                print(f"Nenhuma venda encontrada com ID {venda.id_venda}.")
    except Error as e:
        print(f"Erro ao atualizar venda: {e}")
    finally:
        conexao.close()

def deletar_venda(venda_id: int):
    conexao = get_connection()
    if conexao is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        with conexao.cursor() as cursor:
            sql = "DELETE FROM vendas WHERE id_venda = %s"
            valores = (venda_id,)
            cursor.execute(sql, valores)
            conexao.commit()
            if cursor.rowcount:
                print(f"Venda ID {venda_id} deletada com sucesso.")
            else:
                print(f"Nenhuma venda encontrada com ID {venda_id}.")
    except Error as e:
        print(f"Erro ao deletar venda: {e}")
    finally:
        conexao.close()
