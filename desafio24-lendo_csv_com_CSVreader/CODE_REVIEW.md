# 🔍 CODE_REVIEW.md

# Aula 24 - Leitura de Arquivos CSV com csv.reader()

## Avaliação Geral

⭐ **Nota: 9,7 / 10**

Parabéns!

O objetivo principal do desafio foi concluído com sucesso. O programa realiza a leitura de um arquivo CSV utilizando a biblioteca `csv`, percorre todas as linhas e exibe as informações de forma organizada para o usuário.

Além disso, foi utilizado o padrão profissional para abertura de arquivos (`with open()`), demonstrando evolução em relação às aulas anteriores.

---

# Pontos positivos

## ✔ Importação da biblioteca

```python
import csv
```

Excelente.

Foi utilizada corretamente a biblioteca responsável pela manipulação de arquivos CSV.

---

## ✔ Uso do with open()

```python
with open('produtos_estoque.csv', 'r', encoding='utf-8') as arquivo:
```

Muito bom.

Essa é a forma recomendada para trabalhar com arquivos em Python.

Vantagens:

- fecha o arquivo automaticamente;
- evita vazamento de recursos;
- deixa o código mais limpo;
- é o padrão utilizado profissionalmente.

---

## ✔ Utilização do csv.reader()

```python
leitor = csv.reader(arquivo, delimiter=';')
```

Perfeito.

O delimitador foi informado corretamente, permitindo que cada coluna do arquivo fosse separada automaticamente.

---

## ✔ Percorrendo os registros

```python
for linha in leitor:
```

Excelente.

A leitura foi realizada de forma simples, eficiente e organizada.

Essa estrutura será utilizada diversas vezes ao longo da Python Journey.

---

## ✔ Acesso às colunas

```python
linha[0]
linha[1]
linha[2]
```

Muito bom.

O aluno demonstrou compreender que cada linha do CSV é transformada em uma lista.

Assim foi possível acessar cada informação utilizando índices.

---

## ✔ Organização da saída

```python
print(
    f'Produto: {linha[0]}\n'
    f'Preço: {linha[1]}\n'
    f'Estoque: {linha[2]}\n'
    f'{"-" * 10}'
)
```

Excelente iniciativa.

O desafio solicitava apenas a leitura do arquivo, mas foi criada uma apresentação muito mais amigável para o usuário.

Esse cuidado com a visualização melhora bastante a experiência de utilização do programa.

---

# Boas práticas observadas

✔ Uso correto da biblioteca `csv`.

✔ Utilização do `with open()`.

✔ Definição correta do delimitador.

✔ Código simples e objetivo.

✔ Boa organização visual da saída.

✔ Aplicação correta dos conceitos estudados.

---

# Ponto de atenção

O arquivo CSV contém um cabeçalho:

```text
Nome;Preco;Estoque
```

Como o programa percorre todas as linhas, o cabeçalho também será exibido.

Exemplo:

```
Produto: Nome
Preço: Preco
Estoque: Estoque
----------
Produto: Notebook
Preço: 1800.00
Estoque: 5
----------
```

Isso **não é um erro**.

Na próxima aula aprenderemos a ignorar automaticamente essa primeira linha utilizando a função `next()`.

---

# Sugestões para evolução

Nas próximas versões do programa seria interessante implementar:

- ignorar o cabeçalho;
- converter preço para `float`;
- converter estoque para `int`;
- calcular o valor total do estoque;
- pesquisar produtos pelo nome;
- listar apenas produtos com estoque baixo;
- ordenar produtos por preço.

Essas melhorias serão desenvolvidas ao longo da Python Journey.

---

# Conceitos consolidados

Durante este desafio foram reforçados os seguintes conteúdos:

- biblioteca `csv`;
- `import csv`;
- `with open()`;
- `csv.reader()`;
- `delimiter`;
- leitura de arquivos CSV;
- listas;
- índices;
- estruturas de repetição.

---

# Comentário do professor

Este desafio representa um avanço importante na Python Journey.

Pela primeira vez, foi utilizada uma biblioteca específica para manipulação de dados, aproximando o estudo da realidade encontrada em empresas.

O aluno demonstrou compreender que o `csv.reader()` transforma cada linha do arquivo em uma lista, reutilizando conhecimentos adquiridos anteriormente sobre listas, índices e estruturas de repetição.

Outro ponto positivo foi a preocupação em apresentar os dados de forma organizada, mostrando que não apenas o funcionamento do programa está sendo considerado, mas também a experiência do usuário.

O código está limpo, bem estruturado e demonstra uma evolução consistente em relação aos desafios anteriores.

Parabéns pelo excelente trabalho!