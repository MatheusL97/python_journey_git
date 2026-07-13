# 📚 Aula 13 - Parâmetros de Funções

## 🎯 Objetivo

Aprender a criar funções que recebem informações através de parâmetros.

Os parâmetros tornam as funções mais flexíveis, permitindo reutilizar o mesmo código com diferentes valores.

---

# 📖 O que são parâmetros?

Parâmetros são variáveis declaradas entre os parênteses de uma função.

Exemplo:

```python
def saudacao(nome):
    print(f'Olá, {nome}!')
```

Neste exemplo:

```python
nome
```

é um parâmetro.

---

# Chamando uma função

```python
saudacao("Matheus")
```

Resultado:

```text
Olá, Matheus!
```

Também podemos utilizar:

```python
saudacao("João")
```

Resultado:

```text
Olá, João!
```

A mesma função pode ser utilizada diversas vezes.

---

# Mais de um parâmetro

Uma função pode receber vários parâmetros.

Exemplo:

```python
def apresentar(nome, idade):
    print(f'{nome} possui {idade} anos.')
```

Executando:

```python
apresentar("Matheus", 29)
```

Resultado:

```text
Matheus possui 29 anos.
```

---

# Estrutura

```python
def nome_da_funcao(parametro1, parametro2):
    ...
```

---

# Diferença entre parâmetro e argumento

Parâmetro:

```python
def saudacao(nome):
```

Argumento:

```python
saudacao("Matheus")
```

O parâmetro recebe o valor do argumento.

---

# Vantagens

- reutilização de código;
- evita repetição;
- funções mais flexíveis;
- código mais organizado;
- diminui a necessidade de criar variáveis desnecessárias.

---

# Boas práticas

Escolha nomes claros para os parâmetros.

Correto:

```python
def mostrar_aluno(nome, idade, curso):
```

Evite:

```python
def mostrar(a, b, c):
```

---

# Conceitos estudados

Nesta aula aprendi:

- criar funções com parâmetros;
- chamar funções passando argumentos;
- diferença entre parâmetro e argumento;
- reutilização de funções.

---

# Resumo

Uma função pode receber informações para executar uma tarefa.

Essas informações são chamadas de parâmetros.

Graças aos parâmetros, uma única função pode trabalhar com diferentes valores sem precisar ser modificada.

---

## 👨‍🏫 Anotação do professor

Uma boa função não deve depender de variáveis espalhadas pelo programa.

Sempre que possível, envie as informações através de parâmetros.

Isso torna o código mais organizado e reutilizável.