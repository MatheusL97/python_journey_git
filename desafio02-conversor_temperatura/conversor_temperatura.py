print('=== Conversor de Temperatura ===\n')
print('1 - Celsius para Fahrenheit')
print('2 - Fahrenheit para Ceslsius')
conversao = input('\nQual conversão deseja fazer: [1] [2]:  ')
conversao = int(conversao)


if conversao == 1:
    celsius = input('Digite o grau em Celsiu: ')
    celsius = int(celsius)
    if celsius != int(celsius):
        print('Voce nao digitou um numero valido')
    else:
        celsius_para_farenheit = celsius * 1.8 + 32
        print(f'Resultafo da conversão: {celsius_para_farenheit:.2f}ºF')

elif conversao == 2:
    farenheit = input('Digite o grau em Fahrenheite: ')
    farenheit = int(farenheit)
    if farenheit != int(farenheit):
        print('Voce nao digitou um numero valido')
    else:
        farenheit_para_celsius = (farenheit - 32)/1.8
        print(f'Resultafo da conversão: {farenheit_para_celsius:.2f}ºC')    

else:
    print('Digite apenas "1" ou "2".')

