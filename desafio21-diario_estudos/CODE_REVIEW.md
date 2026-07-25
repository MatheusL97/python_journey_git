# 🔍 CODE_REVIEW.md

# Code Review - Desafio 20

## Avaliação Geral

⭐ Nota: **10 / 10**

Excelente trabalho.

O programa foi desenvolvido corretamente e cumpriu todos os requisitos do desafio.

Além disso, foi realizado o desafio extra, lendo e exibindo o conteúdo do arquivo.

---

# Pontos positivos

✔ Utilização correta da função `open()`.

✔ Escolha correta do modo `"a"` para preservar os registros anteriores.

✔ Escrita organizada utilizando `.write()`.

✔ Uso correto das f-strings.

✔ Utilização adequada de `\n` para organizar o arquivo.

✔ Fechamento do arquivo após a escrita.

✔ Reabertura em modo leitura.

✔ Utilização correta de `.read()`.

✔ Código organizado em etapas de fácil compreensão.

---

# Sugestão de melhoria

Após realizar a leitura do arquivo, recomenda-se também utilizar:

```python
arquivo.close()
```

Embora o programa funcione normalmente, essa é uma boa prática para liberar os recursos utilizados pelo arquivo.

---

# O que foi aprendido

Durante este desafio foram consolidados os seguintes conceitos:

- abertura de arquivos;
- modos de abertura (`r`, `w`, `a`);
- escrita em arquivos;
- leitura de arquivos;
- persistência de dados;
- utilização de `\n`;
- boas práticas ao trabalhar com arquivos.

---

# Comentário do professor

Este desafio representa uma evolução importante na Python Journey.

Foi o primeiro contato com persistência de dados, permitindo que as informações continuem disponíveis mesmo após o encerramento do programa.

Esse conhecimento servirá como base para o trabalho com arquivos CSV, bibliotecas como Pandas e, posteriormente, bancos de dados relacionais.

O código apresentou boa organização, leitura simples e utilização correta dos principais recursos estudados.

Parabéns pelo excelente desempenho!