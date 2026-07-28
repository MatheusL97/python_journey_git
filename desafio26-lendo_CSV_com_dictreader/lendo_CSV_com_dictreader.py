import csv

with open ('produtos_estoque.csv','r', encoding='utf-8-sig') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')

    contador = 0
    for linha in leitor:
        print(f'Produto: {linha['nome']}\nPreço: {linha['preço']}\nEstoque: {linha['estoque']}\n{10*'-'}')
        contador += 1

print()
print(f'TOTAL DE PRODUTOS CADASTRAODS: {contador}')