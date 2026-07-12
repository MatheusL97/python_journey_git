# 🧐 Code Review - Desafio 11

## 📋 Informações

**Desafio:** 11 - Gerenciador de Compras com Funções

**Status:** ✅ Concluído

---

# Objetivo

Refatorar o Gerenciador de Compras utilizando funções (`def`), mantendo exatamente o mesmo comportamento do programa.

---

# Pontos positivos

## Organização

O código ficou muito mais organizado.

As funções foram declaradas antes do `while`, seguindo uma estrutura utilizada em projetos profissionais.

---

## Responsabilidade única

Cada função executa apenas uma tarefa.

Exemplos:

- mostrar menu;
- adicionar produto;
- alterar produto;
- remover produto;
- listar produtos;
- encerrar sistema.

Isso melhora a legibilidade e facilita futuras alterações.

---

## Clareza

Os nomes das funções são descritivos.

Exemplo:

```python
mostrar_menu()
```

É possível entender sua finalidade apenas pelo nome.

---

## Reutilização

Sempre que for necessário mostrar o menu, basta chamar:

```python
mostrar_menu()
```

Sem repetir várias linhas de código.

---

# Evolução

Comparando com os desafios anteriores, este foi um dos maiores avanços da Python Journey.

O programa continua fazendo exatamente as mesmas tarefas, porém sua estrutura ficou muito mais profissional.

Essa prática é conhecida como **refatoração**.

---

# Melhorias futuras

Nas próximas aulas será possível evoluir ainda mais o sistema utilizando:

- parâmetros;
- `return`;
- tratamento de exceções;
- arquivos;
- módulos.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Uso de funções | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |
| Legibilidade | ⭐⭐⭐⭐⭐ |
| Reutilização | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**10/10**

Excelente trabalho.

O objetivo da aula foi totalmente alcançado.

---

## 👨‍🏫 Comentário do Professor

Este desafio marcou uma mudança importante na forma de programar.

Até então, os programas eram escritos em um único bloco de código. A partir desta aula, o sistema passou a ser dividido em pequenas funções, cada uma responsável por uma tarefa específica.

Essa forma de organização facilita a leitura, a manutenção e a evolução do programa, sendo uma prática utilizada em praticamente todos os projetos profissionais.

A evolução do aluno demonstra não apenas domínio da sintaxe, mas também o desenvolvimento de boas práticas de programação.