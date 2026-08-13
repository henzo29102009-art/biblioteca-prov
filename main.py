import csv
import os

ARQUIVO = "livros.csv"

livros = []

def carregar_livros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                livros.append(linha)

def salvar_livros():
    with open(ARQUIVO, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        for livro in livros:
            escritor.writerow(livro)

def cadastrar_livro():
    print("Cadastrar livro")

    titulo = input("Título: ")
    autor = input("Autor: ")
    codigo = input("Código: ")
    ano = input("Ano: ")

    for livro in livros:
        if livro[2] == codigo:
            print("Esse código já está cadastrado!")
            return

    livros.append([titulo, autor, codigo, ano, "disponível"])
    salvar_livros()

    print("Livro cadastrado com sucesso!")

def listar_livros():
    print("\nLista de livros:")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print("Título:", livro[0])
        print("Autor:", livro[1])
        print("Código:", livro[2])
        print("Ano:", livro[3])
        print("Status:", livro[4])
        print("----------------")

def emprestar_livro():
    codigo = input("Digite o código do livro: ")

    for livro in livros:
        if livro[2] == codigo:
            if livro[4] == "emprestado":
                print("Esse livro já está emprestado!")
                return

            livro[4] = "emprestado"
            salvar_livros()
            print("Empréstimo realizado com sucesso!")
            return

    print("Livro não encontrado.")

def devolver_livro():
    codigo = input("Digite o código do livro: ")

    for livro in livros:
        if livro[2] == codigo:
            livro[4] = "disponível"
            salvar_livros()
            print("Livro devolvido com sucesso!")
            return

    print("Livro não encontrado.")

def buscar_livro():
    termo = input("Digite o título ou autor: ").lower()

    for livro in livros:
        if termo in livro[0].lower() or termo in livro[1].lower():
            print("Título:", livro[0])
            print("Autor:", livro[1])
            print("Código:", livro[2])
            print("Ano:", livro[3])
            print("Status:", livro[4])
            print("----------------")

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