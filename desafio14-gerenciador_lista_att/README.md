# 🧪 Laboratório de Escopo

## 📖 Sobre

Neste laboratório foi realizada a refatoração do Gerenciador de Compras para reduzir a dependência de variáveis globais.

As funções passaram a receber a lista de compras através de parâmetros.

---

# Objetivos

Praticar:

- Funções
- Parâmetros
- Escopo
- Organização de código
- Reutilização de funções

---

# Alterações realizadas

Antes:

```python
def adicionar_produto():
```

Depois:

```python
def adicionar_produto(lista):
```

---

Antes:

```python
lista_compras.append(item)
```

Depois:

```python
lista.append(item)
```

---

O mesmo conceito foi aplicado nas funções:

- alterar_produto()
- excluir_produto()
- mostrar_lista()

---

# Aprendizados

Compreendi que uma função não precisa conhecer diretamente uma variável global.

Recebendo a lista como parâmetro, a mesma função pode ser utilizada com diferentes listas.

---

# Python Journey

Este laboratório faz parte da minha jornada de estudos em Python, registrando a evolução dos conceitos aprendidos ao longo das aulas.

---

**Status:** ✅ Concluído