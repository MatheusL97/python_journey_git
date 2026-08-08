# 🚀 Python Journey — Aula 29

## Valor total do estoque

### Sobre

Nesta aula foi desenvolvido um programa capaz de analisar um arquivo CSV de produtos e calcular:

* valor total do estoque;
* quantidade de produtos cadastrados;
* valor médio do estoque por produto.

O exercício reforça conceitos de leitura e tratamento de dados utilizando Python puro.

---

## 📊 Funcionamento

Para cada produto do arquivo CSV, o programa:

1. Lê o preço.
2. Converte a vírgula decimal para ponto.
3. Converte o preço para `float`.
4. Converte o estoque para `int`.
5. Calcula o valor total daquele produto.
6. Acumula o resultado no valor geral.
7. Conta a quantidade de produtos.

Ao final, calcula o valor médio do estoque por produto.

---

## 🧠 Conceitos praticados

* `csv.DictReader()`
* `replace()`
* `float()`
* `int()`
* `for`
* acumuladores
* contadores
* operações matemáticas
* formatação com `:.2f`

---

## 🔢 Fórmulas utilizadas

### Valor do estoque de um produto

```text
preço × quantidade em estoque
```

### Valor total do estoque

```text
soma do valor de estoque de todos os produtos
```

### Valor médio

```text
valor total do estoque ÷ quantidade de produtos
```

---

## 📌 Aprendizado principal

Foi reforçado o padrão:

```text
Inicializar → Percorrer → Calcular → Acumular → Analisar
```

Esse padrão é muito importante para a futura transição para ferramentas de Análise de Dados.

---

## 🐍 Python Journey

Projeto desenvolvido durante a jornada de estudos em Python com evolução gradual para Análise de Dados.

## Status

✅ Aula concluída
✅ Desafio principal concluído
✅ Desafio extra concluído
