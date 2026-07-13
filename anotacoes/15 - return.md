# 📚 Aula 14 - Return

## 🎯 Objetivo

Aprender como uma função pode devolver um valor para o programa utilizando a palavra-chave `return`.

Até esta aula, as funções apenas executavam ações. Agora elas também podem produzir resultados que serão utilizados em outras partes do programa.

---

# O que é o return?

O `return` é utilizado para devolver um valor ao programa que chamou a função.

Exemplo:

```python
def somar(a, b):
    return a + b
```

---

# Chamando a função

```python
resultado = somar(10, 5)

print(resultado)
```

Resultado:

```text
15
```

---

# Diferença entre print() e return

## print()

```python
def somar(a, b):
    print(a + b)
```

Mostra o resultado na tela.

---

## return

```python
def somar(a, b):
    return a + b
```

Devolve o resultado para ser utilizado pelo programa.

---

# Exemplo

```python
def dobro(numero):
    return numero * 2

resultado = dobro(8)

print(resultado)
```

Resultado:

```text
16
```

---

# Fluxo do return

```
Programa principal

↓

Chama a função

↓

A função executa o cálculo

↓

return devolve o resultado

↓

Programa principal recebe o valor

↓

print() exibe o resultado
```

---

# Conceitos estudados

Nesta aula aprendi:

- utilizar `return`;
- diferença entre `print()` e `return`;
- armazenar o retorno em uma variável;
- utilizar o resultado retornado em outras operações.

---

# Resumo

O `return` permite que uma função devolva um resultado para o programa.

Dessa forma, o valor poderá ser armazenado em uma variável ou utilizado em outras operações.

---

## 👨‍🏫 Anotação do professor

Sempre que uma função precisar produzir um resultado para ser utilizado posteriormente, utilize `return`.

Use `print()` apenas quando o objetivo for exibir informações ao usuário.