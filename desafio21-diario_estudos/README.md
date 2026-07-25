# 🚀 README.md

# Desafio 20 - Diário de Estudos

## 📖 Sobre

Neste desafio foi desenvolvido um pequeno sistema capaz de registrar os estudos do usuário em um arquivo de texto.

As informações permanecem salvas mesmo após o encerramento do programa.

Além disso, o sistema lê o arquivo e exibe todo o histórico de estudos.

---

## Funcionalidades

- Solicitar nome do usuário;
- Solicitar o assunto estudado;
- Salvar as informações em um arquivo `.txt`;
- Manter os registros anteriores;
- Ler o arquivo completo;
- Exibir o histórico na tela.

---

## Conceitos praticados

✔ `open()`

✔ Modo `"a"`

✔ Modo `"r"`

✔ `.write()`

✔ `.read()`

✔ `.close()`

✔ f-strings

✔ Quebra de linha (`\n`)

---

## Funcionamento

O programa realiza os seguintes passos:

1. Solicita o nome do usuário.

2. Solicita o conteúdo estudado.

3. Abre o arquivo em modo de acréscimo.

4. Salva as informações.

5. Fecha o arquivo.

6. Reabre o arquivo em modo leitura.

7. Exibe todo o histórico salvo.

---

## Exemplo de saída

```
Nome: Matheus
Estudou: Manipulação de Arquivos

-----------------------------

Nome: Carlos
Estudou: Dicionários

-----------------------------
```

---

## Aprendizados

Este desafio mostrou como criar programas que armazenam informações de forma permanente.

Esse conhecimento será utilizado futuramente para trabalhar com arquivos CSV, Pandas e bancos de dados.

---

## Python Journey

Projeto desenvolvido durante a Python Journey.

---

## Status

✅ Desafio concluído.