# 📚 ANOTACOES.md

# 📚 Aula 14 - Módulos (import)

## 🎯 Objetivo

Aprender a dividir um programa em vários arquivos utilizando módulos (`import`), tornando o código mais organizado e reutilizável.

---

# O que é um módulo?

Um módulo é um arquivo Python (`.py`) que pode conter:

- funções;
- variáveis;
- classes;
- constantes.

Esses recursos podem ser utilizados em outros arquivos através do comando `import`.

---

# Exemplo

Arquivo:

```python
calculadora.py
```

```python
def somar(a, b):
    return a + b
```

Outro arquivo:

```python
import calculadora

resultado = calculadora.somar(5, 3)

print(resultado)
```

Saída:

```
8
```

---

# Importando apenas uma função

Também é possível importar apenas uma função.

```python
from calculadora import somar
```

Agora basta utilizar:

```python
resultado = somar(5, 3)
```

Sem escrever:

```python
calculadora.somar()
```

---

# Diferença

## Importando o módulo inteiro

```python
import calculadora
```

Uso:

```python
calculadora.somar()
```

---

## Importando apenas uma função

```python
from calculadora import somar
```

Uso:

```python
somar()
```

---

# Vantagens dos módulos

- Organização do projeto;
- Reutilização de código;
- Evita copiar funções;
- Facilita manutenção;
- Facilita localização de erros;
- Código mais limpo (Clean Code).

---

# Organização de projetos

Exemplo:

```
projeto/

│

├── main.py

├── calculadora.py

├── clientes.py

├── produtos.py

└── vendas.py
```

Cada arquivo possui uma responsabilidade.

---

# Aprendizados

Nesta aula aprendi:

- o que é um módulo;
- como utilizar `import`;
- como importar apenas funções específicas;
- como dividir um projeto em vários arquivos;
- a importância da organização do código.