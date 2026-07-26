arquivo = open('produtos.csv','w')

cabecalho = 'Nome;Preco;Estoque\n'
arquivo.write(cabecalho)

for _ in range(3):
    nome = input('digite o nome do produto: ').capitalize()
    valor = float(input('digite o valor do produto: '))
    estoque = int(input('digite a quantidade do produto no estoque: '))
    print(10*'-')
    arquivo.write(f'{nome};{valor:.2f};{estoque}\n')

arquivo.close()

arquivo = open('produtos.csv','r')

for linha in arquivo:
    print(linha.strip())

