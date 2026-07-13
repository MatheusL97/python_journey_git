# 🧐 CODE_REVIEW.md

# Code Review - Desafio 14

## Objetivo

Construir um sistema para calcular a média de um aluno e informar sua situação utilizando funções e `return`.

---

# Pontos positivos

## Organização

O programa foi dividido em funções específicas.

Cada função possui uma responsabilidade bem definida.

---

## Uso do return

Foi utilizado corretamente para devolver informações ao programa principal.

Exemplo:

```python
return "Aprovado"
```

---

## Separação de responsabilidades

Foram criadas duas funções independentes.

```python
def media():
```

Responsável apenas pelo cálculo.

---

```python
def verificarsituacao():
```

Responsável apenas por informar a situação.

Essa divisão tornou o código mais organizado e reutilizável.

---

## Programa principal

O fluxo ficou bastante claro.

```python
media_aluno = media(nota1_float, nota2_float)

resultado = verificarsituacao(media_aluno)
```

Essa estrutura facilita a leitura e manutenção do código.

---

# Melhorias sugeridas

Utilizar comparações no padrão Python.

Ao invés de:

```python
if media >= 7 and media <= 10:
```

Utilizar:

```python
if 7 <= media <= 10:
```

Da mesma forma:

```python
elif 5 <= media < 7
```

```python
elif 0 <= media < 5
```

Essas comparações tornam o código mais limpo e legível.

---

# Evolução observada

Neste desafio foi possível perceber uma evolução importante.

O aluno deixou de apenas resolver o problema e passou a organizar melhor as funções.

Também demonstrou preocupação em separar responsabilidades entre elas.

Essa mudança representa um avanço significativo na forma de desenvolver programas.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Funções | ⭐⭐⭐⭐⭐ |
| Return | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |
| Lógica | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**10 / 10**

Excelente desafio.

O aluno demonstrou domínio do conteúdo estudado e aplicou corretamente os conceitos apresentados durante a aula.

---

## 👨‍🏫 Comentário do Professor

Neste desafio ficou evidente a evolução na forma de pensar durante o desenvolvimento.

Além de resolver o problema, houve preocupação em construir um código organizado, reutilizável e de fácil leitura.

Esse é um passo importante para o desenvolvimento de programas maiores e mais profissionais.