# 📚 ANOTACOES.md

# Aula 30 — Análise e classificação de estoque

## 🎯 Objetivo

Aprender a transformar um valor numérico de estoque em uma categoria utilizando estruturas condicionais.

Também foram utilizados contadores para descobrir a quantidade de produtos em cada categoria.

---

# 1. Classificação de dados

Foi criada uma regra para classificar os produtos:

```text
Estoque < 20
→ Estoque baixo

Estoque < 50
→ Estoque normal

Estoque >= 50
→ Estoque alto
```

---

# 2. Estrutura `if`, `elif` e `else`

A classificação foi realizada com:

```python
if estoque < 20:
    ...

elif estoque < 50:
    ...

else:
    ...
```

O primeiro `if` verifica os valores menores que 20.

Caso seja falso, o `elif` verifica se o valor é menor que 50.

Se nenhuma das duas condições for verdadeira, o `else` será executado.

---

# 3. Simplificando condições

Inicialmente poderia ser utilizado:

```python
elif estoque >= 20 and estoque < 50:
```

Porém, não é necessário verificar `estoque >= 20`.

Se o programa chegou ao `elif`, significa que:

```text
estoque < 20
```

já foi considerado falso.

Portanto, sabemos que o estoque é automaticamente 20 ou maior.

Assim podemos utilizar:

```python
elif estoque < 50:
```

Essa forma deixa o código mais simples e legível.

---

# 4. Contadores

Foram criados três contadores:

```python
estoque_baixo = 0
estoque_normal = 0
estoque_alto = 0
```

Quando um produto pertence a uma categoria, seu contador é incrementado:

```python
estoque_baixo += 1
```

ou:

```python
estoque_normal += 1
```

ou:

```python
estoque_alto += 1
```

---

# 5. Resumo fora do `for`

O resumo foi colocado depois do `for`:

```python
for linha in leitor:
    ...

print('===== RESUMO =====')
```

Isso é importante porque o resumo representa todos os produtos processados.

### Dentro do `for`

Trabalhamos com cada registro individualmente.

### Fora do `for`

Trabalhamos com o resultado geral da análise.

---

# 6. Comparando categorias

Depois de contar os produtos, foram comparados os três contadores.

Exemplo:

```python
if estoque_baixo > estoque_normal and estoque_baixo > estoque_alto:
    ...
```

Para uma categoria ser considerada a maior, ela precisa possuir uma quantidade maior que as outras duas.

---

# 7. Operador `and`

O operador `and` exige que as duas condições sejam verdadeiras.

Exemplo:

```python
estoque_baixo > estoque_normal and estoque_baixo > estoque_alto
```

Para essa condição ser verdadeira:

* estoque baixo precisa ser maior que o normal;
* estoque baixo precisa ser maior que o alto.

---

# 8. Atenção aos empates

O código atual não trata situações como:

```text
Estoque baixo: 3
Estoque normal: 5
Estoque alto: 5
```

Nesse caso existe um empate entre estoque normal e estoque alto.

As condições utilizando `>` não identificam um vencedor porque:

```python
5 > 5
```

é falso.

O tratamento de empates será estudado posteriormente.

---

# 🧠 Conceito principal da aula

A aula mostrou como transformar números em informações classificadas.

```text
Dado
 ↓
Regra
 ↓
Classificação
 ↓
Contagem
 ↓
Comparação
 ↓
Informação
```

---

# 📊 Aplicação em Análise de Dados

Esse mesmo raciocínio pode ser utilizado para classificar:

* clientes por faixa de compra;
* produtos por nível de estoque;
* alunos por faixa de notas;
* vendas por valor;
* funcionários por faixa salarial;
* pedidos por prioridade.

---

# 🚀 Evolução

Nesta etapa da Python Journey, o foco começa a sair de operações isoladas e passa para a criação de pequenas análises utilizando dados reais.

Esse conhecimento será importante quando começarmos a utilizar Pandas.
