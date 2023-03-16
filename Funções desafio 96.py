print('===============================ATIVIDADE===============================================')
print("""Faça um programa que tenha uma FUNÇÃO chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a ÁREA DO TERRENO.""")
print('-='*40)
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com a {larg}x{comp} é de = {a}m2')


#Programa Principal.
print('Controle de Terrenos')
print('-'*20)
l= float(input('Largura (m):'))
c = float(input('Comprimento(m):'))
area(l, c)