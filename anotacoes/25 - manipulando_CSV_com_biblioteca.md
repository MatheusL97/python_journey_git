# 📚 ANOTACOES.md

# Aula 23 - Manipulando Arquivos CSV com a Biblioteca csv

## Objetivo

Aprender a utilizar a biblioteca `csv` para ler arquivos CSV de forma organizada, separando automaticamente as colunas dos registros.

---

# O que é a biblioteca csv?

A biblioteca `csv` faz parte da biblioteca padrão do Python e permite ler e escrever arquivos CSV de maneira simples.

Não é necessário instalar.

Basta importar:

```python
import csv
```

---

# O que é um CSV?

CSV significa:

> Comma-Separated Values

É um arquivo utilizado para armazenar dados organizados em linhas e colunas.

Exemplo:

```
Nome;Preco;Estoque
Notebook;1800.00;5
Mouse;80.00;20
```

Cada linha representa um registro.

Cada coluna representa uma informação.

---

# Abrindo um arquivo CSV

Utilizamos:

```python
with open("produtos.csv", "r", encoding="utf-8") as arquivo:
```

O `with` fecha o arquivo automaticamente ao final da leitura.

É considerado uma boa prática.

---

# csv.reader()

Depois de abrir o arquivo:

```python
leitor = csv.reader(arquivo, delimiter=";")
```

O parâmetro `delimiter` informa qual caractere separa as colunas.

No Brasil normalmente utilizamos:

```
;
```

---

# Percorrendo os registros

```python
for linha in leitor:
```

Cada linha passa a ser uma lista.

Exemplo:

```python
['Notebook', '1800.00', '5']
```

---

# Acessando os dados

Como a linha é uma lista:

```python
linha[0]
```

Produto

```python
linha[1]
```

Preço

```python
linha[2]
```

Estoque

---

# Exibindo informações

Podemos utilizar:

```python
print(f"Produto: {linha[0]}")
print(f"Preço: {linha[1]}")
print(f"Estoque: {linha[2]}")
```

---

# Vantagens da biblioteca csv

- leitura automática das colunas;
- código mais organizado;
- evita separações manuais;
- funciona perfeitamente com arquivos do Excel;
- preparação para utilizar Pandas.

---

# Diferença entre open() e with open()

## open()

É necessário fechar o arquivo manualmente.

```python
arquivo.close()
```

---

## with open()

Fecha automaticamente.

Mais seguro.

Mais utilizado profissionalmente.

---

# Relação com Pandas

O Pandas utiliza a mesma ideia de leitura estruturada.

A diferença é que ele oferece diversos recursos para análise de dados.

---

# Conceitos aprendidos

Nesta aula aprendi:

- importar a biblioteca csv;
- utilizar csv.reader();
- utilizar delimiter;
- utilizar with open();
- acessar colunas utilizando índices;
- ler arquivos CSV de forma profissional;
- preparar arquivos para futuras análises de dados.