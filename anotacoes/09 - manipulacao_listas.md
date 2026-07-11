# 📚 Aula 09 - Manipulação de Listas

## 🎯 Objetivo

Aprender a manipular listas em Python utilizando os principais métodos disponíveis.

Nesta aula foram apresentados recursos que permitem alterar, inserir, remover, organizar e verificar elementos dentro de uma lista.

---

# 📖 Revisando

Uma lista permite armazenar diversos valores em uma única variável.

Exemplo:

```python
frutas = ["Maçã", "Banana", "Laranja"]
```

Cada elemento possui um índice.

| Índice | Valor |
|--------|--------|
| 0 | Maçã |
| 1 | Banana |
| 2 | Laranja |

---

# ✏️ Alterando elementos

Podemos alterar um elemento utilizando seu índice.

Exemplo:

```python
frutas[1] = "Uva"
```

Resultado:

```python
["Maçã", "Uva", "Laranja"]
```

---

# ➕ Inserindo elementos

Para inserir um elemento em uma posição específica utilizamos:

```python
insert()
```

Exemplo:

```python
frutas.insert(0, "Abacaxi")
```

Resultado:

```python
["Abacaxi", "Maçã", "Banana", "Laranja"]
```

Todos os elementos são deslocados para a direita.

---

# ➖ Removendo elementos pelo valor

Podemos remover um elemento informando seu valor.

Exemplo:

```python
frutas.remove("Banana")
```

Resultado:

```python
["Maçã", "Laranja"]
```

---

# 🗑️ Removendo elementos pelo índice

Também podemos remover um elemento informando sua posição.

Exemplo:

```python
frutas.pop(1)
```

Resultado:

```python
["Maçã", "Laranja"]
```

O elemento removido foi o da posição 1.

---

# 🔍 Verificando se um elemento existe

Podemos verificar se um valor está presente na lista utilizando o operador:

```python
in
```

Exemplo:

```python
if "Maçã" in frutas:
    print("Produto encontrado.")
```

---

# 📋 Organizando uma lista

Para ordenar uma lista utilizamos:

```python
sort()
```

Exemplo:

```python
frutas.sort()
```

Resultado:

```python
["Banana", "Laranja", "Maçã"]
```

A ordenação é feita em ordem alfabética.

---

# 📝 Métodos estudados

| Método | Função |
|---------|--------|
| append() | Adiciona no final |
| insert() | Insere em uma posição |
| remove() | Remove pelo valor |
| pop() | Remove pelo índice |
| sort() | Ordena a lista |
| in | Verifica se um elemento existe |

---

# 💡 Boas práticas

- Utilize nomes claros para as listas.
- Evite criar listas desnecessárias.
- Sempre pense se deseja remover pelo valor (`remove`) ou pela posição (`pop`).
- Utilize `sort()` apenas quando desejar alterar a ordem da lista.

---

# 🚫 Erros comuns

## Confundir índice com valor

Errado:

```python
frutas.remove(1)
```

Isso tenta remover o valor `1`, e não o elemento da posição 1.

Para remover pela posição utilize:

```python
frutas.pop(1)
```

---

## Acessar uma posição inexistente

```python
frutas[10]
```

Se essa posição não existir, o Python gerará um erro.

---

# 🧠 Resumo

Nesta aula aprendi:

- Alterar elementos.
- Inserir elementos em posições específicas.
- Remover elementos por valor.
- Remover elementos por índice.
- Ordenar listas.
- Verificar se um elemento existe.

---

# 🎯 Conclusão

As listas são uma das estruturas de dados mais importantes do Python.

Dominar sua manipulação é essencial para desenvolver programas mais organizados, eficientes e próximos de aplicações reais.

---

## 👨‍🏫 Anotação do professor

Nesta aula demos um passo importante.

Até agora aprendíamos apenas a armazenar informações.

Agora começamos a manipulá-las.

Grande parte dos sistemas desenvolvidos atualmente utiliza listas (ou estruturas semelhantes) para organizar dados.

Quanto mais confortável você estiver manipulando listas, mais fácil será aprender os próximos conteúdos, principalmente o laço `for`.