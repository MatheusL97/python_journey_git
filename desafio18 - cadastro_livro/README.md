# 🚀 README.md

# Desafio 18 - Cadastro de Livro com Dicionários

## 📖 Sobre

Neste desafio foi desenvolvido um sistema simples para cadastrar um livro utilizando dicionários.

O usuário informa os dados do livro, que são armazenados em um único dicionário. Em seguida, todas as informações são exibidas através de uma função.

---

## Funcionalidades

- Cadastro de título
- Cadastro de autor
- Cadastro de editora
- Cadastro do ano
- Cadastro da quantidade de páginas
- Cadastro do gênero
- Exibição automática de todas as informações

---

## Conceitos praticados

✔ Dicionários (`dict`)

✔ Chave e valor

✔ Funções

✔ Parâmetros

✔ `.items()`

✔ `for`

✔ `capitalize()`

✔ Tipos de dados (`int` e `str`)

---

## Estrutura do programa

O programa foi dividido em três etapas.

### 1. Coleta dos dados

O usuário informa todas as informações do livro utilizando `input()`.

---

### 2. Criação do dicionário

```python
livro = {
    "titulo": titulo,
    "autor": autor,
    "editora": editora,
    "ano": ano,
    "paginas": pagina,
    "genero": genero
}
```

Todas as informações ficam organizadas em um único objeto.

---

### 3. Exibição dos dados

Foi criada uma função responsável por mostrar o cadastro.

```python
def livro_cadastrado(livro):
```

A função recebe o dicionário como parâmetro e percorre todas as informações utilizando:

```python
for chave, valor in livro.items():
```

---

## Exemplo de saída

```
===== LIVRO CADASTRADO =====

Titulo: Dom Casmurro

Autor: Machado de Assis

Editora: Globo

Ano: 1899

Paginas: 256

Genero: Romance
```

---

## Aprendizados

Durante este desafio foi possível compreender como os dicionários representam cadastros de forma organizada.

Também foi praticado o uso de funções para separar responsabilidades e do método `.items()` para percorrer todas as informações automaticamente.

---

## Python Journey

Este desafio faz parte da Python Journey, cujo objetivo é consolidar cada novo conceito através de desafios práticos e progressivos.

---

## Status

✅ Desafio concluído com sucesso.