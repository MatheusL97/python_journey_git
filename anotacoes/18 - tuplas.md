# 📚 ANOTACOES.md

# 📚 Aula 15 - Tuplas (Tuple)

## 🎯 Objetivo

Aprender o que são tuplas, quando utilizá-las e quais são as diferenças em relação às listas.

---

# O que é uma Tupla?

Uma tupla é uma estrutura de dados utilizada para armazenar vários valores.

Sua principal característica é ser **imutável**, ou seja, depois de criada seus elementos não podem ser alterados.

---

# Sintaxe

```python
frutas = ("Maçã", "Banana", "Laranja")
```

Enquanto uma lista utiliza colchetes:

```python
frutas = ["Maçã", "Banana", "Laranja"]
```

A tupla utiliza parênteses.

---

# Diferenças entre Lista e Tupla

| Lista | Tupla |
|--------|--------|
| [] | () |
| Mutável | Imutável |
| append() | Não possui |
| pop() | Não possui |
| remove() | Não possui |

---

# Acessando elementos

```python
cores = ("Azul", "Verde", "Vermelho")

print(cores[0])
print(cores[-1])
```

Resultado:

```
Azul
Vermelho
```

---

# Percorrendo uma tupla

```python
cores = ("Azul", "Verde", "Vermelho")

for cor in cores:
    print(cor)
```

---

# Descobrindo a quantidade de elementos

```python
len(cores)
```

---

# Quando utilizar Tuplas?

Utilize quando os dados não devem ser alterados.

Exemplos:

- Dias da semana
- Meses do ano
- Estados brasileiros
- Coordenadas
- Configurações fixas

---

# Boas práticas

✔ Utilize listas para dados que mudam.

✔ Utilize tuplas para dados fixos.

✔ Evite modificar informações que não precisam ser alteradas.

---

# Aprendizados

Nesta aula aprendi:

- criar tuplas;
- acessar elementos por índice;
- utilizar `for`;
- utilizar `len()`;
- identificar situações onde uma tupla é mais indicada que uma lista.