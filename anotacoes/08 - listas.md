# 📚 Aula 08 - Listas (`list`)

## 🎯 Objetivo

Aprender o que são listas em Python, como criar, acessar, modificar, adicionar e remover elementos.

As listas são uma das estruturas de dados mais importantes da linguagem e serão utilizadas em praticamente todos os projetos desenvolvidos durante a jornada.

---

# 🤔 O problema

Imagine um sistema escolar.

Precisamos armazenar os nomes de vários alunos.

Uma solução seria:

```python
aluno1 = "João"
aluno2 = "Maria"
aluno3 = "Pedro"
aluno4 = "Carlos"
```

Mas imagine uma escola com 2.000 alunos.

Criar milhares de variáveis seria inviável.

Foi para resolver esse problema que surgiram as listas.

---

# 📖 O que é uma lista?

Uma lista é uma estrutura capaz de armazenar vários valores em uma única variável.

Exemplo:

```python
alunos = ["João", "Maria", "Pedro", "Carlos"]
```

Agora todos os nomes estão armazenados dentro da variável `alunos`.

---

# 🔢 Índices (Index)

Cada elemento da lista possui uma posição.

Em Python, a contagem sempre começa em **0**.

Exemplo:

```text
Índice:

0        1        2        3

["João", "Maria", "Pedro", "Carlos"]
```

Portanto:

```python
alunos[0]
```

Resultado:

```text
João
```

---

# 📥 Acessando elementos

Podemos acessar qualquer posição utilizando seu índice.

Exemplo:

```python
print(alunos[0])
print(alunos[1])
print(alunos[2])
```

Saída:

```text
João
Maria
Pedro
```

---

# ✏️ Alterando elementos

Também podemos alterar um valor existente.

Exemplo:

```python
alunos[3] = "Ana"
```

Resultado:

```python
["João", "Maria", "Pedro", "Ana"]
```

---

# ➕ Adicionando elementos

Para adicionar novos elementos utilizamos o método:

```python
append()
```

Exemplo:

```python
alunos.append("Lucas")
```

Resultado:

```python
["João", "Maria", "Pedro", "Ana", "Lucas"]
```

O método `append()` sempre adiciona o novo elemento ao final da lista.

---

# ➖ Removendo elementos

Para remover um elemento utilizamos:

```python
remove()
```

Exemplo:

```python
alunos.remove("Maria")
```

Resultado:

```python
["João", "Pedro", "Ana", "Lucas"]
```

O método `remove()` procura o valor informado e o remove da lista.

---

# 📏 Descobrindo o tamanho da lista

Para descobrir quantos elementos existem utilizamos:

```python
len()
```

Exemplo:

```python
len(alunos)
```

Resultado:

```text
4
```

A função `len()` retorna a quantidade de elementos presentes na lista.

---

# 📌 Operações estudadas

| Operação                | Exemplo                   |
| ----------------------- | ------------------------- |
| Criar lista             | `lista = []`              |
| Criar com valores       | `lista = ["A", "B", "C"]` |
| Acessar elemento        | `lista[0]`                |
| Alterar elemento        | `lista[1] = "Novo"`       |
| Adicionar elemento      | `lista.append("Item")`    |
| Remover elemento        | `lista.remove("Item")`    |
| Quantidade de elementos | `len(lista)`              |

---

# 💡 Boas práticas

* Escolha nomes claros para as listas.

Exemplo:

```python
lista_compras
```

é melhor que:

```python
lista1
```

---

* Crie a lista antes de utilizá-la.

Exemplo:

```python
lista = []
```

---

* Utilize `append()` para adicionar novos elementos.

---

* Utilize `len()` para verificar se a lista possui elementos antes de exibi-la.

---

# 🚫 Erros comuns

### Criar a lista dentro do `while`

```python
while True:
    lista = []
```

Esse é um erro comum.

A lista será recriada a cada repetição e todos os dados serão perdidos.

O correto é:

```python
lista = []

while True:
```

---

### Acessar uma posição inexistente

Exemplo:

```python
lista = ["Python"]

print(lista[5])
```

Resultado:

Erro, pois a posição 5 não existe.

Sempre verifique os índices utilizados.

---

# 🧠 Resumo

Nesta aula aprendi:

* O que é uma lista.
* Como criar uma lista.
* Como acessar elementos.
* Como alterar elementos.
* Como adicionar novos itens com `append()`.
* Como remover itens com `remove()`.
* Como descobrir o tamanho da lista utilizando `len()`.

---

# 🎯 Conclusão

As listas permitem armazenar diversos valores em uma única variável, tornando os programas mais organizados, escaláveis e fáceis de manter.

Elas são uma das estruturas mais utilizadas em Python e servirão de base para diversos conteúdos futuros, como laços de repetição (`for`), funções e projetos completos.

---

## 👨‍🏫 Anotação do professor

As listas representam um dos primeiros contatos com estruturas de dados.

Dominar esse conceito é essencial, pois praticamente toda aplicação desenvolvida em Python manipula listas em algum momento.

Não tenha pressa em decorar todos os métodos. O mais importante agora é compreender o conceito e praticar bastante com pequenos desafios.

> **"Um bom programador não memoriza tudo. Ele entende como as ferramentas funcionam e sabe quando utilizá-las."**
