nome_aluno = input('Digite no nome do aluno: ')
nota_aluno = input('Digite a nota do aluno: ')
nota_aluno = float(nota_aluno)

print(f'Nome do aluno: {nome_aluno}')

if nota_aluno >= 7:
    print('Situação: Aprovado')

elif nota_aluno >= 5:
    print('Situação: Recuperação')

else:
    print('Situação: Reprovado')