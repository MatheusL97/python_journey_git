# 📚 Aula 10 - Laço de Repetição (`for`)

## 🎯 Objetivo

Aprender a utilizar o laço de repetição `for` para percorrer sequências e repetir instruções de forma simples, organizada e eficiente.

O `for` é uma das estruturas mais utilizadas em Python e será muito importante para os próximos conteúdos da jornada.

---

# 📖 O problema

Até agora utilizamos o `while` para repetir ações.

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Esse método funciona muito bem, porém exige que o programador controle a variável de repetição manualmente.

Quando precisamos percorrer uma lista, existe uma maneira muito mais simples.

Foi para isso que o `for` foi criado.

---

# 🤔 O que é o `for`?

O `for` percorre automaticamente uma sequência, executando um bloco de código para cada elemento encontrado.

Exemplo:

```python
frutas = ["Maçã", "Banana", "Laranja"]

for fruta in frutas:
    print(fruta)
```

Resultado:

```text
Maçã
Banana
Laranja
```

Observe que não foi necessário utilizar contador.

O Python faz esse trabalho automaticamente.

---

# 📦 Estrutura do `for`

A estrutura básica é:

```python
for variavel in sequencia:
    bloco_de_codigo
```

Onde:

- `variavel` recebe um elemento da sequência por vez.
- `sequencia` pode ser uma lista, string, `range()` ou outras coleções.

---

# 📚 Percorrendo listas

Exemplo:

```python
nomes = ["Ana", "Carlos", "Pedro"]

for nome in nomes:
    print(nome)
```

Resultado:

```text
Ana
Carlos
Pedro
```

Cada repetição recebe um elemento diferente da lista.

---

# 🔢 Utilizando `range()`

Também podemos utilizar o `for` para repetir um bloco de código várias vezes.

Exemplo:

```python
for numero in range(5):
    print(numero)
```

Resultado:

```text
0
1
2
3
4
```

O número informado representa o limite da repetição.

O último valor nunca é incluído.

---

# 📍 Definindo início e fim

Também podemos informar o valor inicial.

Exemplo:

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```text
1
2
3
4
5
```

Neste caso:

- começa em 1;
- termina antes do 6.

---

# 🔄 Comparando `while` e `for`

## While

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

É necessário controlar a variável manualmente.

---

## For

```python
for numero in range(5):
    print(numero)
```

O Python controla automaticamente a repetição.

O código fica menor, mais limpo e mais fácil de entender.

---

# 📋 Quando utilizar cada um?

Utilize `while` quando:

- não souber quantas repetições serão necessárias;
- depender de uma condição para encerrar o programa.

Exemplo:

Sistema de login.

---

Utilize `for` quando:

- desejar percorrer listas;
- desejar repetir um bloco de código uma quantidade conhecida de vezes.

---

# 💡 Exemplos

Percorrendo uma lista:

```python
produtos = ["Arroz", "Feijão", "Leite"]

for produto in produtos:
    print(produto)
```

Resultado:

```text
Arroz
Feijão
Leite
```

---

Repetindo cinco vezes:

```python
for numero in range(5):
    print("Olá!")
```

Resultado:

```text
Olá!
Olá!
Olá!
Olá!
Olá!
```

---

# 📝 Conceitos estudados

Nesta aula aprendemos:

- laço `for`;
- percorrer listas;
- função `range()`;
- repetições controladas;
- diferença entre `while` e `for`.

---

# 🚫 Erros comuns

## Esquecer os dois pontos

Errado:

```python
for numero in range(5)
```

Correto:

```python
for numero in range(5):
```

---

## Esquecer a indentação

Todo bloco pertencente ao `for` deve estar indentado.

Correto:

```python
for numero in range(5):
    print(numero)
```

---

## Esperar que o último número seja exibido

Exemplo:

```python
range(5)
```

Resultado:

```text
0
1
2
3
4
```

O número 5 não será exibido.

Essa é uma das dúvidas mais comuns entre iniciantes.

---

# 🧠 Resumo

Nesta aula aprendi:

- O que é o laço `for`;
- Como percorrer listas;
- Como utilizar `range()`;
- Quando utilizar `while`;
- Quando utilizar `for`;
- Como escrever códigos mais limpos utilizando o `for`.

---

# 🎯 Conclusão

O laço `for` simplifica a repetição de tarefas e elimina a necessidade de controlar variáveis de repetição manualmente.

É uma das estruturas mais importantes da linguagem Python e será utilizada constantemente nos próximos desafios da Python Journey.

---

## 👨‍🏫 Anotação do professor

O `for` representa um grande passo na evolução da lógica de programação.

Até esta aula, os programas dependiam principalmente do `while`.

A partir de agora, será possível percorrer listas, exibir informações de forma organizada e escrever códigos mais elegantes e legíveis.

Dominar o `for` facilitará muito o aprendizado de funções, dicionários, arquivos e diversos outros recursos da linguagem.

> **"Um bom programador não escreve mais código. Ele escreve o código mais simples possível para resolver o problema."**