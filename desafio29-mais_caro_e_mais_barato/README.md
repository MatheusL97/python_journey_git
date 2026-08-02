# 🚀 README.md

# Aula 28 - Produto mais caro e mais barato

## Sobre

Neste desafio foi desenvolvido um programa capaz de analisar um arquivo CSV para identificar automaticamente:

- o produto mais caro;
- o produto mais barato;
- a diferença entre os dois preços.

Toda a análise é realizada percorrendo o arquivo apenas uma única vez.

---

## Funcionalidades

- leitura de arquivos CSV;
- utilização do csv.DictReader();
- tratamento do preço com replace();
- conversão para float;
- identificação do maior preço;
- identificação do menor preço;
- cálculo da diferença entre os preços;
- exibição organizada dos resultados.

---

## Fluxo do programa

1. Abrir o arquivo CSV.
2. Ler cada produto utilizando DictReader.
3. Converter o preço para float.
4. Comparar o maior preço.
5. Comparar o menor preço.
6. Atualizar as variáveis de referência.
7. Calcular a diferença.
8. Exibir os resultados.

---

## Conceitos praticados

✔ csv.DictReader()

✔ replace()

✔ float()

✔ comparação de números

✔ variáveis de referência

✔ operadores relacionais

✔ reutilização de algoritmos

---

## Aprendizados

Durante este desafio foi possível perceber que o mesmo algoritmo utilizado para encontrar o maior estoque pode ser reutilizado para encontrar o maior preço.

Também foi aprendido que variáveis responsáveis por armazenar o resultado final da análise devem ser inicializadas antes do laço, evitando que sejam reiniciadas a cada iteração.

---

## Próximos passos

Nas próximas aulas continuaremos explorando análises sobre arquivos CSV, preparando a base para trabalhar futuramente com a biblioteca Pandas.

---

## Python Journey

Projeto desenvolvido durante minha jornada de estudos em Python com foco em Desenvolvimento e Análise de Dados.

---

## Status

✅ Desafio concluído com sucesso.