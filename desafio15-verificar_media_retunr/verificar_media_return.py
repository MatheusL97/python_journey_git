nome_aluno = input('Qual nome do aluno: ')

def verificarsituacao(media):
   
    if media < 0 or media > 10:
        return 'Média invalida'
    
    if media >= 7 and media <= 10:
        return 'Aprovado'
    
    elif media >= 5 and media <= 6.9:
        return 'Recuperação'
    
    elif media < 5 and media >= 0 :
        return 'Reprovado'

  
def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
    
nota1_float = float(input('Digite a primeira nota: '))
nota2_float = float(input('Digite a segunda nota: '))

media_aluno = media(nota1_float, nota2_float)

resultado = verificarsituacao(media_aluno)
print(f'\nNome do aluno: {nome_aluno} \n')
print(f'Média: {media_aluno} \n')
print(f'{nome_aluno} está: \n')
print(resultado)
