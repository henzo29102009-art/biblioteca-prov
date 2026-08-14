from dados import carregar_livros
from cadastro import cadastrar_livro, listar_livros
from emprestimo import emprestar_livro, devolver_livro, buscar_livro


def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros")
        print("5 - Buscar livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            emprestar_livro()
        elif opcao == "3":
            devolver_livro()
        elif opcao == "4":
            listar_livros()
        elif opcao == "5":
            buscar_livro()
        elif opcao == "6":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")


carregar_livros()
menu()
