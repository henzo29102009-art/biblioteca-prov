Sistema de Gerenciamento de Biblioteca

Descrição

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python.

O programa permite cadastrar livros, realizar empréstimos e devoluções, listar o acervo, buscar livros por título ou autor e ordenar os livros.

Os dados são armazenados em uma lista de dicionários durante a execução e também são salvos no arquivo `livros.txt`, evitando que os livros cadastrados sejam perdidos quando o programa for encerrado.


⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

 1. Cadastrar livro

Permite cadastrar um novo livro informando:

- Título
- Autor
- Ano de publicação
- ISBN

Todo livro cadastrado começa com o status:

```text
Disponível
