# 📚 ANOTACOES.md

# Aula 24 - Ignorando o Cabeçalho com next()

## Objetivo

Aprender a ignorar automaticamente o cabeçalho de um arquivo CSV utilizando a função `next()`.

---

# O problema

Ao utilizar:

```python
for linha in leitor:
```

o Python percorre todas as linhas do arquivo, incluindo o cabeçalho.

Exemplo:

```
Nome;Preco;Estoque
Notebook;1800.00;5
Mouse;80.00;20
```

Saída:

```python
['Nome', 'Preco', 'Estoque']
['Notebook', '1800.00', '5']
['Mouse', '80.00', '20']
```

Na maioria das vezes não queremos processar o cabeçalho.

---

# A função next()

Utilizamos:

```python
next(leitor)
```

Ela lê a primeira linha do arquivo e avança o leitor para a próxima linha.

Após isso, o `for` inicia diretamente no primeiro registro de dados.

---

# Exemplo

```python
import csv

with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")

    next(leitor)

    for linha in leitor:
        print(linha)
```

Resultado:

```python
['Notebook', '1800.00', '5']
['Mouse', '80.00', '20']
```

---

# Importante

A função `next()` **não altera o arquivo**.

Ela apenas avança a posição atual da leitura.

O arquivo continua exatamente igual.

---

# Quando utilizar?

Sempre que o arquivo possuir um cabeçalho.

Exemplos:

- cadastro de clientes;
- estoque;
- vendas;
- funcionários;
- planilhas do Excel;
- relatórios exportados.

---

# Atenção

Se o arquivo não possuir cabeçalho e utilizarmos:

```python
next(leitor)
```

o primeiro registro será ignorado.

Por isso é importante conhecer a estrutura do arquivo antes da leitura.

---

# Contando registros

Uma forma simples de contar quantos registros foram processados é utilizando um contador.

```python
contador = 0

for linha in leitor:
    contador += 1
```

Depois:

```python
print(contador)
```

---

# Conceitos aprendidos

Nesta aula aprendi:

- utilizar `next()`;
- ignorar o cabeçalho de um CSV;
- contar registros utilizando contador;
- percorrer apenas os dados úteis;
- preparar arquivos para análise de dados.