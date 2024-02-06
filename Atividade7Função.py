#Desenvolva um programa em Python que permita ao usuário digitar 
#várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as 
#notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" 
#que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, 
#e "Parabéns, sua média é 10" se a média for igual a 10.


def calcular_media(notas_aluno):

    while True:
        todas_notas = [float(nota) for nota in notas_aluno.split()]
        media_notas = sum(todas_notas) / len(todas_notas)
        return media_notas
    
def verificar_situacao(media_notas):

    if media_notas < 7:
        return 'Reprovado'
    elif media_notas >= 7:
        return 'Aprovado'
    elif media_notas == 10:
        return 'Parabéns'

notas_aluno = input("Digite as notas separadas por espaço:")

media_notas = calcular_media(notas_aluno)
situacao = verificar_situacao(media_notas)

print(f'A média do aluno é -> {media_notas}')
print(f"Situação do aluno é -> {situacao}")

    







