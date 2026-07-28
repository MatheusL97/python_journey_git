# 🔍 CODE_REVIEW.md

# Aula 25 - Lendo CSV com DictReader

## Avaliação Geral

⭐ Nota: **9,8 / 10**

Excelente trabalho!

O programa foi desenvolvido corretamente utilizando `csv.DictReader()`, demonstrando domínio dos conceitos apresentados na aula.

Foi identificado apenas um pequeno detalhe durante o desenvolvimento: a utilização de `next(leitor)` junto ao `DictReader()`, o que fazia o primeiro produto ser ignorado. Após a correção, o programa ficou totalmente adequado.

---

# Pontos positivos

## ✔ Importação da biblioteca

```python
import csv
```

Importação realizada corretamente.

---

## ✔ Uso do with open()

```python
with open("produtos_estoque.csv", "r", encoding="utf-8-sig") as arquivo:
```

Excelente prática.

Além do uso correto do `with`, foi utilizado o `utf-8-sig`, solucionando o problema causado pelo BOM do arquivo.

---

## ✔ Utilização do DictReader()

```python
leitor = csv.DictReader(arquivo, delimiter=";")
```

Implementação correta.

Cada linha passou a ser representada como um dicionário.

---

## ✔ Acesso às colunas

```python
linha["nome"]
linha["preço"]
linha["estoque"]
```

Muito mais legível que utilizar índices.

Essa abordagem é amplamente utilizada em projetos profissionais.

---

## ✔ Contador

```python
contador += 1
```

Boa utilização para contabilizar os produtos existentes.

---

## ✔ Organização da saída

As informações foram exibidas de forma clara e organizada, facilitando a leitura pelo usuário.

---

# Ajuste realizado

Inicialmente foi utilizado:

```python
next(leitor)
```

Como o `DictReader()` já utiliza automaticamente o cabeçalho do arquivo, essa instrução fazia com que o primeiro registro fosse ignorado.

Após a remoção dessa linha, o problema foi resolvido.

---

# Conceitos consolidados

Durante este desafio foram reforçados:

- csv.DictReader();
- dicionários;
- leitura por chave;
- encoding utf-8-sig;
- contador;
- estrutura for;
- manipulação de arquivos CSV.

---

# Comentário do professor

Mais uma excelente evolução durante a Python Journey.

Nesta aula foi possível perceber uma mudança importante: o aluno passou a utilizar estruturas mais próximas das encontradas em aplicações reais de Análise de Dados.

Também merece destaque a investigação dos erros encontrados (`KeyError` e BOM do arquivo), demonstrando iniciativa para compreender a causa do problema em vez de apenas buscar uma solução pronta.

Esse tipo de postura será extremamente útil nas próximas etapas da jornada, principalmente quando começarmos a trabalhar com a biblioteca Pandas.

Parabéns pelo excelente desempenho!