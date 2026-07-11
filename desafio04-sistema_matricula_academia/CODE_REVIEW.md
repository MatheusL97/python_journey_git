# 🥹 Matheus...

Antes de fazer a revisão...

Quero te falar uma coisa.

**Esse foi o primeiro desafio em que eu realmente senti que você está programando.**

Não copiando.

Não tentando lembrar de um vídeo.

Programando.

E isso é muito legal de ver.

Agora vamos fazer nosso **Code Review**.

---

# 📋 Seu código

```python
nome_aluno = input('Digite o nome do aluno: ')
idade_aluno = input('Digite a idade do aluno: ')
idade_aluno = int(idade_aluno)
possui_atestado = input('O aluno possui atestado medico? Responda somente com "sim" ou "nao". ')

if idade_aluno >= 16 and possui_atestado == 'sim':
    print(f'O aluno {nome_aluno} está apto a participar da turma especial de musculação.')

elif idade_aluno < 16 or possui_atestado == 'nao':
    print(f'O aluno {nome_aluno} não está apto a participar da turma especial de musculação.')

else:
    print('Você nao digitou sim ou não.')
```

---

# 🟢 O que ficou excelente

## 1. Organização

⭐⭐⭐⭐⭐

Você organizou em blocos:

* Entrada
* Processamento
* Saída

Muito bom.

---

## 2. Nome das variáveis

```python
nome_aluno
idade_aluno
possui_atestado
```

⭐⭐⭐⭐⭐

São nomes claros.

Quem lê o código entende imediatamente.

---

## 3. Uso do `and`

Você utilizou exatamente onde precisava.

```python
if idade_aluno >= 16 and possui_atestado == 'sim':
```

⭐⭐⭐⭐⭐

Perfeito.

---

## 4. Mensagens para o usuário

Gostei muito.

Você utilizou **f-string** corretamente.

```python
print(f'O aluno {nome_aluno}...')
```

Isso já deixa o código mais profissional.

---

# 🟡 Agora vamos melhorar.

## Ponto 1

Você escreveu:

```python
elif idade_aluno < 16 or possui_atestado == 'nao':
```

Funciona?

**Sim.**

Mas deixa eu te ensinar algo muito importante.

---

Depois do primeiro `if`, o Python já sabe que a condição abaixo **não foi satisfeita**.

Ou seja.

Se não entrou aqui:

```python
idade >= 16 and possui_atestado == "sim"
```

Significa que alguma das condições falhou.

Então, para o seu programa, bastaria escrever:

```python
else:
    print(...)
```

Percebe?

Você não precisaria verificar tudo novamente.

---

# Então por que existe o seu último `else`?

Você criou:

```python
else:
    print("Você não digitou sim ou não.")
```

E aqui encontramos um detalhe interessante.

Imagine que o usuário digite:

```text
SIM
```

Maiúsculo.

Ou:

```text
Sim
```

O programa cairia nesse `else`.

Mas ele também cairia se digitasse:

```text
banana
```

😂

Então esse `else` está tentando validar uma entrada do usuário.

Só que ainda não aprendemos a fazer validação corretamente.

Vamos aprender isso na aula de **tratamento de erros**.

---

# Como eu faria hoje?

Como ainda estamos no início do curso, eu escreveria apenas:

```python
if idade_aluno >= 16 and possui_atestado == "sim":
    print(...)

else:
    print(...)
```

Mais simples.

Mais limpo.

---

# 🧠 Mas...

Você teve uma preocupação que me chamou atenção.

Você pensou:

> "E se o usuário digitar algo diferente?"

Isso é pensamento de desenvolvedor.

Mesmo que a solução ainda não seja a ideal, a pergunta foi excelente.

---

# 💡 Uma pequena melhoria (opcional)

Existe um método das strings chamado `lower()`.

Por exemplo:

```python
possui_atestado = input(...).lower()
```

Assim:

```text
SIM
```

vira:

```text
sim
```

E:

```text
Sim
```

também vira:

```text
sim
```

Isso evita muitos problemas.

**Mas ainda não estudamos métodos de strings**, então eu prefiro deixar isso para a aula certa. Só queria plantar essa sementinha para você.

---

# 📊 Avaliação

| Critério           | Nota  |
| ------------------ | ----- |
| Organização        | ⭐⭐⭐⭐⭐ |
| Variáveis          | ⭐⭐⭐⭐⭐ |
| Operadores Lógicos | ⭐⭐⭐⭐⭐ |
| Legibilidade       | ⭐⭐⭐⭐⭐ |
| Lógica             | ⭐⭐⭐⭐☆ |

## Nota Final

# **9,9 / 10**

Só não dou 10 porque seu `elif` acabou fazendo uma verificação que poderia ser simplificada.

E isso é uma questão de refinamento, não de erro grave.

---

# 🏆 XP

```text
Desafio concluído

+120 XP

Boa organização

+40 XP

Uso correto do AND

+40 XP

Boa nomenclatura

+30 XP

Excelente raciocínio

+50 XP

TOTAL

280 XP
```

---

# 📈 Sua evolução (e isso me deixou muito feliz)

Olha a diferença entre os seus primeiros códigos e os de agora:

### Antes

```python
numero1 = input(...)
numero1 = int(numero1)
```

Sem muito planejamento.

---

### Agora

Você faz naturalmente:

* Planejamento (IPO)
* Algoritmo
* Código
* Code Review
* Correção

Você percebe que esse já virou o seu processo?

Isso é exatamente o que eu queria construir.

---

# 📅 Nosso próximo passo

Agora que você domina:

* ✅ Variáveis
* ✅ `input()`
* ✅ `print()`
* ✅ `if`
* ✅ `elif`
* ✅ `else`
* ✅ `and`
* ✅ `or`
* ✅ `not`

O próximo grande passo será aprender a fazer **o programa repetir ações**, sem copiar e colar código.

Esse é um divisor de águas em Python.

Vamos entrar no mundo do **`while`**.

---

## 🧑‍🏫 E um pedido do seu professor

Matheus, antes de encerrarmos por hoje, quero te pedir uma coisa.

**Nunca apague os códigos antigos.**

Mesmo aqueles que você considerar "feios".

Daqui a seis meses, quero que você abra o código da calculadora e compare com o que estará escrevendo.

Você vai perceber sua evolução de uma forma que nenhuma nota consegue mostrar.

E isso é extremamente motivador.

---

Parabéns pelo **Desafio 04**.

**Status: ✅ Concluído.**

Você está construindo uma base muito sólida, e isso vai fazer toda a diferença quando chegarmos em projetos maiores. Tenho muito orgulho da forma como você está encarando essa jornada. Vamos continuar! 🚀🐍
