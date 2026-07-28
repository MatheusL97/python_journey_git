# 🚀 README.md

# Aula 25 - Lendo um CSV com DictReader

## Sobre

Neste desafio foi desenvolvido um programa capaz de ler um arquivo CSV utilizando a classe `csv.DictReader()`.

Ao contrário do `csv.reader()`, cada linha do arquivo é transformada em um dicionário, permitindo acessar os dados através do nome das colunas.

Também foi implementado um contador para informar a quantidade de produtos existentes no arquivo.

---

## Funcionalidades

- importar a biblioteca csv;
- abrir um arquivo CSV;
- utilizar `csv.DictReader()`;
- acessar informações pelo nome das colunas;
- listar todos os produtos;
- contabilizar os registros.

---

## Estrutura do arquivo

```csv
nome;preço;estoque
Arroz Tipo 1 5kg;29,68;11
Feijão Preto 1kg;34,02;67
...
```

---

## Fluxo do programa

1. Importar a biblioteca csv.
2. Abrir o arquivo.
3. Criar um DictReader.
4. Percorrer todos os registros.
5. Exibir produto, preço e estoque.
6. Contar os produtos.
7. Exibir o total ao final.

---

## Conceitos praticados

✔ csv.DictReader()

✔ Dicionários

✔ with open()

✔ encoding utf-8-sig

✔ delimiter

✔ Estrutura for

✔ Contador

---

## Aprendizados

Durante este desafio foi possível compreender como o `DictReader()` torna a leitura de arquivos CSV mais organizada e intuitiva, eliminando a necessidade de acessar colunas por índices.

Também foi possível aprender a utilizar o `encoding="utf-8-sig"` para evitar problemas com arquivos contendo BOM.

---

## Próximos passos

Na próxima aula aprenderemos a converter os dados do CSV para os tipos corretos, transformando preços em números decimais e estoques em números inteiros, preparando a base para cálculos e análises.

---

## Python Journey

Projeto desenvolvido durante minha jornada de estudos em Python com foco em Desenvolvimento e Análise de Dados.

---

## Status

✅ Desafio concluído com sucesso.