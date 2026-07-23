# 🚀 README.md

# Desafio 18 - Cadastro de Alunos

## 📖 Sobre

Neste desafio foi desenvolvido um sistema simples de cadastro de alunos utilizando dicionários.

O usuário informa os dados do aluno e pode escolher cadastrar ou não um telefone de contato.

Caso o telefone não seja informado, o programa utiliza o método `get()` para exibir uma mensagem padrão.

---

## Funcionalidades

- Cadastro do nome
- Cadastro da idade
- Cadastro do curso
- Cadastro opcional do telefone
- Exibição organizada das informações

---

## Conceitos praticados

✔ Dicionários

✔ `.get()`

✔ `.items()`

✔ Condicionais (`if`, `elif`, `else`)

✔ Entrada de dados (`input()`)

✔ Tipos de dados (`int` e `str`)

---

## Funcionamento

1. O usuário informa nome, idade e curso.

2. O sistema pergunta se deseja cadastrar um telefone.

3. Caso responda **S**, o telefone é adicionado ao dicionário.

4. Caso responda **N**, o telefone não é cadastrado.

5. Na exibição dos dados, o método `get()` é utilizado para mostrar:

```
Telefone: Não informado
```

quando a chave não existir.

---

## Exemplo

```
Nome: Matheus
Idade: 29
Curso: ADS
Telefone: Não informado
```

ou

```
Nome: Matheus
Idade: 29
Curso: ADS
Telefone: (61)99999-9999
```

---

## Aprendizados

Durante este desafio foi possível compreender como trabalhar com informações opcionais dentro de um dicionário.

Também foi possível entender que criar uma variável não significa adicioná-la automaticamente ao dicionário.

É necessário inserir uma nova chave manualmente.

---

## Python Journey

Desafio desenvolvido durante a Python Journey para consolidar o uso de dicionários e do método `get()`.

---

## Status

✅ Desafio concluído.