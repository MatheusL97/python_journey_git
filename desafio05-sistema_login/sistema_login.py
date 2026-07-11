senha = 'python123'
senha_digitada = input('Digite a senha: ')

while senha_digitada != senha:
    print('Senha Incorreta!')
    senha_digitada = input('Digite a senha: ')

print('Você está logado!')