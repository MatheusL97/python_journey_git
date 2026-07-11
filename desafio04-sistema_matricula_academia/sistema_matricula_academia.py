nome_aluno = input('Digite o nome do aluno: ')
idade_aluno = input('Digite a idade do aluno: ')
idade_aluno = int(idade_aluno)
possui_atestado = input('O aluno possui atestado medico? Responda somente com "sim" ou "nao". ')


if idade_aluno >= 16 and possui_atestado == 'sim':
    print(f'O aluno {nome_aluno} está apto a participar da turma especial de musculação.')

elif idade_aluno < 16 or possui_atestado == 'nao':
    print(f'O aluno {nome_aluno} não está apto a participar da turma especial de musculação.')

else:
    print('Você nao digitou sim ou não.')

