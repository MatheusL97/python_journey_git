arquivo = open('diario_estudos.txt','a')

nome = input('Digite seu nome: ').capitalize()

estudo = input('O que estudou hoje: ')


arquivo.write(f'Nome: {nome}\n')
arquivo.write(f'Estudou: {estudo}\n')
arquivo.write('\n-----------------------------')

arquivo.close()

arquivo = open('diario_estudos.txt','r')
conteudo = arquivo.read()
print(conteudo)

arquivo.close()

