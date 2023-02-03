print('Pergunta:')
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,')
print('lendo e escrevendo o nome do escolhido.')
print('============================================================================================================')
import random
Mariana = str(input('Digite o nome do aluno 1:'))
Gustavo = str(input('Digite o nome do aluno 2:'))
Augusto = str(input('Digite o nome do aluno 3:'))
Nayra = str(input('Digite o nome do aluno 4:'))
lista = [Mariana, Gustavo , Augusto , Nayra ]
escolhido = random.choice(lista)
print('O sorteado para apagar o quadro vai ser {}:'.format(escolhido))
print('PARABÉNS, VOCÊ CONCLUIU O DESAFIO 19!')

