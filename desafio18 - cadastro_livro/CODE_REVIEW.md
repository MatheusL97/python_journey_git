# 🧐 CODE_REVIEW.md

# Code Review - Desafio 18

## Objetivo

Desenvolver um programa utilizando **dicionários** para cadastrar um livro e exibir todas as suas informações.

---

# Pontos positivos

## Organização

O programa foi dividido em duas partes bem definidas:

- Coleta das informações do usuário;
- Exibição dos dados através de uma função.

Essa separação deixa o código mais organizado e facilita futuras alterações.

---

## Utilização de Dicionários

O cadastro foi armazenado corretamente utilizando um dicionário.

```python
livro = {
    'titulo': titulo,
    'autor': autor,
    'editora': editora,
    'ano': ano,
    'paginas': pagina,
    'genero': genero
}
```

Essa é a estrutura ideal para representar um cadastro.

---

## Tipos de Dados

Os campos numéricos foram convertidos corretamente utilizando:

```python
int()
```

Isso garante que:

- Ano seja armazenado como número.
- Quantidade de páginas também seja armazenada como número.

Essa é uma boa prática de programação.

---

## Utilização de Funções

Foi criada a função:

```python
def livro_cadastrado(livro):
```

A função recebe o dicionário como parâmetro, tornando-a reutilizável e independente de variáveis globais.

Essa organização segue um padrão bastante utilizado no desenvolvimento profissional.

---

## Utilização do items()

Foi utilizado corretamente:

```python
for chave, valor in livro.items():
```

Esse recurso permite percorrer todas as informações do dicionário sem necessidade de acessar cada chave individualmente.

---

## Utilização do capitalize()

Foi utilizado corretamente apenas na chave.

```python
chave.capitalize()
```

Essa escolha melhora a apresentação das informações sem causar problemas com os valores numéricos.

---

# Melhorias sugeridas

## Nome da Função

O nome:

```python
livro_cadastrado()
```

está correto.

Como sugestão de nomenclatura, também poderia ser utilizado:

```python
mostrar_livro()
```

pois a função apenas exibe informações.

Entretanto, o nome escolhido também representa bem sua finalidade.

---

## Formatação do print

Hoje o código utiliza:

```python
print(f'{chave.capitalize()}:', f'{valor}\n')
```

Também poderia ser escrito como:

```python
print(f"{chave.capitalize()}: {valor}\n")
```

Essa forma deixa a linha um pouco mais simples e elimina a necessidade de dois argumentos no `print()`.

---

## Organização dos dados

No futuro, quando aprendermos listas de dicionários, será possível armazenar vários livros utilizando exatamente essa mesma estrutura.

Isso permitirá transformar este programa em um pequeno sistema de biblioteca.

---

# Avaliação

| Critério | Resultado |
|----------|-----------|
| Dicionários | ⭐⭐⭐⭐⭐ |
| Funções | ⭐⭐⭐⭐⭐ |
| Organização | ⭐⭐⭐⭐⭐ |
| Uso do `.items()` | ⭐⭐⭐⭐⭐ |
| Tipos de Dados | ⭐⭐⭐⭐⭐ |
| Clareza | ⭐⭐⭐⭐⭐ |

---

# Nota Final

**10 / 10**

Excelente implementação.

Todos os objetivos da aula foram atingidos.

---

## 👨‍🏫 Comentário do Professor

Este desafio mostrou um bom domínio dos conceitos apresentados na aula.

O programa utiliza corretamente um dicionário para representar um cadastro, organiza a exibição das informações em uma função e faz uso do método `.items()` para percorrer todas as informações de forma elegante.

Outro ponto positivo foi a preocupação em armazenar os dados numéricos utilizando o tipo `int`, demonstrando atenção aos tipos de dados e às boas práticas de programação.

Continue seguindo esse padrão de organização. Ele será muito útil nos próximos projetos da Python Journey.