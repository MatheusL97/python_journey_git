# 🚀 Desafio 06 - Menu Interativo

## 📖 Sobre o desafio

Neste desafio, o objetivo foi desenvolver um menu interativo utilizando o laço de repetição `while` juntamente com a instrução `break`.

O programa deve permanecer em execução até que o usuário escolha a opção de sair, simulando o comportamento de diversos sistemas encontrados no mercado.

---

# 📚 Cenário

Imagine que você foi contratado para desenvolver um pequeno sistema para uma lanchonete.

O atendente precisa acessar um menu simples para realizar algumas operações.

Enquanto a opção **Sair** não for escolhida, o sistema deverá continuar exibindo o menu.

---

# 🎯 Objetivos de aprendizagem

Durante este desafio pratiquei:

* Estrutura de repetição `while`
* Utilização do `break`
* Estruturas condicionais (`if`, `elif` e `else`)
* Organização da lógica de um menu
* Planejamento utilizando o método IPO

---

# 📋 Regras

O programa deverá apresentar o seguinte menu:

```text
====== MENU ======

1 - Fazer Pedido
2 - Ver Cardápio
3 - Sair
```

### Opção 1

Exibir:

```text
Pedido realizado!
```

### Opção 2

Exibir:

```text
Cardápio

- Hambúrguer
- Batata Frita
- Refrigerante
```

### Opção 3

Exibir:

```text
Sistema encerrado.
```

Encerrar o programa utilizando `break`.

### Qualquer outra opção

Exibir:

```text
Opção inválida.
```

Após isso, o menu deverá ser exibido novamente.

---

# 💻 Exemplo de execução

```text
====== MENU ======

1 - Fazer Pedido
2 - Ver Cardápio
3 - Sair

Escolha uma opção: 2

Cardápio

- Hambúrguer
- Batata Frita
- Refrigerante

====== MENU ======

1 - Fazer Pedido
2 - Ver Cardápio
3 - Sair

Escolha uma opção: 3

Sistema encerrado.
```

---

# 🧠 Planejamento (IPO)

## Input (Entrada)

* Opção escolhida pelo usuário.

## Process (Processamento)

* Exibir o menu.
* Ler a opção digitada.
* Executar a ação correspondente.
* Repetir o processo até que a opção **3** seja escolhida.

## Output (Saída)

* Pedido realizado.
* Cardápio.
* Opção inválida.
* Sistema encerrado.

---

# 📚 Conceitos utilizados

* Variáveis
* `print()`
* `input()`
* `while`
* `break`
* `if`
* `elif`
* `else`

---

# 📂 Estrutura do projeto

```text
desafio-06-menu-interativo/
│
├── README.md
├── codigo.py
├── CODE_REVIEW.md
└── assets/
```

---

# 💭 Aprendizados

Neste desafio aprendi que um único laço de repetição pode controlar todo o funcionamento de um sistema baseado em menus.

Também compreendi que o comando `break` permite interromper imediatamente o laço quando uma determinada condição é atendida.

---

# 🚀 Próximos passos

Os próximos desafios irão introduzir novos conceitos da linguagem Python, tornando os programas cada vez mais próximos de aplicações reais.

---

# 🐍 Python Journey

Este desafio faz parte da minha jornada de estudos em Python.

O objetivo deste repositório é documentar minha evolução como desenvolvedor, registrando cada aprendizado, desafio e projeto desenvolvido ao longo dos estudos.

---

## 👨‍🏫 Mentoria

Este desafio foi desenvolvido seguindo uma metodologia baseada em:

* Planejamento antes da implementação.
* Resolução de problemas.
* Revisão de código (Code Review).
* Organização do projeto.
* Boas práticas de programação.

Cada desafio representa mais um passo na construção da minha base como futuro desenvolvedor Python.

---

**Status:** ✅ Concluído
