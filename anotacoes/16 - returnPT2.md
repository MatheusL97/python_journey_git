# 📚 ANOTACOES.md

# 📚 Aula 16 - Return (Parte 2)

## 🎯 Objetivo

Aprender a utilizar o `return` para devolver informações de uma função e reutilizá-las no programa principal.

---

# O que é o return?

O `return` encerra a execução da função e devolve um valor para quem a chamou.

Exemplo:

```python
def somar(a, b):
    return a + b
```

Uso:

```python
resultado = somar(5, 3)

print(resultado)
```

Saída:

```
8
```

---

# O que uma função pode retornar?

Uma função pode retornar praticamente qualquer tipo de dado.

Exemplos:

```python
return 10
```

```python
return 3.14
```

```python
return "Python"
```

```python
return True
```

```python
return False
```

```python
return lista
```

---

# Uma função = uma responsabilidade

Durante esta aula foi aplicado o conceito de separar responsabilidades.

Exemplo:

```python
def media(nota1, nota2):
    return (nota1 + nota2) / 2
```

Responsabilidade:

✔ Calcular a média.

---

```python
def verificarsituacao(media):
```

Responsabilidade:

✔ Informar a situação do aluno.

---

Essa organização torna o código:

- mais limpo;
- mais organizado;
- mais fácil de manter;
- mais fácil de reutilizar.

---

# Boas práticas

Evite calcular o mesmo valor mais de uma vez.

Exemplo:

❌

```python
media = (nota1 + nota2) / 2
```

em várias funções.

Prefira:

```python
media_aluno = media(nota1, nota2)
```

Depois reutilize:

```python
resultado = verificarsituacao(media_aluno)
```

---

# Comparações em Python

Podemos simplificar comparações.

Ao invés de:

```python
if media >= 7 and media <= 10:
```

Podemos escrever:

```python
if 7 <= media <= 10:
```

Outro exemplo:

```python
elif 5 <= media < 7:
```

Esse formato é muito utilizado em Python.

---

# Aprendizados

Nesta aula aprendi:

- utilizar `return`;
- separar responsabilidades entre funções;
- reutilizar valores retornados;
- evitar repetir cálculos;
- escrever comparações de forma mais elegante.