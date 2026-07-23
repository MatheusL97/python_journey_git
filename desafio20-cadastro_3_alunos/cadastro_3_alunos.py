alunos =[]

for aluno in range(3):
    nome = input('Digite o nome do aluno: ').capitalize()
    idade = int(input('Digite a idade do aluno: '))
    curso = input('Digite o curso do aluno: ').capitalize()
    novo_aluno = {'nome': nome,
                'idade': idade,
                'curso': curso}
    alunos.append(novo_aluno)

for aluno in alunos:
    print('==== ALUNO CADASTRADO ====')
    for chave, valor in aluno.items():
        print(f'{chave.capitalize()}: {valor}')
    print()

print(f'Quantidade de alunos cadastrados: {len(alunos)}')