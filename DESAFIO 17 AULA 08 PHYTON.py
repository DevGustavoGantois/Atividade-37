print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule')
print('e mostre o comprimeto da hipotenusa.')
print('=========================================================')
import math
CO = float(input('Digite o comprimento do cateto oposto do triângulo:'))
CA = float(input(' Digite o comprimento do cateto adjacente do triângulo:'))
H = math.hypot(CO, CA)
print('O valor do cateto oposto é {} e o valor do cateto adjacente é {} e o valor da hipotenusa será {:.2f}'.format(CO , CA , H))
print('DESAFIO 17 AULA 08 CONCLUIDO!')

