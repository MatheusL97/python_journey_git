# 📚 ANOTACOES.md

# 📚 Aula 22 - Introdução aos Arquivos CSV

## 🎯 Objetivo

Aprender o que é um arquivo CSV, como ele é estruturado e como criar um arquivo CSV manualmente utilizando Python.

---

# O que é um arquivo CSV?

CSV significa:

> **Comma-Separated Values**

(Valores Separados por Vírgula)

É um arquivo de texto utilizado para armazenar dados organizados em linhas e colunas.

No Brasil, é muito comum utilizar o ponto e vírgula (`;`) como separador.

Exemplo:

```text
Nome;Preco;Estoque
Notebook;1800.00;5
Mouse;80.00;20
Teclado;150.00;10
```

Cada linha representa um registro.

Cada coluna representa uma informação.

---

# Diferença entre TXT e CSV

## Arquivo TXT

Não possui estrutura definida.

Pode conter qualquer texto.

Exemplo:

```text
Hoje estudei Python.
Amanhã estudarei Pandas.
```

---

## Arquivo CSV

Possui estrutura organizada em colunas.

Exemplo:

```text
Nome;Idade;Curso
Matheus;29;ADS
Carlos;22;Engenharia
```

---

# Modos de abertura

## Escrita

```python
open("arquivo.csv", "w")
```

Cria um novo arquivo ou substitui o conteúdo existente.

---

## Acrescentar

```python
open("arquivo.csv", "a")
```

Adiciona novas informações ao final do arquivo.

---

## Leitura

```python
open("arquivo.csv", "r")
```

Abre o arquivo para leitura.

---

# Escrevendo um cabeçalho

É uma boa prática adicionar um cabeçalho para identificar cada coluna.

Exemplo:

```python
cabecalho = "Nome;Preco;Estoque\n"

arquivo.write(cabecalho)
```

---

# Gravando registros

Cada registro deve terminar com:

```python
\n
```

Exemplo:

```python
arquivo.write(f"{nome};{valor:.2f};{estoque}\n")
```

Assim cada produto será salvo em uma nova linha.

---

# Formatação de números

Para exibir duas casas decimais:

```python
{valor:.2f}
```

Exemplo:

```
1800.00
```

---

# Lendo o arquivo

```python
for linha in arquivo:
    print(linha.strip())
```

O método `strip()` remove a quebra de linha antes da exibição.

---

# Fluxo do programa

```
Criar arquivo
        ↓
Escrever cabeçalho
        ↓
Cadastrar produtos
        ↓
Salvar informações
        ↓
Fechar arquivo
        ↓
Abrir novamente
        ↓
Ler linha por linha
```

---

# Aplicações do CSV

Arquivos CSV são utilizados para armazenar:

- cadastro de clientes;
- produtos;
- funcionários;
- vendas;
- estoque;
- notas fiscais;
- exportações de sistemas.

---

# Relação com Análise de Dados

Grande parte dos dados utilizados por Analistas de Dados chega em formato CSV.

Esses arquivos podem ser importados para:

- Python;
- Pandas;
- Excel;
- Power BI;
- Bancos de Dados.

---

# Aprendizados

Nesta aula aprendi:

- o que é um arquivo CSV;
- diferença entre TXT e CSV;
- criar um CSV manualmente;
- utilizar cabeçalhos;
- gravar registros utilizando `;`;
- utilizar os modos `w`, `a` e `r`;
- formatar números com duas casas decimais;
- percorrer um arquivo CSV linha por linha.