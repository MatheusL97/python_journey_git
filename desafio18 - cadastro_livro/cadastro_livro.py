titulo = input('Qual titulo do livro? ')
autor = input('Qual autor do livro? ')
editora = input('Qual editora do livro? ')
ano = int(input('Qual ano do livro? '))
pagina = int(input('Quantidade de paginas do livro? '))
genero = input('Qual genero do livro? ')

livro = {
    'titulo':titulo,
    'autor':autor,
    'editora':editora,
    'ano':ano,
    'paginas':pagina,
    'genero':genero
}

def livro_cadastrado(livro):
    print('\n', 5*'=',' LIVRO CADASTRADO ',5*'=','\n')
    for chave, valor in livro.items():
        print(f'{chave.capitalize()}:',f'{valor}\n')

livro_cadastrado(livro)