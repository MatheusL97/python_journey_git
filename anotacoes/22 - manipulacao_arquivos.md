# 📚 ANOTACOES.md

# 📚 Aula 20 - Manipulação de Arquivos (.txt)

## 🎯 Objetivo

Aprender a criar, escrever, ler e salvar informações em arquivos de texto utilizando Python.

---

# O que é um arquivo?

Um arquivo é uma forma de armazenar informações permanentemente no computador.

Diferente das variáveis, os dados continuam existindo mesmo após fechar o programa.

---

# Abrindo um arquivo

Utilizamos a função:

```python
open()
```

Exemplo:

```python
arquivo = open("dados.txt", "w")
```

---

# Modos de abertura

## Leitura

```python
"r"
```

Abre um arquivo existente para leitura.

---

## Escrita

```python
"w"
```

Cria um novo arquivo ou sobrescreve um arquivo existente.

---

## Acrescentar

```python
"a"
```

Adiciona novas informações ao final do arquivo sem apagar o conteúdo anterior.

---

# Escrevendo informações

Utilizamos:

```python
arquivo.write()
```

Exemplo:

```python
arquivo.write("Olá Mundo")
```

---

# Escrevendo variáveis

```python
arquivo.write(f"Nome: {nome}\n")
```

O `\n` realiza a quebra de linha.

---

# Lendo um arquivo

```python
conteudo = arquivo.read()
```

Depois podemos mostrar:

```python
print(conteudo)
```

---

# Fechando o arquivo

Sempre utilize:

```python
arquivo.close()
```

Isso garante que todas as alterações sejam gravadas corretamente.

---

# Fluxo de trabalho

```
Abrir arquivo
        ↓
Escrever ou Ler
        ↓
Fechar arquivo
```

---

# Aprendizados

Nesta aula aprendi:

- utilizar `open()`;
- abrir arquivos em diferentes modos;
- escrever utilizando `.write()`;
- ler utilizando `.read()`;
- utilizar `\n`;
- fechar arquivos com `.close()`;
- salvar dados permanentemente.