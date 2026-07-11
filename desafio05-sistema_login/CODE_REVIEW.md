# 🧐 Code Review — Desafio 05

## 📋 Informações

**Desafio:** 05 - Sistema de Login

**Status:** ✅ Concluído

**Data:** _(preencher quando desejar)_

---

# 💻 Código analisado

## Pontos positivos

### ✅ Organização

O código foi dividido de forma clara em quatro etapas:

1. Definição da senha correta.
2. Entrada da senha digitada pelo usuário.
3. Estrutura de repetição (`while`).
4. Mensagem de sucesso.

Essa organização facilita a leitura e manutenção do código.

---

### ✅ Nomenclatura das variáveis

As variáveis possuem nomes claros e objetivos.

```python
senha
senha_digitada
```

Isso torna o código autoexplicativo e segue boas práticas de programação.

---

### ✅ Utilização do `while`

A estrutura de repetição foi utilizada corretamente.

```python
while senha_digitada != senha:
```

A condição representa exatamente a regra de negócio:

> Enquanto a senha digitada for diferente da senha correta, o programa continuará solicitando uma nova tentativa.

---

### ✅ Atualização da condição

Durante cada repetição, a variável responsável pela condição é atualizada.

```python
senha_digitada = input("Digite a senha: ")
```

Essa atualização impede que o programa entre em um loop infinito.

Foi exatamente o comportamento esperado para este desafio.

---

### ✅ Legibilidade

O código é curto, organizado e fácil de compreender.

Qualquer pessoa que conheça os conceitos básicos de Python consegue entender sua lógica rapidamente.

---

# 📈 Avaliação

| Critério | Resultado |
|----------|-----------|
| Organização | ⭐⭐⭐⭐⭐ |
| Legibilidade | ⭐⭐⭐⭐⭐ |
| Nomenclatura | ⭐⭐⭐⭐⭐ |
| Uso do `while` | ⭐⭐⭐⭐⭐ |
| Controle da repetição | ⭐⭐⭐⭐⭐ |

---

# 🏆 Nota Final

**10 / 10**

Excelente solução.

O desafio foi resolvido corretamente logo na primeira implementação, demonstrando que o conceito de laço de repetição foi compreendido.

---

# 🎯 Habilidades desenvolvidas

Durante este desafio foram praticadas as seguintes competências:

- Controle de fluxo.
- Estruturas de repetição.
- Comparação de strings.
- Organização do código.
- Pensamento lógico.

---

# 💡 O que aprendi

Neste desafio compreendi que o laço `while` deve ser utilizado quando uma ação precisa ser repetida até que determinada condição seja satisfeita.

Também aprendi que toda estrutura de repetição precisa possuir uma condição que possa ser alterada durante a execução, evitando loops infinitos.

---

# 📚 Próximos passos

No próximo conteúdo serão estudados os comandos:

- `break`
- `continue`

Esses comandos permitem controlar o comportamento dos laços de repetição de maneira mais precisa.

---

## 👨‍🏫 Comentários do professor

Este foi o primeiro desafio utilizando `while`.

A solução apresentada demonstra uma boa compreensão do conceito de repetição e da importância de atualizar a condição do laço durante sua execução.

Outro ponto positivo foi a escolha de nomes claros para as variáveis e a organização do código em etapas bem definidas.

O aluno demonstrou evolução em relação aos desafios anteriores, escrevendo uma solução limpa, objetiva e correta logo na primeira tentativa.

---

## 🚀 Evolução na Python Journey

Após concluir este desafio, os seguintes conceitos já foram estudados:

- ✅ Variáveis
- ✅ `print()`
- ✅ `input()`
- ✅ Conversão de tipos
- ✅ Operadores aritméticos
- ✅ Estruturas condicionais (`if`, `elif` e `else`)
- ✅ Operadores lógicos (`and`, `or` e `not`)
- ✅ Estrutura de repetição (`while`)

Cada desafio concluído representa um novo passo na construção da base necessária para o desenvolvimento de aplicações em Python.