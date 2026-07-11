# 🐍 Python Journey

# 07 Laço de Repetição (`while`)

## 🎯 Objetivo

Aprender a utilizar o laço de repetição `while` para executar um bloco de código enquanto uma condição for verdadeira.

---

# 📖 O que é o `while`?

O `while` é uma estrutura de repetição da linguagem Python.

Seu objetivo é executar um bloco de código **enquanto** uma condição permanecer verdadeira.

A palavra `while` significa:

> **Enquanto**

Sempre que um programa precisar repetir uma ação até que determinada condição deixe de ser verdadeira, o `while` pode ser utilizado.

---

# 📌 Estrutura

```python
while condição:
    # código que será repetido
```

Enquanto a condição for verdadeira, o Python continuará executando o bloco de código.

---

# 💡 Exemplo

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
```

### Saída

```text
1
2
3
4
5
```

---

# 🧠 Como o `while` funciona?

Todo `while` possui três partes importantes.

## 1. Valor inicial

```python
contador = 1
```

É o ponto de partida da repetição.

---

## 2. Condição

```python
while contador <= 5:
```

O Python verifica essa condição antes de cada repetição.

Se for verdadeira, o bloco será executado.

Se for falsa, o laço termina.

---

## 3. Atualização

```python
contador = contador + 1
```

Atualiza o valor utilizado na condição.

Sem essa atualização, o programa poderá entrar em um **loop infinito**.

---

# ⚠️ Loop infinito

Um loop infinito acontece quando a condição do `while` nunca deixa de ser verdadeira.

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Nesse caso, o valor de `contador` nunca muda.

O programa continuará imprimindo o número `1` indefinidamente.

---

# 💻 Exemplos de uso

O `while` é utilizado em diversas situações, como:

- Solicitar uma senha até que esteja correta.
- Exibir um menu até o usuário escolher sair.
- Realizar várias operações sem encerrar o programa.
- Processar informações repetidamente.

---

# 🧠 Como pensar antes de criar um `while`

Sempre responda às seguintes perguntas:

### Onde começa?

Exemplo:

```python
contador = 1
```

---

### Quando termina?

Exemplo:

```python
contador > 5
```

---

### O que muda a cada repetição?

Exemplo:

```python
contador = contador + 1
```

Se você conseguir responder essas três perguntas, provavelmente conseguirá construir um `while`.

---

# ⚠️ Erros comuns

- Esquecer de atualizar a variável de controle.
- Criar uma condição que nunca se torna falsa.
- Confundir `if` com `while`.

Lembre-se:

- `if` executa uma única vez.
- `while` executa várias vezes enquanto a condição for verdadeira.

---

# 🌎 Onde isso é usado no mercado?

O `while` está presente em diversos sistemas reais.

Exemplos:

- Sistemas de login.
- Caixas eletrônicos.
- Menus de sistemas administrativos.
- Jogos.
- Aplicações que aguardam ações do usuário.

---

# 📌 Resumo

- `while` significa **enquanto**.
- Repete um bloco de código.
- Executa enquanto a condição for verdadeira.
- Todo `while` precisa de uma condição que possa se tornar falsa em algum momento.

---

# ✅ Checklist

- [ ] Sei quando utilizar `while`.
- [ ] Entendo a estrutura do `while`.
- [ ] Sei identificar um loop infinito.
- [ ] Sei a importância da atualização da condição.
- [ ] Consigo explicar a diferença entre `if` e `while`.

---

> **"Um bom programador não pensa apenas no que o programa faz, mas também em como e quando ele deve parar."**

— Python Journey 🐍