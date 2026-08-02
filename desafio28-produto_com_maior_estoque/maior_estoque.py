import csv

with open ('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')

    maior_estoque = None
    produto_maior = ''
    menor_estoque = None
    produto_menor = ''

    for linha in leitor:
        estoque = int(linha['estoque'])

        if maior_estoque is None or estoque > maior_estoque:
            maior_estoque = estoque
            produto_maior = linha['nome']

        if menor_estoque is None or estoque < menor_estoque:
            menor_estoque = estoque
            produto_menor = linha['nome']
 
    print(5*'=',' ESTOQUE MAIOR ',5*'=')
    print(produto_maior)
    print(maior_estoque)
    print()
    print(5*'=',' ESTOQUE MENOR ',5*'=')    
    print(produto_menor)
    print(menor_estoque)