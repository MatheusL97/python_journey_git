# 🧐 Code Review - Desafio 08

## 📋 Informações

**Desafio:** 08 - Gerenciador de Compras

**Status:** ✅ Concluído

---

# 🎯 Objetivo

Desenvolver um sistema capaz de:

- Adicionar produtos;
- Alterar produtos;
- Remover produtos;
- Visualizar a lista;
- Encerrar o programa.

---

# ✅ Pontos positivos

## Organização

O código foi organizado em uma estrutura simples e de fácil leitura.

A lista foi criada fora do `while`, permitindo que os dados permanecessem durante toda a execução do programa.

---

## Estrutura do menu

O menu ficou claro e bem dividido.

Cada opção possui uma responsabilidade específica.

---

## Uso das listas

Foram utilizados corretamente:

- `append()`
- alteração por índice
- `pop()`
- `len()`

Todos os métodos foram aplicados corretamente.

---

## Estruturas condicionais

O uso de `if`, `elif` e `else` tornou o fluxo do programa fácil de compreender.

---

## Uso do `while`

O programa permanece em execução até que o usuário escolha a opção de sair.

Foi utilizado corretamente o comando:

```python
break
```

---

# 💡 Melhorias futuras

Durante a alteração de um produto, caso o usuário informe uma posição inexistente, o programa será encerrado com erro.

O mesmo acontece durante a remoção.

Esses casos serão tratados futuramente quando estudarmos tratamento de exceções (`try/except`).

---

## Exibição da lista

Atualmente os produtos são exibidos assim:

```text
['Arroz', 'Feijão', 'Leite']
```

Após aprender o laço `for`, a exibição poderá ser melhorada para:

```text
0 - Arroz
1 - Feijão
2 - Leite
```

Essa melhoria será implementada em uma futura revisão do projeto.

---

# 📈 Evolução

Neste desafio foi possível perceber uma evolução significativa na construção da lógica.

Grande parte do programa foi desenvolvida sem auxílio direto, demonstrando maior autonomia na resolução dos problemas.

---

# ⭐ Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Lógica | ⭐⭐⭐⭐⭐ |
| Uso de listas | ⭐⭐⭐⭐⭐ |
| Estruturas condicionais | ⭐⭐⭐⭐⭐ |
| Uso do while | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |

---

# 🏆 Nota Final

**10/10**

Excelente trabalho.

O desafio apresentou uma estrutura semelhante às operações básicas de um CRUD (Create, Read, Update e Delete), muito utilizadas em sistemas reais.

Parabéns pela evolução demonstrada durante este projeto.

---

## 👨‍🏫 Comentário do Professor

Este desafio marcou uma nova etapa da Python Journey.

Pela primeira vez, o desenvolvimento aconteceu com pouca intervenção do professor, mostrando que o raciocínio lógico está evoluindo de forma consistente.

Continue estudando com calma e mantendo essa organização. Os próximos conteúdos aproveitarão toda a base construída até aqui.