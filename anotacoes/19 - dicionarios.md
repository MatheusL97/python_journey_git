# 📚 ANOTACOES.md

# 📚 Aula 19 - Dicionários (dict)

## 🎯 Objetivo

Aprender a utilizar dicionários para armazenar informações em formato de cadastro, utilizando pares de chave e valor.

---

# O que é um dicionário?

Um dicionário é uma estrutura de dados que armazena informações utilizando uma **chave** associada a um **valor**.

Exemplo:

```python
pessoa = {
    "nome": "Matheus",
    "idade": 29,
    "cidade": "Campinas"
}
```

---

# Sintaxe

Os dicionários são criados utilizando chaves `{}`.

```python
produto = {
    "nome": "Notebook",
    "preco": 3500,
    "marca": "Dell"
}
```

---

# Chave x Valor

```python
produto = {
    "nome": "Notebook"
}
```

Neste exemplo:

Chave:

```python
"nome"
```

Valor:

```python
"Notebook"
```

---

# Acessando informações

Para acessar um valor utilizamos sua chave.

```python
print(produto["nome"])
```

Resultado:

```
Notebook
```

---

# Adicionando informações

```python
produto["estoque"] = 10
```

---

# Alterando informações

```python
produto["preco"] = 4200
```

---

# Removendo informações

```python
del produto["marca"]
```

---

# Percorrendo um dicionário

Somente as chaves:

```python
for chave in produto:
    print(chave)
```

---

Chaves e valores:

```python
for chave, valor in produto.items():
    print(chave, valor)
```

---

# Método items()

O método `.items()` retorna simultaneamente:

- chave
- valor

Exemplo:

```python
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis"
}

for chave, valor in livro.items():
    print(chave, valor)
```

---

# capitalize()

O método `capitalize()` pode ser utilizado para deixar a primeira letra maiúscula.

```python
texto = "python"

print(texto.capitalize())
```

Resultado:

```
Python
```

Atenção:

`capitalize()` funciona apenas com **strings**.

Não pode ser utilizado em números.

---

# Quando utilizar dicionários?

Sempre que existir um cadastro.

Exemplos:

- Cliente
- Produto
- Funcionário
- Livro
- Carro
- Filme
- Pedido

---

# Comparação

| Lista | Tupla | Dicionário |
|--------|--------|------------|
| [] | () | {} |
| Índices | Índices | Chaves |
| Mutável | Imutável | Mutável |

---

# Boas práticas

✔ Utilizar nomes claros para as chaves.

✔ Armazenar cada informação utilizando sua própria chave.

✔ Utilizar funções para organizar a exibição das informações.

✔ Utilizar `.items()` quando precisar percorrer todo o cadastro.

---

# Aprendizados

Nesta aula aprendi:

- criar dicionários;
- acessar informações através das chaves;
- adicionar e alterar valores;
- percorrer um dicionário utilizando `.items()`;
- representar cadastros utilizando dicionários;
- utilizar funções para exibir informações de um cadastro.