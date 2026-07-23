nome = input('Digite o nome do aluno: ').capitalize()
idade = int(input('Digite a idade do aluno: '))
curso = input('Digite o curso do aluno: ').capitalize()
telefone = input('Deseja acrescenter telefone: [S] ou [N] ')

aluno = {'nome': nome,
         'idade': idade,
         'curso': curso,
        }

if telefone == 's' or telefone == 'S':
    telefone = input('Digite o numero para contato: ')
    aluno['telefone'] = telefone

else:
    print("Opção invalida")


for chave, valor in aluno.items():
    if chave != "telefone":
        print(f"{chave}: {valor}")

print(f'Telefone: {aluno.get('telefone','Não informado')}')