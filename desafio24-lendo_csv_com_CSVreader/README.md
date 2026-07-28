# Aula 24 - Leitura de Arquivos CSV com csv.reader()

## Sobre

Neste desafio foi desenvolvido um programa capaz de ler um arquivo CSV utilizando a biblioteca `csv` do Python.

O programa percorre cada registro do arquivo e apresenta as informações de maneira organizada para o usuário.

---

## Funcionalidades

- importar a biblioteca `csv`;
- abrir um arquivo utilizando `with open()`;
- utilizar `csv.reader()`;
- definir o delimitador (`;`);
- percorrer todas as linhas do arquivo;
- exibir produto, preço e estoque.

---

## Estrutura do arquivo utilizado

```csv
Nome;Preco;Estoque
Notebook;1800.00;5
Mouse;80.00;20
Teclado;150.00;10
```

---

## Conceitos praticados

✔ Biblioteca `csv`

✔ `import csv`

✔ `with open()`

✔ `csv.reader()`

✔ `delimiter`

✔ `for`

✔ Listas

✔ Índices

✔ Leitura estruturada de dados

---

## Fluxo do programa

1. Importar a biblioteca `csv`.
2. Abrir o arquivo em modo leitura.
3. Criar o leitor com `csv.reader()`.
4. Percorrer cada linha do arquivo.
5. Exibir as informações organizadas.

---

## Aprendizados

Durante este desafio foi possível compreender como a biblioteca `csv` transforma cada linha do arquivo em uma lista, permitindo acessar cada coluna individualmente.

Esse conhecimento servirá como base para trabalhar futuramente com a biblioteca Pandas.

---

## Próximos passos

Nas próximas aulas serão estudados:

- ignorar o cabeçalho utilizando `next()`;
- `csv.DictReader`;
- escrita utilizando `csv.writer`;
- introdução ao Pandas.

---

## Python Journey

Projeto desenvolvido durante minha jornada de estudos em Python com foco em desenvolvimento e Análise de Dados.

---

## Status

✅ Desafio concluído com sucesso.