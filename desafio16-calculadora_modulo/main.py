import calculadora

def menu():
    print('\n1 - Somar\n' \
    '2 - Subtrair\n' \
    '3 - Multiplicar\n' \
    '4 - Dividir')

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

menu()
operacao = input('Escolha uma operação: ')

if operacao == "1":
    print(calculadora.somar(numero1,numero2))

elif operacao == "2":
    print(calculadora.subtrair(numero1,numero2))

elif operacao == "3":
    print(calculadora.multiplicar(numero1,numero2))

elif operacao == "4":
    print(calculadora.dividir(numero1,numero2))

else:
    print("Voce nao digitou uma operação valida!")