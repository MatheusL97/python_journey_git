
lista_compras = []

def mostrar_menu():
    print('====== GERENCIADOR DE COMPRAS ======\n\n' \
    '1 - Adicionar produto\n' \
    '2 - Alterar produto\n' \
    '3 - Remover produto\n' \
    '4 - Ver lista\n' \
    '5 - Sair\n')

def adicionar_produto(lista):
    item = input('Qual item deseja adicionar? ')
    lista.append(item)
    print('Item adicionado com sucesso!')

def alterar_produto(lista):
    posicao = input('Qual a posição do item que deseja alterar, sendo 0 o primeira posição. ')
    posicao = int(posicao)
    item = input('Digite o novo nome do item que desaja alterar: ')
    lista[posicao] = item
    print('Item alterado com sucesso!')

def excluir_produto(lista):
    posicao = input('Qual a posição do item que deseja excluir, sendo 0 o primeira posição. ')
    posicao = int(posicao)
    lista.pop(posicao)
    print('Item excluido com sucesso!')

def mostrar_lista(lista):
    if len(lista) > 0:
        for indice, item in enumerate(lista_compras):
            print(f'{indice} - {item}')
    else: 
        print('Nehum produto cadastrado')

def encerrar():
    print('Sistema Encerrado!')
        
def digito_invalido():
    print('Voce nao digitou uma opção valida!')

while True:
    
    mostrar_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        adicionar_produto(lista_compras)

    elif opcao == '2':    
        alterar_produto(lista_compras)

    elif opcao == '3':
        excluir_produto(lista_compras)
    
    elif opcao == '4':
        mostrar_lista(lista_compras)
    
    elif opcao == '5':
        encerrar()
        break

    else:
        digito_invalido()
