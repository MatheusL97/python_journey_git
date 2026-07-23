# 🔍 CODE_REVIEW.md

# Code Review - Desafio 18

## Avaliação Geral

⭐ Nota: **9,8 / 10**

Excelente evolução.

Este desafio demonstrou que você compreendeu como os dicionários armazenam informações e como tratar dados opcionais utilizando `get()`.

O principal aprendizado foi perceber que uma variável criada no programa não faz parte do dicionário até que seja adicionada explicitamente.

---

# Pontos positivos

✔ Organização do código.

✔ Utilização correta do dicionário.

✔ Uso correto de `.items()`.

✔ Boa escolha dos tipos de dados (`int` para idade).

✔ Utilização correta do método `get()`.

✔ Código simples e fácil de entender.

---

# Pontos para melhorar

## 1. Tratamento da opção "N"

Atualmente o programa considera qualquer resposta diferente de "S" como inválida.

O ideal seria tratar:

```python
if resposta == "S":
    ...

elif resposta == "N":
    ...

else:
    print("Opção inválida")
```

---

## 2. Nome das variáveis

Uma variável como:

```python
telefone
```

poderia ser chamada de:

```python
resposta_telefone
```

para a pergunta "Deseja cadastrar telefone?".

Depois, quando o usuário informar o número, utilizar outra variável:

```python
numero_telefone
```

Isso torna o código mais legível.

---

## 3. Organização futura

Em breve começaremos a criar funções para organizar ainda mais esse programa.

Por exemplo:

- cadastrar_aluno()
- mostrar_aluno()

Isso deixará o código mais profissional.

---

# O que foi aprendido

Neste desafio você consolidou:

- criação de dicionários;
- adição de novas chaves;
- tratamento de informações opcionais;
- utilização do método `get()`;
- utilização do método `.items()`.

---

# Comentário do professor

Este desafio teve um papel importante na Python Journey porque apresentou um problema comum em sistemas reais: nem todas as informações são obrigatórias.

Você inicialmente confundiu a variável `telefone` com a chave `"telefone"` do dicionário, mas rapidamente compreendeu a diferença e conseguiu corrigir a lógica.

Esse tipo de aprendizado vale muito mais do que simplesmente copiar uma solução, pois fortalece o entendimento sobre como os dicionários funcionam.

Continue mantendo esse padrão de organização e preocupação em entender o "porquê" das soluções. Essa postura fará muita diferença nas próximas etapas da jornada.

Parabéns pelo excelente trabalho!