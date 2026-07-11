lista_compras = []

while True:
    print('====== GERENCIADOR DE COMPRAS ======\n\n' \
    '1 - Adicionar produto\n' \
    '2 - Alterar produto\n' \
    '3 - Remover produto\n' \
    '4 - Ver lista\n' \
    '5 - Sair\n')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        item = input('Qual item deseja adicionar? ')
        lista_compras.append(item)
        print('Item adicionado com sucesso!')

    elif opcao == '2':
        posicao = input('Qual a posição do item que deseja alterar, sendo 0 o primeira posição. ')
        posicao = int(posicao)
        item = input('Digite o novo nome do item que desaja alterar: ')
        lista_compras[posicao] = item
        print('Item alterado com sucesso!')

    elif opcao == '3':
        posicao = input('Qual a posição do item que deseja excluir, sendo 0 o primeira posição. ')
        posicao = int(posicao)
        lista_compras.pop(posicao)
        print('Item excluido com sucesso!')
    
    elif opcao == '4':
        if len(lista_compras) > 0:
            for indice, item in enumerate(lista_compras):
                print(f'{indice} - {item}')
        else: 
            print('Nehum produto cadastrado')
    
    elif opcao == '5':
        print('Sistema Encerrado!')
        break

    else:
        print('Voce nao digitou uma opção valida!')
