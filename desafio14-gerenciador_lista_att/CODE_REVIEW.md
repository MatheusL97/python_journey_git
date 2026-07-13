# 🧐 Code Review - Laboratório de Escopo

## Objetivo

Refatorar o Gerenciador de Compras utilizando parâmetros para reduzir o uso de variáveis globais.

---

# Pontos positivos

## Organização

As responsabilidades das funções permaneceram bem definidas.

Cada função realiza apenas uma tarefa.

---

## Uso de parâmetros

As funções passaram a receber a lista como parâmetro.

Exemplo:

```python
def adicionar_produto(lista):
```

Isso tornou o código mais reutilizável.

---

## Escopo

Foi compreendido o conceito de escopo local e global.

As funções deixaram de depender diretamente da variável `lista_compras`.

---

## Clareza

Os nomes das funções e variáveis permanecem intuitivos e de fácil leitura.

---

# Melhorias identificadas

Durante a revisão foi identificado apenas um detalhe:

Na função `mostrar_lista()`, ainda era utilizado:

```python
enumerate(lista_compras)
```

O ideal é utilizar:

```python
enumerate(lista)
```

para manter o padrão adotado em todas as funções.

---

# Evolução

Este laboratório representou uma mudança importante na forma de organizar funções.

Foi compreendido que parâmetros não servem apenas para números, mas também podem receber listas, tornando o código mais flexível.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Escopo | ⭐⭐⭐⭐⭐ |
| Parâmetros | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |
| Reutilização | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**9,9 / 10**

Excelente evolução.

O objetivo principal da aula foi alcançado com sucesso.

---

## 👨‍🏫 Comentário do Professor

Este laboratório marcou a transição para uma forma mais profissional de desenvolver funções.

A compreensão sobre escopo e passagem de parâmetros será utilizada em praticamente todos os projetos futuros da Python Journey.