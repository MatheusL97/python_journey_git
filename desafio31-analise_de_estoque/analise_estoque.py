import csv

with open('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo,delimiter=';')

    estoque_baixo = 0
    estoque_normal = 0
    estoque_alto = 0

    print('===== ANALISE DE ESTOQUE =====\n')

    for linha in leitor:
        estoque = int(linha['estoque'])

        if estoque < 20:
            print(f'Produto: {linha['nome']}')
            print(f'Estoque: {linha['estoque']}')
            print('Situação: Estoque baixo')
            print(20*'-')
            estoque_baixo += 1


        elif estoque < 50:
            print(f'Produto: {linha['nome']}')
            print(f'Estoque: {linha['estoque']}')
            print('Situação: Estoque normal')  
            print(20*'-')
            estoque_normal += 1


        else:
            print(f'Produto: {linha['nome']}')
            print(f'Estoque: {linha['estoque']}')
            print('Situação: Estoque alto')
            print(20*'-')
            estoque_alto += 1

    print('===== RESUMO =====')
    print(f'Estoque baixo: {estoque_baixo} produtos')
    print(f'Estoque normal: {estoque_normal} produtos')
    print(f'Estoque alto: {estoque_alto} produtos')
    print(20*'-')

    if estoque_baixo > estoque_normal and estoque_baixo > estoque_alto:
        print('\nO estoque baixo tem a maior quantidade de produtos.')

    elif estoque_normal > estoque_baixo and estoque_normal > estoque_alto:
        print('\nO estoque normal tem a maior quantidade de produtos.')

    elif estoque_alto > estoque_baixo and estoque_alto > estoque_normal:
        print('\nO estoque alto tem a maior quantidade de produtos.')
