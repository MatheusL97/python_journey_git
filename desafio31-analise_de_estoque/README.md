# 🚀 Python Journey — Aula 30

## Análise e classificação de estoque

### 📌 Sobre

Nesta aula foi desenvolvido um programa capaz de analisar os produtos de um arquivo CSV e classificar seus estoques em três categorias:

* Estoque baixo
* Estoque normal
* Estoque alto

Além da classificação individual, o programa também contabiliza quantos produtos existem em cada categoria e identifica qual categoria possui a maior quantidade de produtos.

---

## 🎯 Objetivos

* Praticar estruturas condicionais.
* Trabalhar com dados vindos de um CSV.
* Converter valores de texto para números.
* Criar contadores.
* Classificar registros de acordo com regras.
* Comparar resultados acumulados.
* Transformar dados brutos em informações úteis.

---

## 📊 Regras utilizadas

O programa utiliza as seguintes regras:

|      Estoque | Situação       |
| -----------: | -------------- |
| Menor que 20 | Estoque baixo  |
| De 20 até 49 | Estoque normal |
|   50 ou mais | Estoque alto   |

---

## 🧠 Conceitos praticados

* `csv`
* `csv.DictReader()`
* `with open()`
* `int()`
* `for`
* `if`
* `elif`
* `else`
* operadores relacionais
* operador `and`
* contadores
* comparação de variáveis
* f-strings

---

## 🔢 Funcionamento

Para cada produto do CSV:

1. O estoque é lido.
2. O valor é convertido para `int`.
3. O estoque é classificado.
4. O contador correspondente é incrementado.
5. As informações do produto são exibidas.

Depois que todos os produtos são processados, o programa apresenta um resumo geral.

Por fim, os três contadores são comparados para descobrir qual categoria possui a maior quantidade de produtos.

---

## 🧠 Estrutura lógica

```text
Ler CSV
   ↓
Percorrer produtos
   ↓
Ler estoque
   ↓
Classificar estoque
   ↓
Incrementar contador
   ↓
Próximo produto
   ↓
Resumo
   ↓
Comparar categorias
```

---

## 📈 Relação com Análise de Dados

Nesta aula foi dado mais um passo em direção à Análise de Dados.

Os dados inicialmente estavam apenas registrados no CSV.

Depois foram:

```text
Dados brutos
     ↓
Tratamento
     ↓
Classificação
     ↓
Contagem
     ↓
Comparação
     ↓
Informação
```

Esse processo representa uma base importante para análises futuras utilizando ferramentas como Pandas, SQL e Power BI.

---

## ⚠️ Observação

A comparação atual identifica a categoria com maior quantidade quando existe apenas um vencedor.

Em caso de empate entre duas ou mais categorias, o programa não apresenta uma categoria vencedora.

O tratamento de empates será trabalhado posteriormente.

---

## ✅ Status

* [x] Desafio principal
* [x] Classificação de estoque
* [x] Contadores
* [x] Resumo
* [x] Desafio bônus
* [x] Comparação entre categorias

**Aula concluída com sucesso.** 🐍📊
