# 📚 ANOTACOES.md

# Aula 26 - Convertendo dados e realizando cálculos

## Objetivo

Aprender a converter dados lidos de um arquivo CSV para seus tipos corretos, permitindo realizar cálculos matemáticos.

---

# Os dados do CSV

Ao ler um arquivo CSV utilizando `csv.DictReader()`, todos os valores são lidos como texto (`str`).

Exemplo:

```python
linha["preço"]
```

Resultado:

```text
"29,68"
```

Mesmo parecendo um número, ele ainda é uma string.

---

# Convertendo o estoque

Como o estoque é um número inteiro:

```python
estoque = int(linha["estoque"])
```

Agora o tipo da variável passa a ser:

```python
<class 'int'>
```

---

# Convertendo o preço

Os preços do arquivo utilizam vírgula como separador decimal.

Antes:

```text
29,68
```

Primeiro substituímos a vírgula:

```python
preco = linha["preço"].replace(",", ".")
```

Resultado:

```text
29.68
```

Depois convertemos:

```python
preco = float(preco)
```

Agora:

```python
<class 'float'>
```

---

# Realizando cálculos

Depois da conversão podemos calcular normalmente.

Exemplo:

```python
valor_total = preco * estoque
```

---

# Somando valores

Para descobrir quanto vale todo o estoque da loja:

```python
valor_geral = 0
```

Dentro do laço:

```python
valor_geral += valor_total
```

---

# Contador

Também podemos contar quantos produtos existem.

```python
contador += 1
```

---

# Formatação de valores

Para exibir valores monetários:

```python
print(f"R$ {preco:.2f}")
```

---

# Conceitos aprendidos

Nesta aula aprendi:

- conversão de string para int;
- conversão de string para float;
- replace();
- cálculos matemáticos com dados do CSV;
- acumuladores;
- contadores;
- formatação de valores monetários.