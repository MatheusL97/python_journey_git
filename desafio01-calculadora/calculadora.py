# Abaixo recebemos do usuario dois numeros em string.
numero1 = input('Digite um numero: ')
numero2 = input('Digite outro numero: ')


if numero1.isdigit() and numero2.isdigit(): #fazendo a verificação se o usuario digitou um numero
    float_numero_1 = float(numero1) #tratamento do dado de String para Float
    float_numero_2 = float(numero2) #tratamento do dado de String para Float

    operador = input('Qual operação deseja fazer: [+][-][/][*]  ')

    if operador == '+':
        soma = float_numero_1 + float_numero_2
        print(f'Resultado: {soma}')

    elif operador == '-':
        subtracao = float_numero_1 - float_numero_2
        print(f'Resultado: {subtracao}')

    elif operador == '/':
        divisao = float_numero_1 / float_numero_2
        print(f'Resultado: {divisao}')
    
    elif operador == '*':
        multiplicacao = float_numero_1 * float_numero_2
        print(f'Resultado: {multiplicacao}')

    else:
        print('Voce nao digitou um operador!')
else:
    print("Voce nao digitou um numero valido!")
