from dados import livros, salvar_livros


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
