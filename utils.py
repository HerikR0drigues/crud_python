# utils.py

from models import Venda

def obter_nome_produto():
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if nome:
            return nome
        else:
            print("Nome do produto não pode estar vazio. Por favor, tente novamente.")

def obter_valor_produto():
    while True:
        valor_str = input("Digite o valor do produto: ").strip()
        try:
            valor = float(valor_str)
            if valor < 0:
                print("O valor do produto não pode ser negativo. Por favor, tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o valor do produto.")

def obter_id_venda():
    while True:
        id_str = input("Digite o ID da venda: ").strip()
        try:
            venda_id = int(id_str)
            if venda_id <= 0:
                print("O ID da venda deve ser um número positivo. Por favor, tente novamente.")
            else:
                return venda_id
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido para o ID da venda.")
