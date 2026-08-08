# 📚 ANOTACOES.md

# Aula 29 — Valor total do estoque

## 🎯 Objetivo

Aprender a calcular informações gerais a partir dos dados de um arquivo CSV.

Nesta aula foram calculados:

* valor total do estoque;
* quantidade de produtos;
* valor médio do estoque por produto.

---

# 1. Acumulador

Criamos uma variável para armazenar a soma dos valores:

```python
valor_geral = 0
```

A cada produto:

```python
valor_geral += valor_total
```

Isso significa:

```python
valor_geral = valor_geral + valor_total
```

O valor vai sendo acumulado durante o `for`.

---

# 2. Contador

Para descobrir quantos produtos existem:

```python
contador = 0
```

Dentro do `for`:

```python
contador += 1
```

Cada produto lido aumenta o contador em 1.

---

# 3. Tratamento do preço

O preço está armazenado no CSV utilizando vírgula:

```text
29,68
```

Precisamos substituir a vírgula por ponto:

```python
preco = linha["preço"].replace(",", ".")
```

Depois converter para `float`:

```python
preco = float(preco)
```

---

# 4. Conversão do estoque

O estoque também vem como texto.

Por isso:

```python
estoque = int(linha["estoque"])
```

---

# 5. Valor total de cada produto

O cálculo é:

```python
valor_total = preco * estoque
```

Exemplo:

```text
Preço: 20,00
Estoque: 10

20 × 10 = 200
```

---

# 6. Valor total do estoque

Depois de calcular cada produto:

```python
valor_geral += valor_total
```

Assim acumulamos o valor de todos os produtos.

---

# 7. Valor médio

Depois que o `for` termina:

```python
valor_medio = valor_geral / contador
```

É importante calcular a média depois do `for`, pois somente nesse momento temos:

* o valor total completo;
* a quantidade total de produtos.

---

# ⚠️ Atenção

Durante o exercício, o cálculo da média estava inicialmente dentro do `for`.

Embora o resultado final pudesse funcionar, é mais organizado deixar:

```python
valor_medio = valor_geral / contador
```

depois do `for`.

Assim separamos:

### Durante o `for`

Coleta e acumulação dos dados.

### Depois do `for`

Análise dos resultados.

---

# 🧠 Padrão aprendido

```text
Inicializar
     ↓
Percorrer
     ↓
Calcular
     ↓
Acumular
     ↓
Analisar
```

Esse padrão aparece frequentemente em programação e Análise de Dados.

---

# 📊 Aplicações

O mesmo conceito pode ser utilizado para calcular:

* faturamento total;
* quantidade de vendas;
* média de vendas;
* total de salários;
* média salarial;
* total de produtos vendidos;
* ticket médio;
* média de preços.

---

# 🚀 Próximo passo

Continuar trabalhando com dados reais em CSV e começar gradualmente a aplicar técnicas cada vez mais próximas da rotina de um Analista de Dados.
