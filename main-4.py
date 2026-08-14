from dados import livros, salvar_livros


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
