listas = []

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
        listas.append(item)
        print('Item adicionado com sucesso!')

    elif opcao == '2':
        posicao = input('Qual a posição do item que deseja alterar, sendo 0 o primeira posição. ')
        posicao = int(posicao)
        item = input('Digite o novo nome do item que desaja alterar: ')
        listas[posicao] = item
        print('Item alterado com sucesso!')

    elif opcao == '3':
        posicao = input('Qual a posição do item que deseja excluir, sendo 0 o primeira posição. ')
        posicao = int(posicao)
        listas.pop(posicao)
        print('Item excluido com sucesso!')
    
    elif opcao == '4':
        if len(listas) > 0:
            for item in listas:
                print(f'- {item}')
        else: 
            print('Nehum produto cadastrado')
    
    elif opcao == '5':
        print('Sistema Encerrado!')
        break

    else:
        print('Voce nao digitou uma opção valida!')
