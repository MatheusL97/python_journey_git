# 📚 ANOTACOES.md

# Aula 25 - Lendo arquivos CSV com csv.DictReader()

## Objetivo

Aprender a utilizar o `csv.DictReader()`, permitindo acessar os dados pelo nome das colunas em vez dos índices.

---

# O que é o DictReader?

O `DictReader` é uma classe da biblioteca `csv` que transforma cada linha do arquivo em um dicionário.

Exemplo de um arquivo CSV:

```csv
nome;preço;estoque
Arroz;29,90;10
Feijão;9,50;20
```

Ao utilizar o `csv.DictReader()`, cada linha será convertida em:

```python
{
    "nome": "Arroz",
    "preço": "29,90",
    "estoque": "10"
}
```

---

# Sintaxe

```python
import csv

with open("arquivo.csv", "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
```

---

# Acessando os dados

Com `csv.reader()`:

```python
linha[0]
linha[1]
linha[2]
```

Com `DictReader()`:

```python
linha["nome"]
linha["preço"]
linha["estoque"]
```

Muito mais legível.

---

# Vantagens

- código mais organizado;
- leitura mais intuitiva;
- elimina o uso de índices;
- facilita manutenção;
- muito utilizado em projetos profissionais.

---

# O cabeçalho

O `DictReader` utiliza automaticamente a primeira linha do arquivo como nome das chaves.

Por isso **não utilizamos**:

```python
next(leitor)
```

Caso seja utilizado, o primeiro registro será ignorado.

---

# UTF-8 com BOM

Alguns arquivos CSV possuem um caractere invisível chamado BOM.

Para evitar erros como:

```
KeyError: 'nome'
```

utilizamos:

```python
encoding="utf-8-sig"
```

Essa prática é recomendada principalmente para arquivos exportados do Excel.

---

# Contador

Podemos contar os registros utilizando:

```python
contador = 0

for linha in leitor:
    contador += 1
```

---

# Conceitos aprendidos

Nesta aula aprendi:

- csv.DictReader();
- leitura por nome das colunas;
- uso automático do cabeçalho;
- diferença entre reader() e DictReader();
- encoding utf-8-sig;
- contador de registros.