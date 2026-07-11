lista = []
  

while True:
    print('====== LISTA DE COMPRAS ======\n\n' \
    '1 - Adicionar produto\n' \
    '2 - Ver lista\n' \
    '3 - Sair\n')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        produto = input('O que deseja adicionar? ')
        lista.append(produto)

    elif opcao == '2':
        if len(lista) > 0:
            print(lista)

        else:
            print('A lista possui zero produtos')

    elif opcao == '3':
        print('Sistema encerrado')
        break

    else: 
        print('Opção invalida')

