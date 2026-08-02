# 🚀 README.md

# Aula 26 - Calculando o valor do estoque

## Sobre

Neste desafio foi desenvolvido um programa capaz de ler um arquivo CSV utilizando `csv.DictReader()`, converter os dados para seus tipos corretos e calcular o valor em estoque de cada produto.

Ao final da execução, o programa informa:

- quantidade de produtos cadastrados;
- valor total do estoque da loja.

---

## Funcionalidades

- importar a biblioteca csv;
- ler arquivos CSV;
- converter preços para float;
- converter estoques para int;
- calcular o valor em estoque de cada produto;
- calcular o valor total do estoque da loja;
- contar os registros do arquivo.

---

## Estrutura do arquivo

```csv
nome;preço;estoque
Arroz Tipo 1 5kg;29,68;11
Feijão Preto 1kg;34,02;67
...
```

---

## Fluxo do programa

1. Abrir o arquivo CSV.
2. Ler os registros utilizando `DictReader`.
3. Converter o preço utilizando `replace()` e `float()`.
4. Converter o estoque utilizando `int()`.
5. Calcular o valor em estoque de cada produto.
6. Acumular o valor geral do estoque.
7. Contar os produtos.
8. Exibir o resultado final.

---

## Conceitos praticados

✔ csv.DictReader()

✔ replace()

✔ float()

✔ int()

✔ acumuladores

✔ contadores

✔ cálculos matemáticos

✔ formatação de valores

---

## Aprendizados

Durante este desafio foi possível compreender que os dados lidos de um CSV são inicialmente strings e precisam ser convertidos antes de serem utilizados em cálculos.

Também foi possível calcular o valor financeiro de cada produto e o valor total do estoque da loja.

---

## Próximos passos

Na próxima aula serão realizadas análises sobre os dados, como identificar automaticamente:

- produto mais caro;
- produto mais barato;
- maior estoque;
- menor estoque.

---

## Python Journey

Projeto desenvolvido durante minha jornada de estudos em Python com foco em Desenvolvimento e Análise de Dados.

---

## Status

✅ Desafio concluído com sucesso.