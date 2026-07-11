# 🚀 Desafio 07 - Lista de Compras

## 📖 Sobre o desafio

Neste desafio, o objetivo foi desenvolver um sistema simples de lista de compras utilizando listas (`list`) em Python.

O programa permite adicionar produtos, visualizar todos os itens cadastrados e encerrar o sistema através de um menu interativo.

Durante o desenvolvimento foram utilizados conceitos estudados nas aulas anteriores, consolidando o aprendizado por meio de uma aplicação prática.

---

# 📚 Cenário

Imagine que você deseja criar um pequeno sistema para organizar uma lista de compras.

O usuário poderá adicionar quantos produtos desejar, consultar os itens cadastrados e encerrar o programa quando terminar.

---

# 🎯 Objetivos de aprendizagem

Durante este desafio pratiquei:

* Criação de listas
* Adição de elementos utilizando `append()`
* Verificação do tamanho da lista com `len()`
* Estruturas condicionais (`if`, `elif` e `else`)
* Estrutura de repetição `while`
* Utilização do comando `break`
* Organização da lógica de um menu

---

# 📋 Regras

O programa deverá apresentar o seguinte menu:

```text
====== LISTA DE COMPRAS ======

1 - Adicionar produto
2 - Ver lista
3 - Sair
```

### Opção 1

Solicitar o nome de um produto.

Adicionar o produto à lista utilizando o método:

```python
append()
```

Após isso, informar ao usuário que o produto foi cadastrado.

---

### Opção 2

Se houver produtos cadastrados, exibir a lista.

Caso contrário, mostrar uma mensagem informando que ainda não existem produtos cadastrados.

---

### Opção 3

Mostrar:

```text
Sistema encerrado.
```

Encerrar o programa utilizando:

```python
break
```

---

### Qualquer outra opção

Mostrar:

```text
Opção inválida.
```

Retornar ao menu principal.

---

# 💻 Exemplo de execução

```text
====== LISTA DE COMPRAS ======

1 - Adicionar produto
2 - Ver lista
3 - Sair

Digite uma opção: 1

O que deseja adicionar? Arroz

Produto adicionado com sucesso!

====== LISTA DE COMPRAS ======

1 - Adicionar produto
2 - Ver lista
3 - Sair

Digite uma opção: 2

['Arroz']
```

---

# 🧠 Planejamento (IPO)

## Input (Entrada)

* Opção escolhida pelo usuário.
* Nome do produto.

## Process (Processamento)

* Criar uma lista vazia.
* Exibir o menu.
* Ler a opção escolhida.
* Adicionar produtos utilizando `append()`.
* Verificar se existem itens cadastrados utilizando `len()`.
* Encerrar o programa quando solicitado.

## Output (Saída)

* Produto adicionado.
* Lista de produtos.
* Mensagem informando lista vazia.
* Sistema encerrado.
* Opção inválida.

---

# 📚 Conceitos utilizados

* Variáveis
* Listas (`list`)
* `append()`
* `len()`
* `print()`
* `input()`
* `while`
* `break`
* `if`
* `elif`
* `else`

---

# 📂 Estrutura do projeto

```text
desafio-07-lista-de-compras/
│
├── README.md
├── codigo.py
├── CODE_REVIEW.md
└── assets/
```

---

# 💭 Aprendizados

Neste desafio aprendi que listas permitem armazenar diversos valores em uma única variável.

Também compreendi que a lista deve ser criada antes do laço de repetição para que os dados permaneçam disponíveis durante toda a execução do programa.

Além disso, utilizei `append()` para adicionar novos elementos e `len()` para verificar se a lista possuía produtos cadastrados antes de exibi-la.

---

# 🚀 Próximos passos

Nos próximos desafios serão apresentados novos recursos da linguagem Python que permitirão manipular listas de forma ainda mais eficiente.

---

# 🐍 Python Journey

Este desafio faz parte da minha jornada de estudos em Python.

O objetivo deste repositório é registrar minha evolução como desenvolvedor, documentando cada aula, desafio e aprendizado adquirido ao longo dos estudos.

---

## 👨‍🏫 Mentoria

Este desafio foi desenvolvido seguindo uma metodologia baseada em:

* Planejamento antes da implementação.
* Resolução de problemas.
* Revisão de código (Code Review).
* Organização do projeto.
* Boas práticas de programação.

Cada desafio representa mais um passo na construção da minha base como futuro desenvolvedor Python.

---

**Status:** ✅ Concluído
