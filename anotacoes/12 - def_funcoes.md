# 📚 Aula 12 - Funções (`def`)

## 🎯 Objetivo

Aprender a criar funções utilizando a palavra-chave `def`, organizando melhor os programas e evitando repetição de código.

As funções permitem dividir um programa em pequenas tarefas, tornando o código mais limpo, organizado e fácil de manter.

---

# 📖 O problema

Até agora todos os programas foram escritos em um único bloco.

Exemplo:

```python
print("1 - Adicionar")
print("2 - Remover")
print("3 - Sair")

opcao = input("Escolha uma opção: ")
```

Conforme o programa cresce, fica mais difícil localizar erros e adicionar novas funcionalidades.

---

# 🤔 O que é uma função?

Uma função é um bloco de código responsável por executar uma tarefa específica.

Ela é criada uma única vez e pode ser utilizada sempre que necessário.

---

# 📦 Estrutura

```python
def nome_da_funcao():
    print("Olá!")
```

A palavra `def` significa que estamos criando uma função.

---

# Executando uma função

Criar uma função não significa executá-la.

Exemplo:

```python
def saudacao():
    print("Olá!")
```

Nesse momento nada será exibido.

Para executar:

```python
saudacao()
```

Resultado:

```text
Olá!
```

---

# Exemplo

```python
def mostrar_menu():
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Sair")
```

Executando:

```python
mostrar_menu()
```

---

# Vantagens

Utilizando funções:

- evita repetição de código;
- melhora a organização;
- facilita manutenção;
- facilita encontrar erros;
- aumenta a reutilização de código.

---

# Boas práticas

Escolha nomes que descrevam a função.

Correto:

```python
mostrar_menu()
```

```python
adicionar_produto()
```

```python
mostrar_lista()
```

Evite:

```python
teste()
```

```python
abc()
```

```python
funcao1()
```

---

# Conceitos estudados

Nesta aula aprendi:

- criar funções;
- executar funções;
- organizar programas;
- reutilizar código;
- utilizar `def`.

---

# Erros comuns

## Criar a função e esquecer de chamá-la

Errado:

```python
def ola():
    print("Olá!")
```

Correto:

```python
def ola():
    print("Olá!")

ola()
```

---

## Criar funções dentro do `while`

As funções devem ser criadas antes do laço principal.

Estrutura correta:

```python
lista = []

def mostrar_menu():
    ...

while True:
    ...
```

---

# Resumo

Nesta aula aprendi:

- o que é uma função;
- como criar uma função;
- como executar uma função;
- por que organizar o código em funções;
- importância da reutilização de código.

---

# Conclusão

As funções representam um dos pilares da programação.

Elas tornam os programas mais organizados, facilitam a manutenção e permitem reutilizar código sempre que necessário.

---

## 👨‍🏫 Anotação do professor

Uma função deve ter apenas uma responsabilidade.

Quanto menores e mais organizadas forem as funções, mais fácil será evoluir o programa futuramente.

A partir desta aula, praticamente todos os projetos da Python Journey utilizarão funções.