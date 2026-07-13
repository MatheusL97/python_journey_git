# 📚 Aula 12 - Escopo de Variáveis

## 🎯 Objetivo

Compreender o conceito de escopo em Python e aprender a utilizar parâmetros para tornar as funções independentes de variáveis globais.

---

# O que é escopo?

Escopo é a região do programa onde uma variável pode ser utilizada.

Existem dois tipos principais:

- Escopo Global
- Escopo Local

---

# Escopo Global

Uma variável criada fora de uma função pode ser utilizada dentro dela.

Exemplo:

```python
nome = "Matheus"

def mostrar():
    print(nome)
```

---

# Escopo Local

Uma variável criada dentro de uma função só existe dentro dela.

Exemplo:

```python
def mostrar():
    idade = 29

print(idade)
```

Resultado:

```
NameError
```

---

# Passando listas como parâmetro

Antes:

```python
lista_compras = []

def adicionar_produto():
    lista_compras.append("Arroz")
```

Depois:

```python
lista_compras = []

def adicionar_produto(lista):
    lista.append("Arroz")
```

Chamada:

```python
adicionar_produto(lista_compras)
```

---

# Vantagens

- Código mais organizado.
- Funções reutilizáveis.
- Menor dependência de variáveis globais.
- Facilita manutenção.
- Reduz erros.

---

# Aprendizados

Nesta aula aprendi:

- diferença entre variável global e local;
- como passar listas como parâmetro;
- por que evitar depender de variáveis globais;
- como tornar funções mais reutilizáveis.

---

## 👨‍🏫 Resumo

Sempre que possível, passe as informações que a função precisa através de parâmetros.

Isso deixa o código mais profissional e organizado.