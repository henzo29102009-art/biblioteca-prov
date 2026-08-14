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
