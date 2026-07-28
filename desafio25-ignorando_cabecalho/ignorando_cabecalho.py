import csv

with open ('produtos_estoque.csv','r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    next(leitor)

    contador = 0
    for linha in leitor:
        print(f'Produto: {linha[0]}\nPreço: {linha[1]}\nEstoque: {linha[2]}\n{10*'-'}')
        contador += 1

print(f'TOTAL DE PRODUTOS CADASTRAODS: {contador}')