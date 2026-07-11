while True:
    print('\n====== MENU ======\n')
    print('1 - Fazer Pedido\n')
    print('2 - Ver cardapio\n')
    print('3 - Sair\n')
    opcao = input('Escolha uma opção: ')


    if opcao == '1':
        print('Pedido realizado!\n')

    elif opcao == '2':
        print('Cardapio: \n\n' \
        '-Hamburger \n' \
        '-Batata Frita\n' \
        '-Refrigerante')

    elif opcao == '3':
        print('Sistema ecenrrado')
        break

    else:
        print('Opção invalida')
