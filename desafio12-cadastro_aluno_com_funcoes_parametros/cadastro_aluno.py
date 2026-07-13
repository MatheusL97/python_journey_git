nome = input('Nome do aluno: ')
idade = int(input('Idade do aluno: '))
curso = input('Qual curso faz: ')

def mostrar_aluno(nome, idade, curso):
    print(5 * '=' + ' DADOS DO ALUNO ' + 5 * '=')
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Curso: {curso}')

mostrar_aluno(nome, idade,curso)