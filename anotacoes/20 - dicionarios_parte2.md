# 📚 ANOTACOES.md

# 📚 Aula 17 - Dicionários (Parte 2)

## 🎯 Objetivo

Aprender novos métodos dos dicionários e entender como tratar informações opcionais utilizando `get()`.

---

# Método get()

O método `get()` permite acessar uma chave sem gerar erro caso ela não exista.

Sintaxe:

```python
dicionario.get("chave")
```

Exemplo:

```python
aluno = {
    "nome": "Matheus"
}

print(aluno.get("idade"))
```

Saída:

```
None
```

---

# Valor padrão

Também podemos informar um valor padrão.

```python
print(aluno.get("idade", "Não informado"))
```

Saída:

```
Não informado
```

---

# Diferença entre [] e get()

Utilizando:

```python
aluno["idade"]
```

Se a chave não existir:

```
KeyError
```

Utilizando:

```python
aluno.get("idade")
```

Retorna:

```
None
```

Sem gerar erro.

---

# Adicionando uma nova chave

Podemos criar novas informações após criar o dicionário.

```python
aluno["telefone"] = "(61)99999-9999"
```

O dicionário passa a possuir essa nova chave.

---

# Método items()

Retorna simultaneamente:

- chave
- valor

Exemplo:

```python
for chave, valor in aluno.items():
    print(chave, valor)
```

---

# Método keys()

Retorna apenas as chaves.

```python
for chave in aluno.keys():
    print(chave)
```

---

# Método values()

Retorna apenas os valores.

```python
for valor in aluno.values():
    print(valor)
```

---

# Quando utilizar get()

Sempre que uma informação puder ser opcional.

Exemplos:

- telefone
- complemento do endereço
- segundo sobrenome
- observações

Assim evitamos erros durante a execução do programa.

---

# Aprendizados

Nesta aula aprendi:

- utilizar o método `get()`;
- adicionar novas chaves em um dicionário;
- tratar informações opcionais;
- evitar `KeyError`;
- percorrer um dicionário utilizando `.items()`;
- compreender a diferença entre acessar uma chave diretamente e utilizar `get()`.