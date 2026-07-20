def titulo():
    print('1 - NORTE\n'
    '2 - NORDESTE\n'
    '3 - CENTRO-OESTE\n'
    '4 - SUDESTE\n'
    '5 - SUL')

def mostrar_estados():
    for estado in estados:
        print(f'- {estado}\n')

    print(f'PRIMEIRO ESTADO: {estados[0]}\n')
    print(f'ULTIMO ESTADO: {estados[-1]}')

    print(f'\nQUANTIDADE DE ESTADOS: {len(estados)}')

titulo()
opcao = input('ESCOLHA UMA OPÇÃO PARA VIZUALIZAR OS ESTADOS DA REGIAO SELECIOANDA: ')

if opcao == '1':
    print('\n===== ESTADOS DO NORTE =====\n')
    estados = ('Acre (AC)','Amapá (AP)','Amazonas (AM)','Pará (PA)','Rondônia (RO)','Roraima (RR)', 'Tocantins (TO)')
    mostrar_estados()

elif opcao == '2':
    print('\n===== ESTADOS DO NORDESTE =====\n')
    estados = ('Alagoas (AL)','Bahia (BA)','Ceará (CE)','Maranhão (MA)','Paraíba (PB)', 'Pernambuco (PE)','Piauí (PI)','Rio Grande do Norte (RN)','Sergipe (SE)')
    mostrar_estados()


elif opcao == '3':
    print('\n===== ESTADOS DO CENTRO-OESTE =====\n')
    estados = ('Goiás (GO)','Mato Grosso (MT)','Mato Grosso do Sul (MS)','Distrito Federal (DF)')
    mostrar_estados()


elif opcao == '4':
    print('\n===== ESTADOS DO SUDESTE =====\n')
    estados = ('São Paulo (SP)','Minas Gerais (MG)','Rio de Janeiro (RJ)','Espírito Santo (ES)')
    mostrar_estados()


elif opcao == '5':
    print('\n===== ESTADOS DO SUL =====\n')
    estados = ('Paraná (PR)','Rio Grande do Sul (RS)','Santa Catarina (SC)')
    mostrar_estados()


else:
    print('VOCE NAO DIGITOU UMA OPÇÃO VALIDA.')