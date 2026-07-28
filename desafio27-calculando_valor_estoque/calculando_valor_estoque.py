import csv

with open ('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')

    valor_geral = 0
    contador = 0
    for linha in leitor:
        preco = linha['preço'].replace(',','.')
        preco = float(preco)
        estoque = int(linha['estoque'])
        valor_total = preco*estoque
        print(f'Produto: {linha['nome']}\nPreço: {linha['preço']}\nEstoque: {linha['estoque']}\nValor em estoque: {valor_total}\n{10*'-'}')
        contador += 1
        valor_geral += valor_total

print()
print(f'TOTAL DE PRODUTOS CADASTRADOS: {contador}')
print(f'VALOR TOTAL DO ESTOQUE DA LOJA: {valor_geral:.2f}')
