import csv

with open ('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')


    maior_preco = None
    produto_mais_caro = ''
    menor_preco = None
    produto_mais_barato = ''


    for linha in leitor:
        preco = linha['preço'].replace(',','.')
        preco = float(preco)

        if maior_preco is None or preco > maior_preco:
            maior_preco = preco
            produto_mais_caro = linha['nome']
        
        if menor_preco is None or preco < menor_preco:
            menor_preco = preco
            produto_mais_barato = linha['nome']

    print(5*'=',' PREÇO MAIOR ',5*'=')
    print(produto_mais_caro)
    print(maior_preco)
    print()
    print(5*'=',' PREÇO MENOR ',5*'=')    
    print(produto_mais_barato)
    print(menor_preco)
    print()
    print(5*'=',' DIFERENÇA DE VALOR ',5*'=')    
    print(maior_preco-menor_preco)



         

    