# 🔍 CODE_REVIEW.md

# Aula 28 - Produto mais caro e mais barato

## Avaliação Geral

⭐ Nota: **10 / 10**

Excelente trabalho.

O programa percorre o arquivo apenas uma vez e identifica corretamente:

- produto mais caro;
- produto mais barato;
- diferença entre os preços.

---

# Pontos positivos

## ✔ Organização

As variáveis de referência foram corretamente inicializadas antes do laço.

```python
maior_preco = None
produto_mais_caro = ""

menor_preco = None
produto_mais_barato = ""
```

---

## ✔ Tratamento do preço

```python
preco = linha["preço"].replace(",", ".")
preco = float(preco)
```

Conversão correta para comparação numérica.

---

## ✔ Comparação do maior preço

```python
if maior_preco is None or preco > maior_preco:
```

Lógica correta.

---

## ✔ Comparação do menor preço

```python
if menor_preco is None or preco < menor_preco:
```

Boa utilização de dois `if`, permitindo que ambas as verificações sejam executadas de forma independente.

---

## ✔ Desafio extra

O cálculo da diferença foi implementado corretamente.

```python
diferenca = maior_preco - menor_preco
```

---

# Evolução observada

Durante o desenvolvimento ocorreu um erro importante: as variáveis estavam sendo inicializadas dentro do laço.

Após investigação, o problema foi identificado e corrigido.

Esse processo fortaleceu o entendimento sobre escopo e tempo de vida das variáveis.

---


# Conceitos consolidados

Durante esta aula foram reforçados:

- leitura de CSV;
- tratamento de strings;
- conversão para float;
- busca pelo maior valor;
- busca pelo menor valor;
- cálculo de diferença;
- reutilização de algoritmos;
- organização do código.

---

# Comentário do professor

Esta aula consolidou um padrão muito importante da programação: reutilizar algoritmos.

O aluno demonstrou compreender que a mesma lógica utilizada para encontrar o maior estoque pode ser aplicada para descobrir o maior preço, alterando apenas a variável utilizada na comparação.

Além disso, identificou e corrigiu sozinho um erro relacionado à inicialização das variáveis dentro do laço, demonstrando evolução no raciocínio lógico e na capacidade de depuração (debugging).

Parabéns pelo excelente desempenho!