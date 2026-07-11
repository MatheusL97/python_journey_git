# 👏👏👏 Matheus!!

**Agora sim.**

Eu diria que este foi o seu melhor desafio até agora.

E sabe por quê?

Porque desta vez eu não precisei explicar a solução. Eu apenas fiz perguntas, e **você encontrou o caminho**.

Isso é exatamente o que um mentor busca.

---

# 🧐 Code Review

## Código

```python
lista = []

while True:
    print('====== LISTA DE COMPRAS ======\n\n'
          '1 - Adicionar produto\n'
          '2 - Ver lista\n'
          '3 - Sair\n')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        produto = input('O que deseja adicionar? ')
        lista.append(produto)

    elif opcao == '2':
        if len(lista) > 0:
            print(lista)
        else:
            print('A lista possui zero produtos')

    elif opcao == '3':
        print('Sistema encerrado')
        break

    else:
        print('Opção inválida')
```

---

# ✅ Organização

⭐⭐⭐⭐⭐

O programa está dividido em etapas bem claras:

* criação da lista;
* menu;
* leitura da opção;
* tratamento de cada opção.

Isso deixa o código muito fácil de acompanhar.

---

# ✅ Uso da lista

```python
lista = []
```

Excelente.

Agora ela existe durante toda a execução do programa.

Foi exatamente a correção que discutimos.

---

# ✅ Uso do `append()`

```python
lista.append(produto)
```

Perfeito.

Você utilizou o método correto para adicionar novos itens.

---

# ✅ Uso do `len()`

```python
if len(lista) > 0:
```

Muito bom.

Você lembrou da função da aula e a aplicou corretamente.

Inclusive, no mercado é comum encontrar também:

```python
if len(lista) == 0:
```

ou até:

```python
if not lista:
```

Mas essa última nós veremos mais para frente.

Para o seu nível, sua solução está excelente.

---

# ✅ Uso do `break`

```python
elif opcao == '3':
    print('Sistema encerrado')
    break
```

Perfeito.

Era exatamente o objetivo do desafio.

---

# 📌 Pequena melhoria

Na opção 1, seria interessante informar ao usuário que tudo ocorreu bem.

Exemplo:

```python
print('Produto adicionado com sucesso!')
```

Isso melhora a experiência de quem utiliza o sistema.

Mas **não é um erro**. É apenas uma melhoria de usabilidade.

---

# 📌 Outro detalhe

Hoje você imprime a lista assim:

```python
print(lista)
```

Resultado:

```text
['Arroz', 'Feijão', 'Leite']
```

Está **correto**.

Quando aprendermos `for`, vamos evoluir isso para:

```text
Sua lista:

- Arroz
- Feijão
- Leite
```

Ou seja, não há nada para corrigir agora.

Esse desafio será naturalmente melhorado quando chegarmos ao conteúdo de `for`.

---

# 📊 Avaliação

| Critério          | Nota  |
| ----------------- | ----- |
| Organização       | ⭐⭐⭐⭐⭐ |
| Estrutura         | ⭐⭐⭐⭐⭐ |
| Uso do `while`    | ⭐⭐⭐⭐⭐ |
| Uso de listas     | ⭐⭐⭐⭐⭐ |
| Uso do `append()` | ⭐⭐⭐⭐⭐ |
| Uso do `len()`    | ⭐⭐⭐⭐⭐ |
| Legibilidade      | ⭐⭐⭐⭐⭐ |

---

# 🏆 Nota Final

# **10 / 10** 🥳

---

# 📈 Sua evolução

Olha onde você estava há alguns desafios:

### Desafio 01

Uma calculadora usando apenas `if`.

---

### Desafio 05

Primeiro contato com `while`.

---

### Desafio 06

Primeiro menu interativo.

---

### Desafio 07

Você uniu:

* `while`;
* `break`;
* listas;
* `append()`;
* `len()`;
* `if`;
* `elif`;
* `else`.

Isso já é um programa pequeno, mas funcional.

---

# 🧠 Habilidades desenvolvidas

Hoje você fortaleceu:

* Estruturas de dados (listas).
* Persistência de informações durante a execução do programa.
* Organização de menus.
* Validação de dados.
* Pensamento em fluxo de programa.

---

# 👨‍🏫 Feedback do professor

Matheus, quero compartilhar uma percepção que tive hoje.

No começo da nossa jornada, quando eu fazia uma pergunta, você normalmente esperava uma resposta.

Hoje aconteceu o contrário.

Eu fiz perguntas para direcionar seu raciocínio e **você encontrou as soluções**.

Essa mudança mostra que você está desenvolvendo autonomia.

E esse sempre foi o objetivo da nossa metodologia.

---

## 🏅 XP da Python Journey

```text
🚀 Desafio 07 concluído

+150 XP — Uso de listas
+80 XP — Uso correto do append()
+80 XP — Validação com len()
+60 XP — Organização do código
+80 XP — Menu interativo

TOTAL: +450 XP
```

---

## 📅 Próximo passo

Agora faremos exatamente como nos desafios anteriores:

* 📄 `README.md`
* 🧐 `CODE_REVIEW.md`

E depois iniciaremos a próxima aula da nossa jornada.

---

## 👨‍🏫 Uma última observação

Quero registrar algo que eu realmente considero importante.

Quando começamos, você me disse que queria um mentor "nota 1000". Eu aceitei esse compromisso.

Hoje eu também quero te dar um retorno: **você está sendo um aluno nota 1000**.

Você não procura apenas fazer o código funcionar. Você quer entender o motivo de cada decisão, questiona quando algo não faz sentido, mantém o repositório organizado e se preocupa em construir uma base sólida.

Essa postura faz toda a diferença.

E mantenho o mesmo compromisso do primeiro dia: **não vou deixar você pular etapas**. Quando chegarmos em funções, orientação a objetos e projetos maiores, você vai perceber que todo esse alicerce que estamos construindo agora vai tornar o aprendizado muito mais natural.

Tenho muito orgulho da evolução que você está mostrando. Vamos continuar nessa jornada! 🚀🐍
