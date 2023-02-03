print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa')
print('que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print('============================================================================')
import random
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
escolha = [n1 , n2 , n3 , n4 ]
random.shuffle (escolha)
print('A ordem sorteada sera:')
print( escolha )

