arquivo = open('lista_presenca.txt','a')

for _ in range(5):
    nome = input('Digite o nome do convidado: ').capitalize()
    arquivo.write(f'{nome}\n')

arquivo.close()

arquivo = open('lista_presenca.txt','r')
print('========== C O N V I D A D O S ==========')
for linha in arquivo:
    print(linha.strip())
    

arquivo.close()

