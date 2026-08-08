import csv

with open ('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')

    valor_geral = 0
    contador = 0

    for linha in leitor:
        preco = linha['preço'].replace(',','.')
        preco = float(preco)

        estoque = int(linha['estoque'])

        valor_total = preco * estoque

        valor_geral += valor_total
        contador += 1

    valor_medio = valor_geral / contador

    print('===== Valor do Estoque =====\n')
    print(f'Valor total do estoque: R$ {valor_geral:.2f}\n')
    print(f'Quantidade de produtos cadastrados: {contador}\n')
    print(f'Valor medio do estoque por produto: R$ {valor_medio:.2f}\n')
