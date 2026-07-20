# 🧐 CODE_REVIEW.md

# Code Review - Desafio 17

## Objetivo

Criar um programa para consultar os estados das regiões do Brasil utilizando tuplas.

---

# Pontos positivos

## Organização

O programa foi dividido em funções.

```python
def titulo():
```

Responsável pelo menu.

```python
def mostrar_estados():
```

Responsável por exibir os dados da região.

Essa separação deixou o código mais limpo e organizado.

---

## Utilização de Tuplas

As cinco regiões foram armazenadas utilizando tuplas.

Essa escolha foi correta, pois os estados brasileiros são informações fixas.

---

## Reutilização de código

Na primeira versão do desafio havia repetição de várias linhas.

Na versão final foi criada a função:

```python
def mostrar_estados():
```

Essa alteração eliminou a repetição de código e melhorou significativamente a organização do programa.

---

## Utilização do for

Foi utilizado corretamente:

```python
for estado in estados:
```

Permitindo percorrer toda a tupla.

---

## Utilização do len()

Foi utilizado corretamente:

```python
len(estados)
```

para mostrar a quantidade de estados.

---

## Índices

Também foram utilizados corretamente:

```python
estados[0]
```

```python
estados[-1]
```

Mostrando o primeiro e o último estado.

---

# Melhorias sugeridas

## Receber parâmetros

Hoje a função:

```python
def mostrar_estados():
```

utiliza diretamente a variável global:

```python
estados
```

Uma forma mais profissional seria:

```python
def mostrar_estados(estados):
```

E realizar a chamada:

```python
mostrar_estados(estados)
```

Essa abordagem torna a função independente e reutilizável.

---

## Uso de Dicionários

Em aulas futuras será possível substituir vários blocos `if` e `elif` utilizando dicionários, deixando o programa ainda mais elegante.

---

# Evolução

Este desafio mostrou uma evolução importante na forma de desenvolver.

Além de aplicar corretamente tuplas, houve uma preocupação em eliminar repetições e reutilizar código através de funções.

Essa mudança representa um passo importante rumo ao desenvolvimento de códigos mais limpos e organizados.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Tuplas | ⭐⭐⭐⭐⭐ |
| Funções | ⭐⭐⭐⭐⭐ |
| Reutilização | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |
| Lógica | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**10 / 10**

Excelente implementação.

Todos os objetivos da aula foram alcançados.

---

## 👨‍🏫 Comentário do Professor

Nesta aula foi possível perceber uma mudança na forma de pensar o código.

Ao identificar trechos repetidos, foi criada uma função para centralizar a lógica de exibição dos estados.

Esse tipo de melhoria é conhecido como refatoração e faz parte do dia a dia de qualquer desenvolvedor.

Continue cultivando esse hábito de revisar e melhorar seus programas. É exatamente assim que se constrói um código profissional.