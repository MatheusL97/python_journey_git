# 📚 ANOTACOES.md

# 📚 Aula 21 - Leitura de Arquivos Linha por Linha

## 🎯 Objetivo

Aprender a percorrer arquivos de texto utilizando um laço `for`, entendendo como o Python realiza a leitura de cada linha.

---

# Revisão

Na aula anterior aprendemos:

```python
arquivo.read()
```

Esse método retorna todo o conteúdo do arquivo como uma única string.

---

# Lendo linha por linha

Também podemos percorrer um arquivo diretamente:

```python
arquivo = open("arquivo.txt", "r")

for linha in arquivo:
    print(linha)

arquivo.close()
```

Cada repetição do `for` representa uma linha do arquivo.

---

# O problema da quebra de linha

Ao utilizar:

```python
print(linha)
```

Podem aparecer linhas em branco.

Isso acontece porque cada linha do arquivo termina com:

```python
\n
```

---

# Removendo a quebra de linha

Utilizamos:

```python
linha.strip()
```

Exemplo:

```python
for linha in arquivo:
    print(linha.strip())
```

Agora o conteúdo é exibido corretamente.

---

# Escrevendo informações

Para salvar cada informação em uma nova linha:

```python
arquivo.write(f"{nome}\n")
```

Sem o `\n`, todas as informações seriam gravadas na mesma linha.

---

# Fechando o arquivo

Sempre devemos fechar o arquivo após terminar de utilizá-lo.

```python
arquivo.close()
```

---

# Cursor de leitura

Todo arquivo possui um cursor.

Quando utilizamos:

```python
for linha in arquivo:
```

O cursor percorre todas as linhas.

Após chegar ao final, não existem mais dados para serem lidos.

Por isso, não devemos misturar:

```python
arquivo.read()
```

com

```python
for linha in arquivo:
```

na mesma leitura.

---

# Fluxo de leitura

```
Abrir arquivo
        ↓
Percorrer linha por linha
        ↓
Remover "\n" com strip()
        ↓
Fechar arquivo
```

---

# Aprendizados

Nesta aula aprendi:

- percorrer arquivos utilizando `for`;
- utilizar `.strip()`;
- salvar uma informação por linha;
- entender o funcionamento do cursor de leitura;
- evitar misturar `read()` com `for linha in arquivo`.