# 🚀 README.md

# Aula 25 - Ignorando o Cabeçalho de um CSV

## Sobre

Neste desafio foi desenvolvido um programa capaz de ler um arquivo CSV utilizando a biblioteca `csv`, ignorando automaticamente o cabeçalho através da função `next()`.

Ao final da leitura, o programa também informa a quantidade de produtos encontrados.

---

## Funcionalidades

- importar a biblioteca `csv`;
- abrir arquivo utilizando `with open()`;
- criar um leitor com `csv.reader()`;
- ignorar o cabeçalho com `next()`;
- percorrer todos os registros;
- exibir produto, preço e estoque;
- contabilizar a quantidade de produtos.

---

## Estrutura do arquivo

```csv
Nome;Preco;Estoque
Notebook;1800.00;5
Mouse;80.00;20
Teclado;150.00;10
```

---

## Fluxo do programa

1. Importar a biblioteca `csv`.
2. Abrir o arquivo.
3. Criar o leitor.
4. Ignorar o cabeçalho utilizando `next()`.
5. Percorrer todos os registros.
6. Exibir as informações.
7. Contabilizar os produtos.
8. Mostrar o total ao final.

---

## Conceitos praticados

✔ Biblioteca `csv`

✔ `with open()`

✔ `csv.reader()`

✔ `delimiter`

✔ `next()`

✔ Contador

✔ Estruturas de repetição

✔ Listas

✔ Índices

---

## Aprendizados

Durante este desafio foi possível compreender como ignorar automaticamente o cabeçalho de um arquivo CSV, permitindo processar apenas os dados relevantes.

Também foi praticada a utilização de um contador para informar quantos registros foram lidos.

---

## Próximos passos

Na próxima aula serão estudados:

- `csv.DictReader`;
- acesso por nomes de colunas;
- leitura mais organizada de arquivos CSV.

---

## Python Journey

Projeto desenvolvido durante minha jornada de estudos em Python com foco em Desenvolvimento e Análise de Dados.

---

## Status

✅ Desafio concluído com sucesso.