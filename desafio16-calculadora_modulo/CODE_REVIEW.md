# 🧐 CODE_REVIEW.md

# Code Review - Desafio 15

## Objetivo

Criar uma calculadora utilizando módulos para organizar o código em diferentes arquivos.

---

# Pontos positivos

## Organização

O projeto foi corretamente dividido em:

- calculadora.py
- main.py

Cada arquivo possui uma responsabilidade específica.

---

## Utilização do import

Foi utilizado corretamente:

```python
import calculadora
```

As funções foram chamadas através do módulo.

Exemplo:

```python
calculadora.somar(numero1, numero2)
```

---

## Estrutura do programa

O programa principal ficou organizado em etapas:

- leitura dos números;
- apresentação do menu;
- escolha da operação;
- chamada da função;
- exibição do resultado.

---

## Menu

A criação da função:

```python
def menu():
```

deixou o código mais organizado e facilitou futuras alterações.

---

## Clareza

O código possui boa legibilidade.

Os nomes das variáveis e funções são intuitivos e facilitam a compreensão.

---

# Melhorias sugeridas

## Mostrar o resultado de forma mais amigável

Ao invés de:

```python
print(calculadora.somar(numero1, numero2))
```

Pode-se utilizar:

```python
resultado = calculadora.somar(numero1, numero2)

print(f"Resultado: {resultado}")
```

Isso melhora a experiência do usuário.

---

## Tratamento de divisão por zero

Ainda não foi estudado tratamento de exceções.

No futuro será interessante impedir erros quando o usuário tentar dividir por zero.

---

# Evolução

Este desafio marcou uma nova etapa na Python Journey.

Pela primeira vez foi desenvolvido um projeto dividido em múltiplos arquivos, utilizando módulos para reutilização de código.

Esse é um conceito utilizado em praticamente todos os projetos profissionais.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Módulos | ⭐⭐⭐⭐⭐ |
| Import | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |
| Reutilização | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**10 / 10**

Excelente implementação.

Os objetivos da aula foram atingidos com sucesso.

---

## 👨‍🏫 Comentário do Professor

Neste desafio foi possível perceber uma evolução significativa na organização do código.

O projeto deixou de ser um único arquivo e passou a utilizar módulos, aproximando-se da estrutura encontrada em aplicações profissionais.

Parabéns pela dedicação e pela evolução constante durante a Python Journey.