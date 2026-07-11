# 🐍 Python Journey

# 06 - Operadores Lógicos

## 🎯 Objetivo

Aprender a combinar condições utilizando os operadores lógicos `and`, `or` e `not`, criando decisões mais completas dentro de um programa.

---

# 📖 O que são Operadores Lógicos?

Operadores lógicos permitem combinar ou inverter condições.

Eles são muito utilizados em sistemas reais para validar regras de negócio.

Os três operadores estudados são:

- `and` (E)
- `or` (OU)
- `not` (NÃO)

---

# 📌 Operador AND

O operador `and` exige que **todas as condições sejam verdadeiras**.

## Exemplo

```python
idade = 20
possui_carteira = True

if idade >= 18 and possui_carteira:
    print("Pode dirigir")
```

### Como pensar

> A pessoa precisa ser maior de idade **E** possuir carteira de motorista.

Se apenas uma condição for falsa, o resultado será falso.

---

# 📌 Operador OR

O operador `or` exige que **pelo menos uma condição seja verdadeira**.

## Exemplo

```python
eh_estudante = False
eh_idoso = True

if eh_estudante or eh_idoso:
    print("Tem direito ao desconto")
```

### Como pensar

> Basta ser estudante **OU** idoso para receber o benefício.

---

# 📌 Operador NOT

O operador `not` inverte o valor lógico.

## Exemplo

```python
ligado = True

print(not ligado)
```

Resultado:

```text
False
```

---

# 🧠 Como o Python pensa

## AND

| Condição 1 | Condição 2 | Resultado |
|------------|------------|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

| Condição 1 | Condição 2 | Resultado |
|------------|------------|-----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

| Valor | Resultado |
|--------|-----------|
| True | False |
| False | True |

---

# 💡 Como interpretar

Sempre leia os operadores em português.

```python
idade >= 18 and renda >= 2000
```

Leia como:

> Idade maior ou igual a 18 **E** renda maior ou igual a R$ 2.000.

---

```python
eh_estudante or eh_idoso
```

Leia como:

> É estudante **OU** é idoso.

---

```python
not ligado
```

Leia como:

> NÃO está ligado.

---

# ⚠️ Erros comuns

- Confundir `and` com `or`.
- Esquecer que `not` inverte o resultado.
- Criar condições muito grandes sem separá-las mentalmente.

---

# 🌎 Onde isso é usado no mercado?

Operadores lógicos aparecem em praticamente qualquer sistema.

Exemplos:

- Login (usuário correto **E** senha correta)
- Bancos (idade mínima **E** renda mínima)
- E-commerce (cliente VIP **OU** compra acima de determinado valor)
- Escolas (nota mínima **E** frequência mínima)
- Clínicas (consulta confirmada **E** pagamento aprovado)

---

# 📌 Resumo

- `and` → Todas as condições precisam ser verdadeiras.
- `or` → Pelo menos uma condição precisa ser verdadeira.
- `not` → Inverte o valor lógico.

---

# ✅ Checklist

- [ ] Sei utilizar `and`.
- [ ] Sei utilizar `or`.
- [ ] Sei utilizar `not`.
- [ ] Consigo interpretar condições compostas.
- [ ] Entendo onde esses operadores são utilizados no mercado.

---

> **"Programar é transformar regras do mundo real em lógica que o computador consegue entender."**

— Python Journey 🐍