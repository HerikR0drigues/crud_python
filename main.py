# main.py

from models import Venda
import crud
import utils

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n=== Sistema CRUD de Vendas ===")
    print("1. Criar nova venda")
    print("2. Listar todas as vendas")
    print("3. Atualizar uma venda")
    print("4. Deletar uma venda")
    print("5. Sair")

def main():
    """
    Função principal que executa o loop do menu.
    """
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-5): ").strip()

        if escolha == '1':
            print("\n=== Criar Nova Venda ===")
            nome = utils.obter_nome_produto()
            valor = utils.obter_valor_produto()
            venda = Venda(nome_produto=nome, valor_produto=valor)
            crud.criar_venda(venda)

        elif escolha == '2':
            print("\n=== Listar Todas as Vendas ===")
            vendas = crud.ler_vendas()
            if vendas:
                print(f"\n{'ID':<5} {'Produto':<40} {'Valor':<10}")
                print("-" * 55)
                for venda in vendas:
                    print(f"{venda.id_venda:<5} {venda.nome_produto:<40} {venda.valor_produto:<10.2f}")
            else:
                print("Nenhuma venda encontrada.")

        elif escolha == '3':
            print("\n=== Atualizar Venda ===")
            venda_id = utils.obter_id_venda()
            nome = utils.obter_nome_produto()
            valor = utils.obter_valor_produto()
            venda = Venda(id_venda=venda_id, nome_produto=nome, valor_produto=valor)
            crud.atualizar_venda(venda)

        elif escolha == '4':
            print("\n=== Deletar Venda ===")
            venda_id = utils.obter_id_venda()
            confirmacao = input(f"Tem certeza que deseja deletar a venda ID {venda_id}? (s/n): ").strip().lower()
            if confirmacao == 's':
                crud.deletar_venda(venda_id)
            else:
                print("Operação cancelada.")

        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()
