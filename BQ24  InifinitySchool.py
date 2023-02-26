print('                                        ATIVIDADE                                 ')
print('======================================================================================')
print('Faça um programa que verifique se um número é primo, e se for informe na tela.')
print('=='*40)
numero = int(input('Digite um número:'))
mult = 0
print ('ANALISANDO...')
for cont in range (2, numero):
    if (numero % cont == 0):
        print('Multiplo de ', cont)
        mult += 1
if(mult==0):
    print('É primo.')
else:
    print('Tem' , mult , 'múltiplos acima de 2 e abaixo de ', numero) 
