# 📚 ANOTACOES.md

# Aula 27 - Encontrando o maior e o menor valor

## Objetivo

Aprender a percorrer um arquivo CSV para encontrar automaticamente:

- maior valor;
- menor valor;
- registro correspondente.

---

# O problema

Quando trabalhamos com arquivos CSV, normalmente não sabemos onde está a informação que procuramos.

Por exemplo:

- Qual produto possui o maior estoque?
- Qual possui o menor estoque?

Precisamos analisar todos os registros.

---

# Variáveis de referência

Antes do laço, criamos variáveis para armazenar os valores encontrados.

```python
maior_estoque = None
produto_maior = ""

menor_estoque = None
produto_menor = ""
```

Inicializamos com `None` porque ainda não existe nenhum valor para comparar.

---

# Comparando valores

Dentro do `for`, convertemos o estoque para inteiro:

```python
estoque = int(linha["estoque"])
```

Depois verificamos:

```python
if maior_estoque is None or estoque > maior_estoque:
    maior_estoque = estoque
    produto_maior = linha["nome"]
```

Se encontrarmos um valor maior, atualizamos a referência.

---

# Encontrando o menor valor

A lógica é exatamente a mesma.

Apenas trocamos o operador:

```python
if menor_estoque is None or estoque < menor_estoque:
    menor_estoque = estoque
    produto_menor = linha["nome"]
```

---

# Por que usar dois IF?

As verificações são independentes.

Um mesmo registro pode ser, ao mesmo tempo:

- o maior até agora;
- o menor até agora.

Por isso utilizamos dois `if` e não `elif`.

---

# Estrutura geral

```python
for linha in leitor:

    if condição_maior:
        atualizar_maior()

    if condição_menor:
        atualizar_menor()
```

---

# Aplicações

Esse algoritmo é utilizado para descobrir:

- maior salário;
- menor salário;
- maior venda;
- menor venda;
- produto mais caro;
- produto mais barato;
- aluno com maior nota;
- maior temperatura;
- menor temperatura.

---

# Conceitos aprendidos

- comparação de valores;
- variáveis de referência;
- uso de `None`;
- busca do maior elemento;
- busca do menor elemento;
- comparação utilizando `>` e `<`;
- lógica de análise de dados.