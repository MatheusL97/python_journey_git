# 📚 ANOTACOES.md

# Aula 28 - Encontrando o produto mais caro e o mais barato

## Objetivo

Aprender a identificar automaticamente:

- o produto mais caro;
- o produto mais barato;
- a diferença entre os preços.

---

# Relembrando

O algoritmo é praticamente o mesmo utilizado para encontrar:

- maior estoque;
- menor estoque.

A única diferença é que agora comparamos o preço.

---

# Tratando o preço

O preço no CSV vem como texto.

Exemplo:

29,68

Antes de comparar, precisamos converter:

```python
preco = linha["preço"].replace(",", ".")
preco = float(preco)
```

---

# Variáveis de referência

Antes do laço:

```python
maior_preco = None
produto_mais_caro = ""

menor_preco = None
produto_mais_barato = ""
```

Essas variáveis armazenam o resultado final da análise.

Por isso ficam fora do `for`.

---

# Comparando o maior preço

```python
if maior_preco is None or preco > maior_preco:
    maior_preco = preco
    produto_mais_caro = linha["nome"]
```

---

# Comparando o menor preço

```python
if menor_preco is None or preco < menor_preco:
    menor_preco = preco
    produto_mais_barato = linha["nome"]
```

As duas comparações são independentes.

Por isso utilizamos dois `if`.

---

# Calculando a diferença

Depois das comparações:

```python
diferenca = maior_preco - menor_preco
```

---

# Erro que aconteceu durante a aula

Inicialmente as variáveis estavam sendo criadas dentro do `for`.

Exemplo incorreto:

```python
for linha in leitor:

    maior_preco = None
    menor_preco = None
```

Isso fazia com que elas fossem reiniciadas a cada produto lido.

A solução foi mover as variáveis para antes do laço.

---

# Conceitos aprendidos

- replace()
- float()
- comparação de números decimais
- variáveis de referência
- busca pelo maior valor
- busca pelo menor valor
- cálculo de diferença
- reutilização de algoritmos

---

# Aplicações

Esse algoritmo pode ser utilizado para encontrar:

- produto mais caro;
- produto mais barato;
- maior salário;
- menor salário;
- maior nota;
- menor nota;
- maior faturamento;
- menor faturamento.