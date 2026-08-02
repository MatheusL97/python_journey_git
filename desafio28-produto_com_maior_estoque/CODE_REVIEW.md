# 🔍 CODE_REVIEW.md

# Aula 27 - Encontrando o maior e o menor estoque

## Avaliação Geral

⭐ Nota: **10 / 10**

Excelente trabalho!

O algoritmo foi implementado corretamente e percorre o arquivo apenas uma vez, tornando a solução simples e eficiente.

---

# Pontos positivos

## ✔ Leitura do arquivo

```python
with open("produtos_estoque.csv", "r", encoding="utf-8-sig") as arquivo:
```

Uso correto do `with open()`.

---

## ✔ DictReader

```python
leitor = csv.DictReader(arquivo, delimiter=";")
```

Excelente utilização do cabeçalho do arquivo.

---

## ✔ Conversão

```python
estoque = int(linha["estoque"])
```

Conversão correta antes da comparação.

---

## ✔ Variáveis de referência

```python
maior_estoque = None
produto_maior = ""

menor_estoque = None
produto_menor = ""
```

Boa escolha de nomes e inicialização adequada.

---

## ✔ Comparação

```python
if maior_estoque is None or estoque > maior_estoque:
```

Lógica correta para encontrar o maior valor.

---

## ✔ Menor valor

```python
if menor_estoque is None or estoque < menor_estoque:
```

Muito bom.

A utilização de um segundo `if` garante que as duas comparações sejam realizadas de forma independente.

---

## Evolução durante o desenvolvimento

Inicialmente foi utilizada uma estrutura com `elif`, o que impedia a atualização correta do menor estoque em determinadas situações.

Após a análise do algoritmo, a estrutura foi ajustada para dois `if`, solucionando o problema e tornando a lógica correta.

Esse tipo de refinamento faz parte do processo de desenvolvimento profissional e demonstra evolução no entendimento das estruturas condicionais.

---

# Sugestões futuras

Como melhoria visual, a saída pode ser apresentada com mensagens mais descritivas.

Exemplo:

```python
print(f"Produto: {produto_maior}")
print(f"Quantidade: {maior_estoque} unidades")
```

---

# Conceitos consolidados

Durante este desafio foram reforçados:

- comparação de valores;
- busca do maior elemento;
- busca do menor elemento;
- variáveis de referência;
- uso de `None`;
- estruturas condicionais independentes;
- análise de dados em arquivos CSV.

---

# Comentário do professor

Esta aula consolidou um dos algoritmos mais utilizados em programação e Análise de Dados: a busca por valores máximos e mínimos.

Além de implementar corretamente a solução, o aluno compreendeu a diferença entre utilizar `if` e `elif` em situações onde as verificações precisam ocorrer de forma independente.

A evolução no raciocínio lógico e na organização do código é bastante perceptível em relação às primeiras aulas da Python Journey.

Parabéns pelo excelente trabalho!