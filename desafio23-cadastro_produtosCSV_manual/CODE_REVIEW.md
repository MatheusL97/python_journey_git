# 🔍 Code Review - Desafio 22

# Cadastro de Produtos em CSV

## Avaliação Geral

⭐ Nota: **10 / 10**

Excelente trabalho.

O objetivo do desafio foi atingido com sucesso. O programa cria um arquivo CSV, grava um cabeçalho, cadastra produtos, salva as informações corretamente e exibe o conteúdo do arquivo ao final.

---

# Pontos positivos

## ✔ Organização

O código está dividido em etapas bem definidas:

1. Criação do arquivo.
2. Escrita do cabeçalho.
3. Cadastro dos produtos.
4. Fechamento do arquivo.
5. Leitura do arquivo.
6. Exibição dos dados.

Essa organização facilita a leitura e manutenção do programa.

---

## ✔ Uso correto do modo "w"

```python
arquivo = open('produtos.csv', 'w')
```

Excelente escolha.

O modo `"w"` recria o arquivo a cada execução, evitando cabeçalhos duplicados e tornando o comportamento previsível.

---

## ✔ Cabeçalho

```python
cabecalho = 'Nome;Preco;Estoque\n'
arquivo.write(cabecalho)
```

Muito bem.

O uso do `\n` garante que o primeiro produto seja gravado na linha seguinte.

---

## ✔ Estrutura de repetição

```python
for _ in range(3):
```

Excelente.

Foi utilizada corretamente a variável `_`, indicando que o valor do contador não será utilizado.

Essa é uma convenção muito utilizada na comunidade Python.

---

## ✔ Formatação do preço

```python
{valor:.2f}
```

Muito bom.

Essa formatação deixa o arquivo mais organizado e semelhante ao padrão utilizado em sistemas comerciais.

Exemplo:

```
Notebook;1800.00;5
```

---

## ✔ Escrita no CSV

```python
arquivo.write(f'{nome};{valor:.2f};{estoque}\n')
```

Excelente.

Os dados foram separados por ponto e vírgula (`;`), padrão muito utilizado em arquivos CSV no Brasil.

---

## ✔ Leitura do arquivo

```python
for linha in arquivo:
```

Ótima escolha.

Essa forma é eficiente e indicada para leitura de arquivos.

---

## ✔ Uso do strip()

```python
print(linha.strip())
```

Muito bem.

Remove corretamente a quebra de linha antes da exibição.

---

# Boas práticas observadas

✔ Utilização correta do `capitalize()`.

✔ Conversão dos tipos utilizando `float()` e `int()`.

✔ Fechamento do arquivo antes de reabri-lo.

✔ Código limpo e fácil de entender.

✔ Boa sequência lógica das instruções.

---

# Sugestões de melhoria

Embora o programa esteja correto, ele pode evoluir nas próximas aulas.

Algumas melhorias possíveis:

- criar funções para organizar o código;
- validar entradas do usuário;
- permitir cadastrar uma quantidade variável de produtos;
- calcular o valor total do estoque;
- pesquisar produtos pelo nome;
- editar ou remover produtos cadastrados.

Essas funcionalidades serão estudadas ao longo da Python Journey.

---

# O que foi aprendido

Neste desafio foram consolidados os seguintes conceitos:

- criação de arquivos CSV;
- escrita de cabeçalho;
- gravação de múltiplos registros;
- utilização do laço `for`;
- formatação de números com duas casas decimais;
- leitura de arquivos linha por linha;
- manipulação de arquivos utilizando `open()`, `write()`, `strip()` e `close()`.

---

# Comentário do professor

Este desafio marca um momento importante da Python Journey.

Foi o primeiro contato com um formato de arquivo amplamente utilizado em empresas: o CSV.

O aluno demonstrou compreender não apenas como gravar informações em um arquivo, mas também como estruturar os dados de forma organizada para futuras análises.

Além disso, mostrou evolução na organização do código e na escolha das estruturas adequadas para resolver o problema.

Esse conhecimento será a base para as próximas aulas, nas quais trabalharemos com a biblioteca `csv` e, posteriormente, com **Pandas**, ferramenta essencial para Análise de Dados.

Parabéns pelo excelente trabalho!