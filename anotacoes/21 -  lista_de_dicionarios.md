# 📚 ANOTACOES.md

# 📚 Aula 18 - Listas de Dicionários

## 🎯 Objetivo

Aprender a armazenar vários dicionários dentro de uma lista, permitindo criar cadastros com múltiplos registros.

---

# Lista de dicionários

Uma lista pode armazenar vários dicionários.

Exemplo:

```python
alunos = [
    {"nome": "Carlos", "idade": 20},
    {"nome": "Maria", "idade": 22}
]
```

Cada posição da lista representa um cadastro.

---

# Criando uma lista vazia

```python
alunos = []
```

---

# Criando um dicionário

```python
novo_aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}
```

---

# Adicionando na lista

```python
alunos.append(novo_aluno)
```

Sempre que um novo aluno for cadastrado, ele será adicionado ao final da lista.

---

# Percorrendo uma lista de dicionários

```python
for aluno in alunos:
    print(aluno)
```

---

# Percorrendo um dicionário

```python
for chave, valor in aluno.items():
    print(chave, valor)
```

---

# Utilizando dois laços

Primeiro:

Cadastrar os alunos.

Segundo:

Exibir todos os alunos cadastrados.

Essa separação deixa o código mais organizado.

---

# Descobrindo a quantidade de alunos

```python
len(alunos)
```

Exemplo:

```python
print(len(alunos))
```

---

# Boa prática

Quando a variável do `for` não será utilizada:

```python
for _ in range(3):
```

O caractere `_` indica que a variável existe apenas para controlar a repetição.

---

# Estrutura utilizada

```
Lista
│
├── Dicionário 1
├── Dicionário 2
├── Dicionário 3
```

Essa estrutura é muito utilizada em APIs, bancos de dados e bibliotecas como Pandas.

---

# Aprendizados

Nesta aula aprendi:

- criar listas de dicionários;
- cadastrar vários registros;
- utilizar `.append()`;
- percorrer listas com `for`;
- percorrer dicionários com `.items()`;
- utilizar `len()` para contar registros;
- compreender uma das estruturas mais utilizadas no desenvolvimento Python.